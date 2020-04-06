import flask
import webscrapler
from flask import request, jsonify
app = flask.Flask(__name__)


@app.route('/api/news', methods=['POST'])
def home():
    keywords_req = request.get_json()
    ws = webscrapler.webScrapler()
    ans = ws.find(keywords_req["keywords"])
    return jsonify(ans)

app.run()