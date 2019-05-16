from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/control", methods=["GET"])
def control():
    return render_template("control.html")


@socketio.on("broadcast")
def broadcast():
    emit("play", broadcast=True)
