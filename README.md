Slack-Gemini Chatbot
This is a Flask-based Slack chatbot that integrates with Google's Gemini AI model to process and respond to Slack app mentions. The bot listens for mentions in Slack, processes the message using the Gemini AI model, and posts the response back to the Slack channel.

Prerequisites
Before setting up and running the application, ensure you have the following:

Python 3.8+ installed on your system.
A Slack App configured with a Bot Token and Signing Secret.
A Google API Key for accessing the Gemini AI model.
ngrok or a similar tool for exposing your local server to the internet (for Slack event subscriptions).
Basic familiarity with Python, Flask, and Slack API.
Setup Instructions
1. Clone the Repository
Clone this repository to your local machine or create a new project directory with the provided code.

bash

Collapse

Wrap

Run

Copy
git clone https://github.com/ankitbaghel01/Slack_AI_Bot.git

2. Create and Activate a Virtual Environment
Set up a Python virtual environment to manage dependencies.

bash

Collapse

Wrap

Run

Copy
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
Install the required Python packages using pip.

bash

Collapse

Wrap

Run

Copy
pip install flask google-generativeai slack-sdk python-dotenv
The dependencies include:

flask: For creating the web server.
google-generativeai: For interacting with the Gemini AI model.
slack-sdk: For interacting with the Slack API.
python-dotenv: For loading environment variables from a .env file.
4. Configure Environment Variables
Create a .env file in the project root directory and add the following environment variables:

bash

Collapse

Wrap

Run

Copy
GOOGLE_API_KEY=your-google-api-key
SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_SIGNING_SECRET=your-slack-signing-secret
GOOGLE_API_KEY: Obtain from Google Cloud Console for accessing the Gemini AI model.
SLACK_BOT_TOKEN: Obtain from your Slack App's "OAuth & Permissions" settings (starts with xoxb-).
SLACK_SIGNING_SECRET: Obtain from your Slack App's "Basic Information" settings.
5. Configure Your Slack App
Create a Slack App in the Slack API dashboard.
Enable Event Subscriptions:
Set the Request URL to https://<your-ngrok-url>/slack/events.
Subscribe to the app_mention event under "Subscribe to bot events."
Install the app to your Slack workspace and obtain the Bot Token.
Ensure the Signing Secret is available in your Slack App settings.
6. Expose Your Local Server (Optional)
To receive Slack events, you need to expose your local server to the internet. Use ngrok or a similar tool.

bash

Collapse

Wrap

Run

Copy
# Install ngrok if not already installed
ngrok http 3000
Copy the https URL provided by ngrok and use it in your Slack App's Event Subscriptions settings.

7. Run the Application
Start the Flask application.

bash

Collapse

Wrap

Run

Copy
python app.py
The application will run on http://localhost:3000. If using ngrok, Slack will send events to the ngrok URL.

How It Works
The Flask app listens for POST requests at the /slack/events endpoint.
Slack sends a url_verification challenge during setup, which the app responds to with the provided challenge.
When the bot is mentioned in a Slack channel (e.g., @BotName hello), the app:
Verifies the request using the Slack Signing Secret.
Extracts the user's message, removing the bot mention.
Sends the message to the Gemini AI model (gemini-1.5-flash-latest).
Posts the Gemini response back to the Slack channel.
The app uses environment variables for secure configuration.
Usage
Mention your bot in a Slack channel (e.g., @BotName What's the weather like today?).
The bot processes the message using Gemini AI and responds in the channel.
Troubleshooting
Invalid Request (403): Ensure the SLACK_SIGNING_SECRET is correct and the request is coming from Slack.
Gemini API Errors: Verify the GOOGLE_API_KEY is valid and has access to the Gemini model.
No Response in Slack: Check the Slack Bot Token and ensure the bot is added to the channel.
ngrok Issues: Ensure ngrok is running and the URL is correctly set in Slack's Event Subscriptions.
