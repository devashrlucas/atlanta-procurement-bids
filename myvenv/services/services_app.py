#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import render_template

import services_scraper as ss


app = Flask(__name__)

@app.route('/')
def post_solicitation():
    if len(ss.forward_output) == 0:
        abort(404)
    else:
        for item in ss.forward_output:
            return jsonify(item)
        #return render_template('services_template.html')
        #{key:value for key, value in ss.forward_output.iteritems()}


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
