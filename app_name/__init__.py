from flask import Flask
from authentication import controller
from flask_sqlalchemy import SQLAlchemy
from app_name import authentication # import blueprints here

app = Flask('__name__')
db = SQLAlchemy(app)

#register blueprints here
app.register_blueprint(authentication)

app.config_from_object('config')