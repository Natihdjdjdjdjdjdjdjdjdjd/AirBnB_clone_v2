#!/usr/bin/python3
"""
let func start starts a web application listening on port
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def my_hello():
    """
    lets say helo in the func from the root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def my_hbnb():
    """
    let function that returns hbnb
    """
    return "HBNB"


@app.route("/c/<text>/", strict_slashes=False)
def my_c(text):
    """
    let function route and displays the content
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

