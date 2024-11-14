import dash
from dash import Dash, dcc, html, Input, Output, callback
from cache_object import cache, cache_timeout
import datetime

dash.register_page(__name__)

def layout():
    return [html.Div(
            "This page is empty. We only require multipage environemnt to show how memoize can be sset up in such cases."
        )
    ]