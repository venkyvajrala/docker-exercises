from flask import Flask, render_template, request
import redis

app = Flask(__name__)
db= redis.Redis(host="db",port=6379,decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def movie():
    if request.method == 'POST':
        username = request.form['username']
        movie = request.form['movie']
        db.set(username,movie)
    return render_template('data.html')

if __name__ == '__main__':
    app.run()
