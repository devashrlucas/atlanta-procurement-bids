#!flask/bin/python
from flask import Flask, jsonify

from services_scraper import keep_copy

app = Flask(__name__)

@app.route('/services/', methods=['POST'])
def post_solicitation():
    return jsonify({'Solicitation': [item for item in keep_copy]})


if __name__ == '__main__':
    app.run(debug=True)
