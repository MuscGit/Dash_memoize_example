import dash
from dash import Dash, dcc, html, Input, Output, callback
from cache_object import cache, cache_timeout
import datetime

dash.register_page(__name__)

def layout():
    return [html.Div(
            [
                dcc.Dropdown(
                    id="dropdown",
                    options=['option1', 'option2', 'option3'],
                    clearable=False,
                ),
                html.Br(),
                html.Div('Callback has not been yet triggered', 
                         id = 'callback_output')
            ]
        )
    ]

@cache.memoize(timeout=cache_timeout)
def cached_function(value):
    cached_time = datetime.datetime.now()
    expiry_time = cached_time + datetime.timedelta(seconds=cache_timeout)
    return f"Function output for value: {value} was cached at {cached_time.hour}:{cached_time.minute}:{cached_time.second} and will expire at {expiry_time.hour}:{expiry_time.minute}:{expiry_time.second}"

@callback(
        Output("callback_output", "children"), 
        Input("dropdown", "value"),
        prevent_initial_call=True
)
    
def update_div(value):
    return f"Callback has been called at {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second} with value {value} - {cached_function(value)}"

