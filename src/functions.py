import matplotlib.pyplot as plt

import io
import base64


def create_base64(df, columns: list[int], chart_type: str):
    import matplotlib
    matplotlib.use('Agg')
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#eaeaea')  # Jasnoszary

    if len(columns) == 2:
        i, j = columns
    else:
        i = columns

    if chart_type == 'points':
        ax.plot(df.iloc[:, i], df.iloc[:, j], '*r')
        ax.set(xlabel='x', ylabel='y', title='CSV Data Plot')
    elif chart_type == 'lines':
        ax.plot(df.iloc[:, i], df.iloc[:, j])
        ax.set(xlabel='x', ylabel='y', title='CSV Data Plot')
    elif chart_type == 'bars':
        ax.bar(df.iloc[:, i], df.iloc[:, j])
    elif chart_type == 'histogram':
        ax.hist(df.iloc[:, i])


    # save as base64
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf8')


def table_html_view(df):
    n_rows = df.shape[0]
    if n_rows > 6:
        reprezentation = df.iloc[[0, 1, 2, -3, -2, -1], :].to_html(
                justify='center',
                max_cols=7,
                max_rows=7,
                notebook=True
                )
    else:
        reprezentation = df.to_html(justify='center',
                                    max_cols=7,
                                    max_rows=7,
                                    notebook=True
                                    )
    return reprezentation
