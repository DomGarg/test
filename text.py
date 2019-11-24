from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

lastClientRequest = None
clientRequests = {}
startingMessage = 'Hello and Welcome to renoSMS!!!\n\nReceiving multiple quotes for your desired home project is just seconds away!\n' \
                  'Please follow the following format so that we can properly process your message:\n' \
                  '\nLine 1: Select the appropriate number to match the construction sepcialist for your project' \
                  '\nLine 2: The description of your home project' \
                  '\n(And remember the more details that you include... the better the estimate you will receive from our connected construction speicalists!!)\n' \
                  'Heres an example:\n\n' \
                  '1\n' \
                  'PERSONALMESSAGE\n' \
                  'PERSONALMESSAGE\n' \
                  'PERSONALMESSAGE\n' \
                  'Lastly here are the options to select from:\n' \
                  '1. Painter\n' \
                  '2. Roofer\n' \
                  '3. Welder\n' \
                  '4. Plaster\n' \
                  '5. Carpentry\n' \
                  '6. Drywall\n' \
                  '7. Electrician\n' \
                  '8. Plumber\n' \
                  '9. Taping\n' \
                  '10. Masonry\n' \
                  '11. Tiles\n' \
                  '12. Carpet Installer\n' \
                  '13. Cement & Concrete Finisher\n' \
                  '14. Fencer/Fence Erector\n' \
                  '15. Flooring Installer\n' \
                  '16. HVAC\n' \
                  '17. Insulation\n' \
                  '18. Landscaper\n'

linkSkills = {"1": "Painter", "2": "Roofer", "3": "Welder", "4": "Plaster", "5": "Carpentry", "6": "Drywall", "7": "Electrician", "8": "Plumber", "9": "Taping", "10": "Masonry", "11": "Tiles", "12": "Carpet Installer", "13": "Cement & Concrete Finisher", "14": "Fencer/Fence Erector", "15": "Flooring Installer", "16": "HVAC", "17": "Insulation", "18": "Landscaper"}
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
    original_message_body = request.values.get('Body', None)
    message_body = original_message_body.split("\n", 1)
    found = 0
    for i in userForms.Companies:
        if i.getPhoneNumber() == message_body:
            message = client.messages.create(body=original_message_body, from_=i.getPhoneNumber(), to= lastClientRequest)
            return str(message.sid)

    sendBaseMessage = 0
    ##then this message is from a client and check if they have already messaged us!
    if(number not in clientRequests):
        lastClientRequest = number1
        sendBaseMessage += 1
        clientRequests.update({number: sendBaseMessage})
        message = client.messages.create(body=startingMessage, from_=i.getPhoneNumber(), to= lastClientRequest)
        return str(message.sid)

    clientRequest.pop(number)

    lastClientRequest = None
    compare = linkSkills.get(message_body)
    for i in userForms.Companies:
        if i.getSkills() == compare:
            message = client.messages.create(body=compare, from_='+16475576348', to='+19056060506')
            print(message.sid)


    #resp = MessagingResponse()
    #resp.message('Hello {}, you said: {}'.format("+19056060506", message_body[0]))
    #message = client.messages.create(body=message_body, from_='+16475576348', to='+19056060506')
    #print(message.sid)
    return str(message.sid)
