from flask import Flask, request
from weather import get_weather

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/weather')
def weather():
    city_name = request.args.get('location')
    return get_weather(city_name)
