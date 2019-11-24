from flask import Flask, request
from twilio import twiml


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Deployed to heroku baby</h1>'

@app.route('/sms', methods=['POST', 'GET'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == "__main__":
    app.run()