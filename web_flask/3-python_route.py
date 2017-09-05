#!/usr/bin/python3
"""a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)

""" Route: / """
@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return 'Hello HBNB!'

""" Route: /hbnb """
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'

""" Route: /c/<string:text> """
@app.route('/c/<string:text>', strict_slashes=False)
def display_c(text):
    text = text.replace("_"," ")
    return 'C {}'.format(text)

""" Route: /python/* """
@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def display_python2(text="is cool"):
    text = text.replace("_"," ")
    return 'Python {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)