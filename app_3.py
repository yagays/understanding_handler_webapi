from parse import parse
from webob import Request, Response


class API:
    def __init__(self) -> None:
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = Response()

        # find handler
        handler = None
        for path, path_handler in self.routes.items():
            parse_result = parse(path, request.path)
            if parse_result:
                handler = path_handler
                kwargs = parse_result.named
        if handler:
            response.text = handler(**kwargs)
        else:
            response.status_code = 404
            response.text = "Not found."

        return response(environ, start_response)

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper


app = API()


@app.route("/home")
def home():
    return "Hello from the HOME page"


@app.route("/hello/{name}")
def greeting(name):
    return f"Hello, {name}"
