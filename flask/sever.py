from myapp import app

def wsgi():

    environ = {
        "request_type": "GET",
        "urs_schema": "HTTPS",
    }

    def start_response(status="", headers=""):
        # prepare response
        response = status + headers + "This is the response!"
        return [response]

    iterable = app(environ, start_response)
    for item in iterable:
        print(item)

if __name__ == "__main__":
    wsgi()
