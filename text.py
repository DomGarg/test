from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

account_sid = 'ACb0cf08833e40e8ba91eda2f822201d43'
auth_token = '4c4a4cffd5e80692cd6b0f74e1027e1b'
client = Client(account_sid, auth_token)


@app.route('/')
def index():
    return '<h1>Deployed to heroku baby</h1>'

@app.route('/sms', methods=['POST', 'GET'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    message_body.splitlines()
    #resp = MessagingResponse()
    #resp.message('Hello {}, you said: {}'.format("+19056060506", message_body[0]))
    message = client.messages.create(body="hi", from_='+16475576348', to='+19056060506')
    print(message.sid)
    #return str(resp)
