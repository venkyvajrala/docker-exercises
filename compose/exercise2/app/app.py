from flask import Flask, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')
def get_user():
    version = os.getenv("VERSION")
    response = {"data": f'You are running version {version}'}
    return jsonify(response)
