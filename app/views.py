from flask import render_template
from app import app 

@app.route("/")
@app.route("/index")
def index():
	page = "index"
	return render_template("index.html", page="index")
	
@app.route("/boglight")
def boglight():
	return render_template("boglight.html")
	
@app.route("/videos")
def videos():
	return render_template("videos.html")

@app.route("/calendar")
def calendar():
	return render_template("calendar.html")

@app.route("/store")
def store():
	return render_template("store.html")

@app.route("/photos")
def photos():
	return render_template ("photos.html")