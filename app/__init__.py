from flask import Flask
from config import Config
from .routes.api import api
from .routes.errors import errors

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(errors, url_prefix="/")
