#!/usr/bin/python3
"""
0-hell_route - starts a Flask web app
"""
from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_hbnb():
    """ outputs 'Hello HBNB!' """
    application.url_map.strict_slashes = False
    return 'Hello HBNB!'

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
