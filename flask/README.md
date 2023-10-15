After reading Flask's documentation, It wasn't really clear how "global" App and Request contexts work. This example tries to mimic some of Flask's request dispatch and context
management functionality. If interested, look at app.py, ctx.pt and globals.py in Flask's source code. Short explanation below:

WSGI server will call the Flask app object with request parameters as a dict and a callable for response. Flask app object itself should be a callable. It could be a function object, a 
callable class object etc. Flask uses callable class object i.e. implements ```__call__``` method.
Flask will push app context, request context, send appropriate signals, prepare response and send response back using the callable provided by the WSGI server and pop out the contexts.

At the start of a request, if app context is not pushed, Flask will push the app context and then push the request context.
AppContext and RequestContext are context managers which are set as a value to a context variable. Context manager ```__enter__``` and ```__exit__``` methods are used to push and pop the context respectively. Context var is a thread safe way to implement locally global like functionality so different functions, views can access them without actually passing the objects around. 

When context var value it set during ```__enter__```, ```set()``` returns a token which refers to the previous value of the context var. This token get pushed on to the stack. When current context ends during ```__exit__```, this token is popped from the stack and context var's value is reset to the previous context using ```reset()```. ```g``` and ```current_app``` are proxies to this context variable. Hence, updates to ```g``` in one app context are isolated from another app context. Request context vars and their proxies ```request``` and ```session ``` work in similar way.

