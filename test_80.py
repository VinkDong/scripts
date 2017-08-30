from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('Hello World! 80 port')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 80, application)