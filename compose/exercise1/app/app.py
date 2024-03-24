from flask import Flask, jsonify
import os
import json
import redis
from dotenv import load_dotenv

load_dotenv("app.env")
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)


@app.route('/')
def get_user():
    username = os.getenv("USERNAME")
    email = os.getenv("USER_EMAIL")
    hobbies = json.loads(os.getenv("HOBBIES"))

    response = {"data": {"username": username,
                         "email": email, "hobbies": hobbies}}

    return jsonify(response)
