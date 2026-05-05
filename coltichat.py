from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows your React app to talk to Flask

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Your logic here — for now just echo it back
    response = f"You said: {user_message}"

    return jsonify({ "response": response })

if __name__ == "__main__":
    app.run(debug=True)  # runs on http://127.0.0.1:5000