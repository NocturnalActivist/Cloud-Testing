#!/usr/bin/python3

import requests
import flask

url = ('https://newsapi.org/v2/everything?'
       'q=Health&'
       'from=2021-05-24&'
       'sortBy=popularity&'
       'totalResults=10&'
       'apiKey=d0d00606e43a405ba369dcb3943fb80b')

response = requests.get(url)

articles = []
articles = response.json()["articles"]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def article():
    return articles.json()

app.run
