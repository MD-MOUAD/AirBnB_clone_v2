#!/usr/bin/python3
"""Script that starts Flask web application:

Requirements:
    - Web application must be listening on 0.0.0.0, port 5000.
    - Routes:
        /: display “Hello HBNB!”.
        /hbnb: display “HBNB”.
        /c/<text>: display “C ”, followed by the value of the text variable
            (replace underscore _ symbols with a space ).
        /python/<text>: display “Python ”, followed by the value of the text
            variable (replace underscore _ symbols with a space ).
        The default value of text is “is cool”
    - You must use the option strict_slashes=False in your route definition
"""

# Imports the Flask module and creates a Flask web server from the Flask module
from flask import Flask

# Creates a new web application object, which we’ll use to configure routes.
app = Flask(__name__)


# -This Decorator tells Flask what URL should trigger our function.
# -strict_slashes=False: option means the route is defined without trailing
# slashes and Flask redirects all URLs with trailing slashes to this route.
@app.route('/', strict_slashes=False)
def Disp_hello_HBNB():
    """This function is triggered when the user visits the root URL"""
    return 'Hello HBNB!'


# -This decorator tells Flask to trigger the show_HBNB() function when
#  the ‘/hbnb’ URL is visited.
@app.route('/hbnb', strict_slashes=False)
def Disp_HBNB():
    """This function is triggered when the user visits the ‘/hbnb’ URL"""
    return 'HBNB'


# -This decorator tells Flask to trigger the show_C(text) function when the
#  ‘/c/<text>’ URL is visited. <text> is a variable part of the URL.
# -Returns a string that starts with 'C ’ and ends with the <text> from
#   the URL, with underscores replaced by spaces.
@app.route('/c/<text>', strict_slashes=False)
def Disp_C(text):
    """This function is triggered when the user visits the ‘/c/<text>’ URL"""
    return 'C {}'.format(text.replace('_', ' '))


# -Decorator tells Flask to trigger the show_Python(text='is cool') function
# when the ‘/python’ URL is visited.
# -The strict_slashes=False option means the route is defined without trailing
#  slashes.
#  and Flask redirects all URLs with trailing slashes to this route.
# -Decorator tells Flask to trigger the show_Python(text) function when
#  the ‘/python/<text>’ URL is visited. <text> is a variable part of the URL.
@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Disp_Python(text='is cool'):
    """This function is triggered when the user visits either the
    ‘/python’ or ‘/python/<text>’ URL.
    """
    return 'Python {}'.format(text.replace('_', ' '))
    """ returns a string that starts with 'Python ’ and ends with the <text>
    from the URL, with underscores replaced by spaces. If no <text> is provided
    in the URL, it defaults to ‘is cool’.
    """


# Set socket to run the app on
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
