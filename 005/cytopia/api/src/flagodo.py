"""asdsad asd asd as."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Asdasd asd asd asd."""
    return '<span style="color:red">I am app 1</span>'