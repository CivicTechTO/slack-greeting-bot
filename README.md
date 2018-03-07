# Slack Greeting Bot

Greetings! this is a Flask application that is hooked up to slack events api.
It sends a welcome message to the user that has just joined channels that this slackbot is configured to react to.

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

export CHANNEL_IDS='COMMA_SEPARATED_LIST_OF_CHANNEL_IDS'

# run the Flask app
python -m flask run

```

# Testing with Slack API

To test with the Slack API from your local development environment, would suggest `ngrok` to tunnel the flask app running on the machine's port.

# Deployment

We use [Heroku ](https://heroku.com) for hosting the chatbot service.

The `master` branch is setup to auto deploy to heroku whenever changes are pushed into the master branch. The `master` branch is a protected branch, changes can only be submitting through pull requests and requires revies before merging. See our [CONTRIBUTING](CONTRIBUTING.md) for 

The chatbot service lives at: [https://ctto-greetingbot.herokuapp.com](https://ctto-greetingbot.herokuapp.com)

# Contributing

Please see our [contributing guidelines](CONTRIBUTING.md).

# LICENSE

See [LICENSE](LICENSE.md)
