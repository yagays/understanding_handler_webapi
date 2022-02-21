from parse import parse
from webob import Request, Response


class API:
    def __init__(self) -> None:
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

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


def home_handler():
    return "Hello from the HOME page"


def hello_handler(name):
    return f"Hello, {name}"


app = API()

app.add_route("/home", home_handler)
app.add_route("/hello/{name}", hello_handler)
