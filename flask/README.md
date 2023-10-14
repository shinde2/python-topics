After reading Flask's documentation, It wasn't really clear how "global" App and Request contexts work. This example tries to mimic some of Flask's request dispatch and context
management functionality. If interested, in Flask's source code, look at app.py, ctx.pt and globals.py. Short explanation below:

WSGI server will call Flask app object with request parameters as a dict and a callable for response. Flask app object itself should be a callable. It could be a function object, a 
callable class object etc. Flask uses callable class object i.e. implements \__call__ method.
Flask will push app context, request context, send appropriate signals, prepare response and send response back using the callable provided by the WSGI server and pop out the contexts.





