from globals import cv_app

class AppContext:

    def __init__(self, app):
        print("Creating application context...")
        self.y = "a"
        self.app = app
        self.stack = []

    def push(self):
        self.stack.append(cv_app.set(self))
        print("App context pushed.")

    def pop(self):
        current_ctx = cv_app.get()
        cv_app.reset(self.stack.pop())
        print("App context popped.")

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, *args):
        self.pop()


class Flask:

    def __init__(self):
        print("Creating flask app...")

    def app_context(self):
        return AppContext(self)

    def __call__(self, environ, start_response: callable) -> "Response":
        
        print("Request dispatched...")
        return start_response()


app = Flask()
