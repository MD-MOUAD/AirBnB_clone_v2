#!/usr/bin/python3
""" Script that starts a Flask web application:

    Requirements:
    - web application must be listening on 0.0.0.0, port 5000
    - You must use the option strict_slashes=False in your route definition
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

# Imports the Flask module and creates a Flask web server from the Flask module
from flask import Flask

#  Creates a new web application object, which we’ll use to configure routes.
app = Flask("__name__")


# -Decorator tells Flask what URL should trigger our function.
# -The strict_slashes=False option means the route is defined without
#   trailing slashes and Flask redirects all URLs with trailing slashes
#   to this route.
#  - def hello() This function is triggered when the user visits the root URL.
#    It returns the string ‘Hello HBNB!’.
@app.route('/', strict_slashes=False)
def Disp_hello():
    """Display 'Hello HBNB!."""
    return ("Hello HBNB!")


# -Decorator tells Flask to trigger the hbnb() function when the ‘/hbnb’ URL
#  is visited.
@app.route("/hbnb", strict_slashes=False)
# -This function is triggered when the user visits the ‘/hbnb’ URL.
#  It returns the string ‘HBNB’.
def Disp_hbnb():
    """Returns a given string"""
    return ("HBNB")


# -If this script is run directly (not imported), then it will run the app
#   on host 0.0.0.0 (which makes it publicly available) and on port 5000.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
