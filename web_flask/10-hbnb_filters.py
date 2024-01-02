#!/usr/bin/python3
"""Script that starts a Flask web application:
-web application  listens on 0.0.0.0, port 5000.
-Routes:
   /hbnb_filters: : display a HTML page like 6-index.html
   ....see rest in readme file
"""
from models import storage
from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
