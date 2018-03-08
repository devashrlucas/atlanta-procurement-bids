#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify, make_response, render_template

import services_scraper as ss



app = Flask(__name__)


@app.context_processor
def for_template(): 
    for url in ss.urls:
        master_list = []
        ss.get_info(url)
        master_list.append(ss.full_set)
        return (dict(parent_dict=master_list))


@app.route('/', methods=['GET'])
def return_temp():
    return render_template('services_template.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == '__main__':
    app.run()
