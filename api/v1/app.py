#!/usr/bin/python3
storage_get_count
"""first endpoint (route) will be to return the status of my API:"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')

app = Flask(__name__)

"""Inintialize APIs"""
from os import getenv
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
master
app.register_blueprint(app_views)


@app.teardown_appcontext
storage_get_count
def db_teardown(error):
    """closes db connection session"""
    storage.close()


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
=======
def tear_down(error):
    """Removes the SQLAlchemy session"""
    storage.close()


@app.errorhandler(404)
def not_found(message):
    """Handler for 404 errors.
           Parameters:
               message [str]: message to display.
           Returns:
               The HTTP response.
    """
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', default='0.0.0.0'),
        port=int(getenv('HBNB_API_PORT', default=5000)),
        threaded=True
    )
master
