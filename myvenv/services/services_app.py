#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import render_template

import simplejson as json

import services_scraper as ss

'''
import werkzeug
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
'''


app = Flask(__name__)


@app.context_processor
def ss_func(): 
    for url in ss.urls:
        ss.get_info(url)
        return dict(forward=ss.get_info.full_set)


@app.route('/services', methods=['GET','POST'])
def post_solicitation():
    #return jsonify('connected')
    #return jsonify(ss.get_info.full_set.full_set)
    return render_template('services_template.html')
        
    
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
