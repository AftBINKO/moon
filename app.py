from flask import Flask, redirect, url_for, render_template
from config import *

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return redirect(url_for("home"))


@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(host='127.0.0.2', debug=DEBUG)
