#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify
from flask import make_response
from flask import abort

import services_scraper as ss

keep_copy = ss.get_info()

app = Flask(__name__)

@app.route('/')
def post_solicitation():
        if len(keep_copy) == 0:
            abort(404)
        else:
            return jsonify({'Solicitation': keep_copy})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
'''
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(debug=True)
'''
