#RestApiLotech

#!/usr/bin/python3

import requests
import flask
from flask import request, jsonify

url = ('https://newsapi.org/v2/everything?'
       'q=Health&'
       'qInTitle=Health&'
       'sortBy=relevancy&'
       'apiKey=d0d00606e43a405ba369dcb3943fb80b')

response = requests.get(url)

articles_ = []
articles_ = response.json()["articles"]
articles = []
articles = articles_[:10]

for article in articles:
 article["nomer"] = articles.index(article)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/articles/all', methods=['GET'])
def article():
    return jsonify(articles)

@app.route('/articles', methods=['GET'])
def article_nomer():
     if 'nomer' in request.args:
         nomer = int(request.args['nomer'])
     else:
         return "Error: No nomer field provided. Please specify a nomer\n"

     results = []
     for article in articles:
         if article["nomer"] == nomer:
              results.append(article)
     return jsonify(results)

app.run(host="0.0.0.0",port=443)
