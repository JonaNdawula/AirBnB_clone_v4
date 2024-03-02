#!/usr/bin/python3

""" Will Start a Clask web application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Gets rid of the current SQLAlchemy session """
    storage.close()


@app.route('/3-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is working """
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda state: state.name)
    states_with_sities = []

    for st in sorted_states:
        states_with_cities.append([st, sorted(st.cities,
                                  key=lambda city: city.name)])

    all_amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(all_amenities, key=lambda amenity: amenity.name)

    all_places = storage.all(Places).values()
    sorted_places = sorted(all_places, key=lambda place: place.name)

    return render_template('3-hbnb.html',
                           states=states_with_cities,
                           amenities=sorted_amenities,
                           places=sorted_places,
                           cahe_id=uuid.uuid4())


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
