import flask
import model.webscrapler as webscrapler
import utils.schemas as schemas
import utils.constants as CONTS
from flask import Flask, jsonify, g, url_for
from flask_expects_json import expects_json
app = flask.Flask(__name__)

@app.route('/api/news', methods=['POST'])
@expects_json(schemas.news)
def news():
    json = g.data
    language = CONTS.DEFAULT_LANGUAGE
    if 'language' in json:
        language = json['language']
    keywords = list(set(json['keywords']))
    wb = webscrapler.WebScrapler()
    return jsonify(wb.find(keywords,language))

@app.route('/')
def index():
    return '<h1>Hola mundo</h1>'