#!/usr/bin/python3
"""
6-number_odd_or_even - starts a Flask web application
"""
from flask import Flask
from flask import render_template
application = Flask(__name__)


@application.route('/number_odd_or_even/<int:n>')
def num_odd_even(n):
    """ injects is even or is odd to the html  """
    application.url_map.strict_slashes = False
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
