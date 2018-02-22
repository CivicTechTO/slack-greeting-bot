from flask import Flask, request, Response
import json
import requests
import os

SLACK_BOT_OAUTH_TOKEN = os.environ['SLACK_BOT_OAUTH_TOKEN']
SLACK_BOT_USERNAME = os.environ['SLACK_BOT_USERNAME']
CHANNEL_ID = os.environ['CHANNEL_ID']

app = Flask(__name__)

@app.route("/slack", methods=['POST'])
def inbound():
    jsonPayload = request.json
    
    event_type = jsonPayload["event"]["type"]
    token = jsonPayload["token"]
    team_id = jsonPayload["team_id"]
    user_id = jsonPayload["event"]["user"]
    channel_id = jsonPayload["event"]["channel"]
    if channel_id == CHANNEL_ID:
        message = welcome_message()
        outbound_uri_string = 'https://slack.com/api/chat.postMessage?token=%s&channel=%s&text=%s&as_user=true&username=%s' %(SLACK_BOT_OAUTH_TOKEN,user_id,message,SLACK_BOT_USERNAME)
        r = requests.get(outbound_uri_string)
        r.status_code
        print(channel_id)
        return("New user joined", 200)
    else:
        print(channel_id)
        return("Channel not defined for the slackbot", 400)
    
    #return(jsonPayload["challenge"], 200)
    

def welcome_message():
    message = open('welcome_text.txt', 'r').read()
    return message

if __name__ == "__main__":
    app.run()