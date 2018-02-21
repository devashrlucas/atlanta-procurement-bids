#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify

from services_scraper import keep_copy

app = Flask(__name__)
'''
@app.route('/')
def post_solicitation():
    return jsonify({'Solicitation': [item for item in keep_copy]})


if __name__ == '__main__':
    app.run(debug=True)
 '''
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(debug=True)

