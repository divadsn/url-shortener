import logging
from os import path
from flask import Flask

from shortener import default_config

# Initalize framework and load config
app = Flask(__name__)
app.config.from_object(default_config)
if path.exists('config.py'):
    import config
    app.config.from_object(config)

# Initialize loggers
app.logger
logging.warn('Something happened!')

# Load app modules
from shortener import routes