import dash
from dash import Dash, dcc, html, Input, Output, callback
from cache_object import cache, cache_timeout
import datetime

dash.register_page(__name__, path='/')

def layout():
    return [html.Div(
            "Home Page"
        )
    ]