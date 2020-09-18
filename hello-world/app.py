from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<b>Hello World!</b>"


app.add_url_rule("/", "index", index)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
