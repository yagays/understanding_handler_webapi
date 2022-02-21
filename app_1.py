from parse import parse
from webob import Request, Response


class API:
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = Response()

        # Routing
        if request.path == "/home":
            response.text = "Hello from the HOME page"
        elif request.path == "/about":
            response.text = "Hello from the ABOUT page"
        elif request.path.startswith("/hello"):
            parse_result = parse("/hello/{name}", request.path)
            name = ""
            if parse_result:
                name = parse_result.named["name"]
            response.text = f"Hello, {name}"
        else:
            response.status_code = 404
            response.text = "Not found."

        return response(environ, start_response)


app = API()
