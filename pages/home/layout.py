from dash import html


def home_layout():
    return html.Div(children=[
        html.H1(children="Home"),
        html.Div(children='''
            Home...
        ''')
    ])