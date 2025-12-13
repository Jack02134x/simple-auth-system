import os

import bcrypt
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

mycursor = mydb.cursor(dictionary=True)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Missing fields", 400

        mycursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        if mycursor.fetchone():
            return "Username already exists", 400

        hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        mycursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, hashed_pass),
        )
        mydb.commit()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        mycursor.execute(
            "SELECT id, password_hash FROM users WHERE username = %s", (username,)
        )
        user = mycursor.fetchone()

        if user and bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
            session["user_id"] = user["id"]
            return redirect("/dashboard")

        return "Invalid credentials", 401

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
