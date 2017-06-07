"""
contains code for migration of models to the database
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app_name import app
from app_name import db

db = SQLAlchemy(app)
migrate = Migrate(app, db)