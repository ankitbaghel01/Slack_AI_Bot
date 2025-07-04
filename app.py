import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
print("Gemini API Key:", os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
verifier = SignatureVerifier(os.getenv("SLACK_SIGNING_SECRET"))

# Use Gemini Chat model
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

chat = model.start_chat(history=[])


try:
    for model in genai.list_models():
        print("✅ Model available:", model.name)
except Exception as e:
    print("❌ Error:", e)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    if not verifier.is_valid_request(request.get_data(), request.headers):
        return "invalid request", 403

    data = request.json

    # URL verification
    if data.get("type") == "url_verification":
        return jsonify({"challenge": data.get("challenge")})

    # Handle app_mention
    if "event" in data:
        event = data["event"]
        if event.get("type") == "app_mention":
            user_input = event.get("text")

            # Remove bot mention
            cleaned_input = user_input.replace(f"<@{event.get('user')}>", "").strip()

            # Use Gemini for response
            try:
                 gemini_response = chat.send_message(cleaned_input)
                 print("Gemini response full:", gemini_response)
                 response_text = gemini_response.text
            except Exception as e:
                response_text = f"Error: {str(e)}"

            client.chat_postMessage(channel=event["channel"], text=response_text)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=3000)
