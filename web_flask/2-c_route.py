#!/usr/bin/python3
"""model - flask app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ empty function that returns the string hello hbnb"""
    return "hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """an empty string that returns the string HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """a function to display text based on c"""
    text = text.replace('_', ' ')
    return 'C ' + '{}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
