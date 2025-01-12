import matplotlib.pyplot as plt

import io
import base64


def create_base64(df, columns: list[int], chart_type: str):
    import matplotlib
    matplotlib.use('Agg')

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#eaeaea')  # Jasnoszary

    
    # check if x and y are valid indexes
    for i in columns:
        if i < 0 or i >= df.shape[1]:
            return None

    if len(columns) == 1:
        i = columns[0]
        x = df.iloc[:, i].tolist()
        print(f'x:', x)
        if chart_type in ['points', 'lines', 'bars']:
            return None

    elif len(columns) == 2:
        i, j = columns[0], columns[1]
        x, y = df.iloc[:, i].tolist(), df.iloc[:, j].tolist()
        print(f'y:', y)
        print(f'x:', x)
        if chart_type == 'histogram':
            return None
    else:
        return None
    

    if chart_type == 'points':
        ax.plot(x, y, '*r')
        ax.set(xlabel='x', ylabel='y', title='CSV Data Plot')
    elif chart_type == 'lines':
        ax.plot(x, y)
        ax.set(xlabel='x', ylabel='y', title='CSV Data Plot')
    elif chart_type == 'bars':
        ax.bar(x, y)
    elif chart_type == 'histogram':
        ax.hist(x)


    # save as base64
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf8')


def table_html_view(df):
    n_rows = df.shape[0]
    if n_rows > 6:
        reprezentation = df.iloc[[0, 1, 2, -3, -2, -1], :].to_html(max_cols=7, max_rows=7)
    else:
        reprezentation = df.to_html(max_cols=7, max_rows=7)
    return reprezentation
