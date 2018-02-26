#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import render_template

import simplejson as json

import itertools

from services_scraper import got_info



app = Flask(__name__)

@app.route('/services', methods=['GET','POST'])
def post_solicitation():
    full_array = []
    for item in got_info:
        full_array = [item]
    #got_info = get_info() #this works
        #return jsonify(full_array)
        return render_template('services_template.html', full_array = full_array)
    
'''
    for item in ss.forward:
        for entry in item.iteritems():
            #subdict = subdict
            if len(entry) == 0:
                abort(404)
            else:
                return jsonify(entry)
        #return render_template('services_template.html')
        #{key:value for key, value in ss.forward_output.iteritems()}
'''

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
