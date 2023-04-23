#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)  # __name__ is the name of the module


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays a HTML page with a list of states """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    city = sorted(list(storage.all(City).values()),  # sort by name
                    key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states, city=city)


@app.teardown_appcontext
def teardown(exception):
    """ Closes the session after each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
