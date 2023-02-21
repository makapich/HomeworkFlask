from flask import Flask, Response
from faker import Faker
import pandas as pd
import requests
import flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/requirements/')
def show_requirements():
    with open('requirements.txt', encoding="utf-8") as rt:
        req = rt.read()
    return Response(req, mimetype="text/plain")





@app.route('/generate-users/')
def generate_users():
    faker = Faker()
    count = int(flask.request.args.get('count', default=100))
    user_data = []
    for _ in range(count):
        user_data.append((faker.email(),faker.name()))
    response = flask.jsonify(data=user_data)
    return response



@app.route('/mean/')
def mean():
    dataset = pd.read_csv('hw.csv')
    average = dataset.mean()

    return f"Средний рост {round(average.values[1]*2.54)} сантиметра, средний вес {round(average.values[2]/2.2)} килограмм"


@app.route('/space/')
def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts_count = r.json()['number']
    response = flask.jsonify(count=astronauts_count)
    return response

if __name__ == "__main__":
    app.run()
