#!/usr/bin/env python
import sys
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT'])
def do_post():
    return Response(json.dumps(returndata), mimetype='application/json')
    return flask.jsonify(**returndata)

if __name__ == "__main__":
    with open('data.json') as f:
        returndata = json.load(f)
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
