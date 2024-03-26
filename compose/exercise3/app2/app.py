from flask import Flask, render_template, request
import redis
from markupsafe import escape

app = Flask(__name__)
db = redis.Redis(host="db", port=6379, decode_responses=True)


@app.route('/<username>/movie', methods=['GET'])
def movie(username):
    movie = db.get(escape(username))
    if movie:
        return {"response": {"username": username, "movie": movie}}
    return {"response": f"User with name {username} not found!"}


if __name__ == '__main__':
    app.run()
