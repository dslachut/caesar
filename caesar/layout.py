import dash_bootstrap_components as dbc
from dash import html


def page_header(page_title: str) -> dbc.Row:
    return dbc.Row(
        [
            html.H1(page_title),
            html.Hr(),
        ]
    )
