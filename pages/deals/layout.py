from dash import html


def deals_layout():
    return html.Div(children=[
        html.H1(children='Today''s'' Deals'),
        html.Div(children='''
            Deals...
        ''')
    ])