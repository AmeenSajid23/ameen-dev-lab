from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask backend is running"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")

    return jsonify({
        "message": f"Hello {username}, your email {email} was received!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
