#!/usr/bin/env python3
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    print("Cookie header raw: {}".format(request.headers['Cookie']))
    print("cookies: {}".format(request.cookies))
    return "Got it!\n"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
