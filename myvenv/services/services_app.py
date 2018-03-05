#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify, make_response, render_template


import services_scraper as ss



app = Flask(__name__)


@app.context_processor
def for_template(): 
    #return jsonify('connected')
    for url in ss.urls:
        master_list = []
        ss.get_info(url)
        #keys = range(0, len(ss.full_set))
        values = ss.full_set
        master_list.append(ss.full_set)
        #parent_dict = {key:value for key, value in enumerate(values)}
        return (dict(parent_dict=master_list))
        #parent_dict = dict(zip(keys, values))
        #return jsonify(master_list)


@app.route('/', methods=['GET'])
def return_temp():
    return render_template('services_template.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
