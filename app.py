from flask import Flask
from routes import tracker

app = Flask(__name__)

app.register_blueprint(tracker, url_prefix='/tracker/')


@app.route('/')
def index():
    return 'Go to <a href="http://127.0.0.1:5000/tracker/">Tracker</a>'


if __name__ == '__main__':
    app.run()
