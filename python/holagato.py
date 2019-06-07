from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/gato")
def gato():
    return "Hello, Gato!"
