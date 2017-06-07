"""
    contains all the top level rotes for the project; such as homepage etc
"""
from flask import redirect, url_for, jsonify, render_template, Blueprint

from app_name import app

main = Blueprint('Main',__name__)

#route for index page
@main.route('/index')
def index():
    return "render_template(index.html)"