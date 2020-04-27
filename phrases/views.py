from phrases.app import app


@app.route("/")
def index():
    return "hello world"