from flask import Flask
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()

# Initializing application
app = Flask(__name__)

from app import views

