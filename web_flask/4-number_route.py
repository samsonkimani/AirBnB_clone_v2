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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """function to return text else default"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ a function that returns a value only when it is a number"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
