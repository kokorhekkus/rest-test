#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun


application = Flask(__name__)


@application.route('/', methods=['GET'])
def get():
    return '{"Output":"Goodbye World"}'


@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Goodbye World"}'


if __name__ == '__main__':
    flaskrun(application)
