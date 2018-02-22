from flask import Flask, request, Response
import json
import requests
import os

SLACK_CLIENT_ID = os.environ['SLACK_CLIENT_ID']
SLACK_CLIENT_SECRET = os.environ['SLACK_CLIENT_ID']
SLACK_VERIFICATION_TOKEN = os.environ['SLACK_VERIFICATION_TOKEN']
SLACK_BOT_OAUTH_TOKEN = os.environ['SLACK_BOT_OAUTH_TOKEN']
SLACK_BOT_USERNAME = os.environ['SLACK_BOT_USERNAME']

app = Flask(__name__)

@app.route("/slack", methods=['POST'])
def inbound():
    jsonPayload = request.json
    event_type = jsonPayload["event"]["type"]
    token = jsonPayload["token"]
    team_id = jsonPayload["team_id"]
    user_id = jsonPayload["event"]["user"]
    channel_id = jsonPayload["event"]["channel"]
    message = welcome_message()
    outbound_uri_string = 'https://slack.com/api/chat.postMessage?token=%s&channel=%s&text=%s&as_user=true&username=%s' %(SLACK_BOT_OAUTH_TOKEN,user_id,message,SLACK_BOT_USERNAME)
    r = requests.get(outbound_uri_string)
    r.status_code
    return(jsonPayload["challenge"], 200)

def welcome_message():
    message = open('welcome_text.txt', 'r').read()
    return message

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)