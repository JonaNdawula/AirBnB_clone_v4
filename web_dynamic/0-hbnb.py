#!/usr/bin/python3
""" Will start a Flask Web Application """
from models import storage
from models.state import state
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Get rid of the current SQLAlchemy session """
    storage.close()


@app.route('0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is working """
    all_states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    states_with_cities = []

    for st in sorted_states:
        states_with_cities.append([st, sorted(st.cities,
                                   key=lambda city: city.name)])

    all_amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(all_amenities,
                              key=lambda amenity: amenity.name)

    all_places = storage.all(Place).values()
    sorted_places = sorted(places_list, key=lambda place: place.name)

    return render_template('0-hbnb.html',
                           states=states_with_cities,
                           amenities=sorted_amenities,
                           places=sorted_places,
                           cache_id=uuid.uuid4())


if __name__ == 'main':
    """ Main function """
    app.run(host='0.0.0.0', port=5000)
