#!/usr/bin/env python3

from bottle import route, run, request

@route('/')
def apex():
    print("\nraw Cookie header: {}".format(request.headers.get("Cookie")))
    print("cookies: {}\n".format([ x for x in request.cookies.allitems()]))
    return "Got it.\n"

run(host='localhost', port=8080)

