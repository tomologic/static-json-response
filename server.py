#!/usr/bin/env python
from flask import Flask, Response
from gevent.pywsgi import WSGIServer
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT'])
def do_post():
    return Response(json.dumps(returndata), mimetype='application/json')

if __name__ == "__main__":
    with open('data.json') as f:
        returndata = json.load(f)
    app.debug = True
    print("Listening on 8080")
    server = WSGIServer(('', 8080), app).serve_forever()
