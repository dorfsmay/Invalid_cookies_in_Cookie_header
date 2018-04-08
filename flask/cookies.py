#!/usr/bin/env python3
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    cookies_raw = "Cookie header raw: {}".format(request.headers['Cookie'])
    print(cookies_raw)
    cookies_formatted = "cookies: {}".format(request.cookies)
    print(cookies_formatted)
    return cookies_raw + '\n' + cookies_formatted + '\n'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
