from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


@app.route("/healthy", methods=["GET", "POST"])
def healthy():
    if request.method == "GET":
        return {"status": 200, "request_type": "GET"}
    else:
        return {"status": 200, "request_type": "POST"}


app.run(host="0.0.0.0", debug=True, port=80)
