#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify

import services_scraper 

app = Flask(__name__)

@app.route('/')
def post_solicitation():
    return jsonify({'Solicitation': [item for item in services_scrapper.keep_copy]})


if __name__ == '__main__':
    app.run(debug=True)
'''
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(debug=True)
'''
