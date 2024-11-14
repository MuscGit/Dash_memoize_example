import dash
from flask_caching import Cache

cache = Cache(dash.get_app().server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

cache_timeout = 240