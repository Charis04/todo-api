#!api_env/bin/python
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Todo Home Page"