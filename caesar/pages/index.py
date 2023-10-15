import dash_bootstrap_components as dbc
from dash import dcc, html, register_page

from caesar.components import map_div
from caesar.layout import page_header

page_info = {"path": "/", "title": "CAESAR"}

register_page(__name__, path=page_info["path"], title=page_info["title"], name=page_info["title"])


layout = dbc.Container(
    [
        # page_header(page_info["title"]),
        map_div,
        # html.Hr(),
    ],
)
