# Slack Greeting Bot

Greetings! this is a Flask application that is hooked up to slack events api.
It sends a welcome message to the user that has just joined a channel this slackbot is install on.

# Requirements

This Flask application is using python3, since python2.7 will be retiring [soon!!!](https://pythonclock.org/)

# Installation

```shell
#clone this repo
git clone <thisgitrepo>
cd <thisgitrepo>

# make sure you have virtualenv installed
virtualenv venv

# activate your virtualenv
source venv/bin/activate

# Install requirementst
pip install -r requirements.txt

```

# Development

Once the installation is done, can run the application locally.

```shell

export FLASK_APP=app.py

export FLASK_DEBUG=1

# Export the environ variables needed for sending chat messages
export SLACK_BOT_OAUTH_TOKEN='YOU_BOT_TOKEN_FROM_SLACK'

export SLACK_BOT_USERNAME='YOUR SLACKBOT USERNAME'

export CHANNEL_ID='YOUR_WORKSPACE_CHANNEL_ID'

# run the Flask app
python -m flask run

```

# Testing with Slack API

To test with the Slack API from your local development environment, would suggest `ngrok` to tunnel the flask app running on the machine's port.