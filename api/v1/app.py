#!/usr/bin/python3
"""first endpoint (route) will be to return the status of my API:"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def db_teardown(error):
    """closes db connection session"""
    storage.close()

if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
