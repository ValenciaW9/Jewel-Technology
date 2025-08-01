
## Valencia Walker's for Jewel.technology


from flask import Blueprint, request, jsonify
import openai
import os

ai = Blueprint('ai', __name__)

@ai.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt required"}), 400

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({"response": answer})
