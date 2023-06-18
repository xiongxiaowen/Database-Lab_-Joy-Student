from flask import Flask
from os import getenv


# create a Flask application instance, sets the secret key.
app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

# import the routes module.
import routes


