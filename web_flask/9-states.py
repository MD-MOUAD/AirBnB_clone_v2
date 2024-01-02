#!/usr/bin/python3
""" Python script that uses the Flask framework to start a web application:
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask, render_template

# Creates an instance of a Flask web application.
app = Flask(__name__)


# Defines a route for the web application
@app.route("/states", strict_slashes=False)
def states():
    """This function is executed when a user navigates to the /states route.
    It retrieves all “State” objects from the storage, and then uses the
    render_template function to generate an HTML page that lists all of
    these states.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


# Defines another route for the web application that includes a variable
#  part <id>
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    This function is executed when a user navigates to the /states/<id> route
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


# Starts the Flask web server if the script is being run directly (as opposed
#   to being imported as a module).
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
