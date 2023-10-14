from globals import cv_app

class AppContext:

    def __init__(self, app):
        print("Creating application context...")
        self.app = app
        self.tokens = []

    def push():
       pass 

    def __enter__(self):
        self.push()
        return self

    def __exit__(self):
        self.pop()


class Flask:

    def __init__(self):
        print("Creating flask app...")

    def __call__(self, environ, start_response: callable) -> "Response":
        
        print("Request dispatched...")
        return start_response()


app = Flask()
