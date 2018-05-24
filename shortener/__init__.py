import re
from os import path

from flask import (Flask, Response, jsonify, redirect, render_template,
    request, send_from_directory, url_for, session)

from shortener import default_config

app = Flask(__name__)
app.config.from_object(default_config)
if path.exists('config.py'):
    import config
    app.config.from_object(config)

@app.route('/hello')
def helloWorld():
    return "Hello World!"