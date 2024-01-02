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
        /number/<n>: display “n is a number” only if n is an integer.
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
    - You must use the option strict_slashes=False in your route definition.
"""
# -Imports the Flask module and render_template function from the Flask module.
# -render_template:is used to generate output from a template file based on the
#   Jinja2 engine that is found in the application’s templates folder.
from flask import Flask
from flask import render_template


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
#  when the ‘/python’ URL is visited.
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


# -This decorator tells Flask to trigger the Disp_number(n) function when the
# ‘/number/<n>’ URL is visited. <n> is a variable part of the URL and must be
#  an integer.
@app.route('/number/<int:n>', strict_slashes=False)
def Disp_number(n):
    """This function is triggered when the user visits the ‘/number/<n>’ URL.
    It returns a string that starts with '<n> ’ and ends with ‘is a number’.
    """
    return '{} is a number'.format(n)


# -This decorator tells Flask to trigger the show_number_template(n) function
#  when the ‘/number_template/<n>’ URL is visited. <n> is a variable part of
#  the URL and must be an integer.
@app.route('/number_template/<int:n>', strict_slashes=False)
def Disp_number_template(n):
    """Display a HTML page only if n is an integer;
    This function is triggered when the user visits ‘/number_template/<n>’URL.
    It uses Flask’s render_template to render a HTML template named
    ‘5-number.html’, passing <n> as a parameter to be used in that template.
    """
    return render_template('5-number.html', n=n)


# -If this script is run directly (not imported), then it will run the app on
# host 0.0.0.0 (which makes it publicly available) and on port 5000.
# Set socket to run the app on
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
