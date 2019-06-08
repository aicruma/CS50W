from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("index02.html", names=names)
