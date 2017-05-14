#!/usr/bin/env python2

import sys
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(request.cookies)
    return Response('Hello World!\n')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, application)
