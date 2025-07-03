import os  # This refers to the operating system module
from flask import Flask, request
from flask_cors import CORS

from dotenv import load_dotenv
from db import connect_db

load_dotenv()
connect_db(os.getenv)


app = Flask(__name__)
CORS(app, origins=[os.getenv("FRONTEND_URL")])


@app.route("/healthy", methods=["GET", "POST"])
def healthy():
    if request.method == "GET":
        return {"status": 200, "request_type": "GET"}
    else:
        return {"status": 200, "request_type": "POST"}


app.run(host="0.0.0.0", debug=True, port=80)
