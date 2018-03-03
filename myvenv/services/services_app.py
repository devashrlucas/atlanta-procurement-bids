#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify, make_response


import services_scraper as ss



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    master_list = []
    #return jsonify('connected')
    for url in ss.urls:
        ss.get_info(url)
        master_list.append(ss.full_set)
        return jsonify(master_list)
  

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
