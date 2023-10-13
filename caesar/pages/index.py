import dash_bootstrap_components as dbc
from dash import dcc, html, register_page

from caesar.layout import page_header

page_info = {"path": "/", "title": "CAESAR"}

register_page(__name__, path=page_info["path"], title=page_info["title"], name=page_info["title"])

ph = """## Placeholder

This is placeholder content.
"""

layout = dbc.Container(
    [page_header(page_info["title"]), dbc.Container(dcc.Markdown(ph)), html.Hr()],
)
