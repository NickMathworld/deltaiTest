import flask
import model.webscrapler as webscrapler
import utils.schemas as schemas
from flask import Flask, jsonify, g, url_for
from flask_expects_json import expects_json
app = flask.Flask(__name__)

@app.route('/api/news', methods=['POST'])
@expects_json(schemas.news)
def home():
    json = g.data
    wb = webscrapler.WebScrapler()
    return jsonify(wb.find(json['keywords']))
app.run()