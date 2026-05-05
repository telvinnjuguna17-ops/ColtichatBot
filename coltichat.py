from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import anthropic
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system="You are Coltibot, a helpful assistant for a restored vehicle dealership. You help customers with questions about classic cars, restoration, pricing, and availability.",
        messages=[{ "role": "user", "content": user_message }]
    )

    return jsonify({ "response": message.content[0].text })

if __name__ == "__main__":
    app.run(debug=True)