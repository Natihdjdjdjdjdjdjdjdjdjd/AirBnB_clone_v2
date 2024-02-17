#!/usr/bin/python3
"""
let function starts a Flask web app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def my_hello():
    """let the func returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """let the func returns HBNB to the root rout"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
