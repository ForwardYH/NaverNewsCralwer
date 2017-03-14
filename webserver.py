# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, jsonify
from connection import Session
from newsdao import NewsDAO

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def hello_json():
    data = {'name': 'Youngho', 'family': 'Jeon'}
    return jsonify(data)


@app.route('/news/search/contents/<keyword>')
def search_news_contents(keyword):
    session = Session()
    newsdao = NewsDAO()
    data = newsdao.get_news_by_keyword_in_content(str(keyword))

    return jsonify(data)


@app.route('/news/search/title/<keyword>')
def search_news_title(keyword):
    session = Session()
    newsdao = NewsDAO()
    data = newsdao.get_news_by_keyword_in_title(str(keyword))

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
