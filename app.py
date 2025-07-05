from flask_cors import CORS

from flask import Flask, request, jsonify, render_template
from chatbot_model import predict_intent
from response_map import get_response

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    print("Received data:", data)  # DEBUG

    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    intent = predict_intent(user_input)
    print("Predicted intent:", intent)  # DEBUG

    response = get_response(intent)
    print("Bot response:", response)  # DEBUG

    return jsonify({"intent": intent, "response": response})

if __name__ == "__main__":
    app.run(debug=True)
