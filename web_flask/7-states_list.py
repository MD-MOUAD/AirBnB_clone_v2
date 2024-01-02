#!/usr/bin/python3
"""Script that starts a Flask web application:
- Your web application must be listening on 0.0.0.0, port 5000.
- You must use storage for fetching data from the storage engine (FileStorage
   or DBStorage) => from models import storage and storage.all(...).
- After each request you must remove the current SQLAlchemy Session:
    -Declare a method to handle @app.teardown_appcontext
    -Call in this method storage.close()
- Routes:
    -/states_list: display a HTML page: (inside the tag BODY).
    -H1 tag: “States”.
    -UL tag: with the list of all State objects present in DBStorage sorted
      by name (A->Z) tip.
    -LI tag: description of one State: <state.id>: <B><state.name></B>
- Import this 7-dump to have some data
- You must use the option strict_slashes=False in your route definition
"""
from models import storage
from flask import Flask, render_template
from models.state import State

# Creates an instance of a Flask web application.
app = Flask(__name__)


# -Defines a route for the web application. When a user navigates to
# <your-domain>/states_list in their web browser, the function defined
# directly below this line will be executed.
@app.route("/states_list", strict_slashes=False)
def Disp_states():
    """This function is executed when a user navigates to the /states_list
    route. It retrieves all “State” objects from the storage, and then uses
    the render_template function to generate an HTML page that lists all of
    these states.
    """
    states = storage.all()
    return render_template("7-states_list.html", states=states)


# -This decorator ensures that the function defined directly below it
# (def teardown(exc)) will be called when the application context ends,
#  which typically occurs after a request has been processed.
@app.teardown_appcontext
def teardown(exc):
    """
    This function is called after each request, and it closes the storage
    session.
    """
    storage.close()


# -Starts the Flask web server if the script is being run directly
# (as opposed to being imported as a module).
if __name__ == "__main__":
    app.run(host="0.0.0.0")
