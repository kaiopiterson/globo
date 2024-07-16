from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

api_bp = Blueprint('api', __name__)

from . import routes
