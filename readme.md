# Dash - memoize

As per Dash documentation, memoization stores the results of a function after it was called and re-uses the result if the function is called again with the same arguments.
This examample showcases that when we memoize a function with arguments, the specific value of those arguments is considered when the cache is generated.

Flask-Caching library is used for memoization, which allows to save the results in a shared memory database (eg. Redis) or a file in our filesystem. The latter is used in this example to start with.

The separation of the cache definition in cache_object/ allows us to use this in a multipage app; If cache was defined in app.py, this would lead to circular references of app