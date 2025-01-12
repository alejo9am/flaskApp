import io
from flask import Flask, render_template, request, session
from flask_session import Session
import pandas as pd

from src import functions as fn

app = Flask(__name__)
app.secret_key = "flaskkey"

#Configuration for Flask session to handle big .csv files
app.config['SESSION_TYPE'] = 'filesystem'  # Almacena las sesiones en el sistema de archivos
app.config['SESSION_FILE_DIR'] = './.flask_session/'  # Directorio para los archivos de sesión
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    table = ''
    name = ''
    img = ''

    return render_template('index.html',
                           name=name,
                           table=table,
                           img64base=img
                           )


@app.route('/upload', methods=['POST'])
def data_upload():
    table = ''
    name = ''
    img = ''

    if 'csv_file' in request.files:
        # <input type="file" id="myfile" name="csv_file"><br><br>
        # use name from input tag to upload file
        file = request.files['csv_file']
        name = file.filename
        df = pd.read_csv(file)
        table = fn.table_html_view(df)
        # make df 'global' between sessions
        session['df'] = df.to_json()
        session['name'] = name
        session['table'] = table

    return render_template('index.html',
                           name=name,
                           table=table,
                           img64base=img
                           )


@app.route('/chart', methods=['POST'])
def create_chart():
    table = ''
    name = ''
    img = ''

    if 'chart' in request.form:
        tmp = io.StringIO(session['df'])
        df = pd.read_json(tmp)
        name = session['name']
        table = session['table']

        columns = request.form['columns']
        columns = [int(i) for i in columns.split(',')]
        chart_type = request.form['chart_type'] 

        img = fn.create_base64(df, columns, chart_type)

        if img is None:
            img = 0

    return render_template('index.html',
                           name=name,
                           table=table,
                           img64base=img
                           )


if __name__ == '__main__':
    app.run(debug=True)
