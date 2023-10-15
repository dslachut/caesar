import dash_bootstrap_components as dbc
import dash_leaflet as dl
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, State, callback, dcc, get_asset_url, html
from dash_extensions.javascript import Namespace, arrow_function

from caesar.data import ar_crops

base_style = dict(weight=2, opacity=1, color="white", dashArray="3", fillOpacity=0.7)
elev_classes = [
    2.7997894,
    87.8501300,
    172.9004707,
    257.9508113,
    343.0011520,
    428.0514926,
    513.1018333,
    598.15217,
]  # for res=6
# elev_classes = [0.0, 76.1384735, 152.2769470, 228.4154205, 304.5538940, 380.6923675, 456.8308410, 532.9693145] # for res=7
elev_colorscale = ["#FFEDA0", "#FED976", "#FEB24C", "#FD8D3C", "#FC4E2A", "#E31A1C", "#BD0026", "#800026"]

ns = Namespace("myNamespace", "mySubNamespace")

crop_layer = dl.GeoJSON(
    data=ar_crops(),
    hideout=dict(style=base_style, colorscale=elev_colorscale, classes=elev_classes),
    style=ns("crop_style"),
    hoverStyle=arrow_function(dict(fillOpacity=0.9, dashArray="")),
)

map_div = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dl.Map(
                            [
                                dl.TileLayer(),
                                crop_layer,
                            ],
                            center=dict(lat=36.1, lng=-94.2),
                            zoom=12,
                            style={"height": "90vh"},
                            id="my-map",
                        ),
                    ],
                    width=12,
                ),
            ],
        ),
    ],
)
