# Dont ignore me! I'm a python package directory - (__init__)

import os
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set config (from cinfig.py, http://flask.pocoo.org/docs/0.12/config/#development-production)
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })