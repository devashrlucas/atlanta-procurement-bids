#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify

import services_scraper as ss

ss.keep_copy = ss.get_info()

app = Flask(__name__)

@app.route('/')
def post_solicitation():
    return jsonify({'Solicitation': [item for item in ss.keep_copy]})


if __name__ == '__main__':
    app.run(debug=True)
'''
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(debug=True)
'''
