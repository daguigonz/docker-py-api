from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/api/v1/users")
def users():
    return jsonify({"users": [{"name": "Daniel Aguirre"}, {"name": "John Doe"}]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
