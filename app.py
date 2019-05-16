from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/send", methods=["POST"])
def send():

