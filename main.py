from flask import Flask, render_template, url_for, redirect, request, session, jsonify
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

load_dotenv(override=True)
app.secret_key = os.getenv("SECRET_KEY")

IST = pytz.timezone("Asia/Kolkata")
VALENTINES_DAY = IST.localize(datetime(2025, 2, 14, 0, 0, 0))
VALENTINES_DAY_UNIX_TIMESTAMP = int(VALENTINES_DAY.timestamp())
 
PASSWORD = os.getenv("PASSWORD")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]

        if password.upper() == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid password.")
    
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
        return render_template("countdown.html", valentines_day=VALENTINES_DAY_UNIX_TIMESTAMP)
    else:
        return render_template("home.html")
    
    return render_template("home.html")
    
# @app.route("/get_time_left")
# def get_time_left():
#     return jsonify({"time_left": get_seconds_left()})

@app.route("/viewhome")
def viewhome():
    return render_template("home.html")

@app.route("/logout")
def logout():
    session.pop("logged_in")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=4998)