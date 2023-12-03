from flask import Flask
from routes import tracker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(tracker, url_prefix='/tracker/')


@app.route('/')
def index():
    return 'Go to <a href="http://127.0.0.1:5000/tracker/">Tracker</a>'


if __name__ == '__main__':
    app.run()
