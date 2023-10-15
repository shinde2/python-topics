from contextvars import ContextVar

cv_app = ContextVar("App-Context-Var")
current_app = cv_app #Proxy(cv_app)
g = cv_app #Proxy(cv_app)


cv_request = ContextVar("Request-Context-Var")
request = cv_request #Proxy(cv_request)
session = cv_request #Proxy(cv_request)
