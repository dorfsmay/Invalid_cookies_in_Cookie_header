#!/usr/bin/env python3

from bottle import route, run, request

@route('/')
def apex():
    cookies_raw = "raw Cookie header: {}".format(request.headers.get("Cookie"))
    print(cookies_raw)
    cookies_formatted = "cookies: {}\n".format([ x for x in request.cookies.allitems()])
    print(cookies_formatted)
    return cookies_raw + '\n' + cookies_formatted + '\n'

run(host='localhost', port=8080)

