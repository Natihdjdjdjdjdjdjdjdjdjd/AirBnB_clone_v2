#!/usr/bin/python3
"""
a let the python starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def my_hello():
    """let we runt to returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def my_hbnb():
    """let the func rrturn returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def my_c(text):
    """let the func display value of the text var"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """let the we display the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
