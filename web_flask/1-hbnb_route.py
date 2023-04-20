#!/usr/bin/python3
""" model - hbnb """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """an empty function that returns the hello hbnb string"""
    return "hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ an empty function that returns the string hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
