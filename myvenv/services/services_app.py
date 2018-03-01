#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import render_template
from flask import Blueprint


import services_scraper as ss

'''
import werkzeug
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
'''


app = Flask(__name__)
#scraped = Blueprint("scraped", __name__, template_folder='templates')


@app.route('/services', methods=['GET', 'POST'])
def index():
    #return jsonify('connected')
    for url in ss.urls:
        ss.get_info(url)
        return jsonify(ss.master_list)
        #return jsonify(ss.full_set)
        #return jsonify('connected')
    #return render_template('services_template.html')

'''
@scraped.context_processor
def ss_func(): 
    def get_urls():
        for url in ss.urls:
            ss.get_info(url)
            return ss.get_info.full_set
    return dict(get_urls=get_urls)
'''

        
    
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
