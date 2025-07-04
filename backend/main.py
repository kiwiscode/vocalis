import os  # This refers to the operating system module
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from dotenv import load_dotenv
from db import connect_db

import bcrypt

load_dotenv()
conn = connect_db(os.getenv)


app = Flask(__name__)
CORS(app, origins=[os.getenv("FRONTEND_URL")])


@app.route("/healthy", methods=["GET", "POST"])
def healthy():
    if request.method == "GET":
        return {"status": 200, "request_type": "GET"}
    elif request.method == "POST":
        return {"status": 200, "request_type": "POST"}


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data["email"]
    password = data["password"]

    if len(email) < 1 or len(password) < 1:
        return (
            jsonify(
                {
                    "error": "All fields are mandatory. Please provide your email and password."
                }
            ),
            403,
        )

    if not len(password) >= 12:
        return (
            jsonify({"error": "Your password must contain: At least 12 characters"}),
            403,
        )

    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=salt)

    print(f"Actual Password: {password}")
    print(f"Hashed Password: {hash_password}")

    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hash_password.decode("utf-8")),
        )
        conn.commit()
        print("📦 'new user' is created in the table.")
        return {"status": 200}
    except Exception as e:
        print("❌ Error during registration:", e)
        conn.rollback()
        return {"status": 500, "error": str(e)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
