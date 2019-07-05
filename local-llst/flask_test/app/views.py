from flask import request

from flask_test.app import app
import json


@app.route("/")
def test():
    return 'Hello World'


@app.route("/test", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        return "world"
    return "Hello"


@app.route("/test/<name>")
def json_test(name=None):
    dic = {}
    dic['name'] = name
    return json.dumps(dic)
