#!/usr/bin/python3
"""Script to start a simple Flask web application on socket 0.0.0.0:5000

Requirements
     - Web application must be listening on 0.0.0.0 and port 5000.
     - Routes use option strict_slashes=False in thier definitions.
Routes
     / Display hello HBNB!.
"""

# imports the Flask module and creates a Flask web server from the Flask module
from flask import Flask

# Creates a new web application object, which we’ll use to configure routes.
app = Flask(__name__)

# Disable 404 status code on Accessing the URL with a trailing slash gloablly
# app.url_map.strict_slashes = False


# -Routes definitions
# -Decorator tells Flask what URL should trigger our function
# -The strict_slashes=False option means the route is defined without
#   trailing slashes and Flask redirects all URLs with trailing slashes
#   to this route.
@app.route('/', strict_slashes=False)
# -This function is triggered when the user visits the root URL.
# It returns the string ‘Hello HBNB!’.
def Disp_hello_HBNB():
    """Display 'Hello HBNB!.'"""
    return 'Hello HBNB!'


# -Set socket to run the app on
# -if this script is run directly (not imported),
#   then it will run the app on host 0.0.0.0 and on port 5000.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
