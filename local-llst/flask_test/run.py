from flask_test.app import app


@app.route("/")
def test():
    return 'Hello World'


if __name__ == '__main__':
    app.debug = True
    app.run()
