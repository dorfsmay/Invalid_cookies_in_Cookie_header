#!/usr/bin/env python3

import sys
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(request.cookies)
    response_text = 'Cookies:\n'
    response_text += str(request.cookies)
    response_text += '\n'
    return Response(response_text)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, application)
