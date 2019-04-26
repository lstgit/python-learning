from flask_test.app import app


@app.route("/")
def test():
    return 'Hello World'


@app.route("/test")
def index():
    return "Hello"
