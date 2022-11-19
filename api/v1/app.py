#!/usr/bin/python3
"""Inintialize APIs"""
from os import getenv
from Flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views


app = Flask(__name__)


app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(error):
    """Removes the SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', default='0.0.0.0'),
        port=int(getenv('HBNB_API_PORT', default=5000)),
        threaded=True
    )
