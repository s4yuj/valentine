from flask import Flask, render_template, url_for, redirect, request, session, jsonify
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

IST = pytz.timezone("Asia/Kolkata")
# Valentine's Day (February 14, 12:00 AM IST)
VALENTINES_DAY = IST.localize(datetime(2025, 2, 14, 0, 0, 0))

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")
    
    return render_template("login.html")

def get_seconds_left():
    now = datetime.now(IST)
    time_left = VALENTINES_DAY - now
    return max(0, int(time_left.total_seconds()))

@app.route("/home")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    time_left = get_seconds_left()
    if time_left > 0:
        return render_template("countdown.html", time_left=time_left)
    else:
        return render_template("home.html")
    
@app.route("/get_time_left")
def get_time_left():
    return jsonify({"time_left": get_seconds_left()})

@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=4998)