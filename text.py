from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import userForms
import requests
startingMessage = '\n\nHello and Welcome to renoSMS!!!\n\nReceiving multiple quotes for your desired home project is just seconds away!\n' \
                'Please follow the following format so that we can properly process your message:\n' \
                '\n------------------------'\
                '\nLine 1: Select the appropriate number to match the construction sepcialist for your project' \
                '\n------------------------\n\n'\
                '------------------------\n'\
                'Line 2: The description of your home project' \
                '\n------------------------\n'\
                '\nAnd remember the more details that you include... the better the estimate you will receive from our connected construction specialists!!\n' \
                '\nExample:' \
                '\n------------------------\n'\
                '----TEXT--MESSAGE--'\
                '\n------------------------\n'\
                '1\n' \
                'PERSONALMESSAGE\n' \
                'PERSONALMESSAGE\n' \
                'PERSONALMESSAGE' \
                '\n------------------------\n\n'\
                'Lastly here are the options you can enter on your first line of text(REMEMBER NUMBERS ONLY!):\n\n' \
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


    #link = "https://brandonassing.lib.id/tp-me@dev/getNumbers/"
    #f = requests.get(link)
    #f.json()
    #print(f.text[0])



    # Search GitHub's repositories for requests
    response = requests.get(
        'https://dgargala.lib.id/notyet@dev/getNumbers/',
        params={'q': 'requests+language:python'},
    )


    # Inspect some attributes of the `requests` repository
    json_response = response.json()

    for i in json_response:
        #temp = json_response[i]
        company = userForms.Company(i[0], i[1][1], "+" + i[1][0], None, None)
        temp = userForms.Companies.get(i[1][1])
        temp.append(company)
        userForms.Companies.update({i[1][1]:temp})

    repository = json_response
    return "<h1>Welcome to heroku app</h1>"


@app.route('/sms', methods=['POST', 'GET'])
def sms():

    number = request.form['From']
    original_message_body = request.values.get('Body', None)
    message_body = original_message_body.split("\n", 1)
    print("Original: " ,message_body)
    print("part original: ", message_body[0])
    ##Company has sent a text message
    if number in userForms.listOfAllCompanies:
        message = client.messages.create(body=original_message_body, from_='+16475576348', to= userForms.interactions[-1])
        return str(message.sid)


    ##Message was entered incorrectly by customer
    ##if(message_body[0] not in linkSkills and  not in clientRequests):
    ##message = client.messages.create(body="Error: You have entered information incorrectly", from_='+16475576348', to= lastClientRequest)
        ##return str(message.sid)
    companiesPresent = 0
    if(message_body[0].isdigit()):
        print("HERE: ", message_body )
        compare = linkSkills.get(str(message_body[0]))
        print("Compare: ", compare)
        list = userForms.Companies.get(compare)
        print("List: " , list)
        userForms.interactions.append(number)
        for j in list:
            print("Skills: ",j.getSkills())
            if j.getSkills() == compare:
                companiesPresent += 1
                message = client.messages.create(body=message_body[1], from_='+16475576348', to=j.getPhoneNumber())
                print(message.sid)

    ##then this message is from a client and check if they have already messaged us!
    else:
        print("THERE")
        print("NUMBER: ", number)
        message = client.messages.create(body=startingMessage, from_='+16475576348', to= number)
        return str(message.sid)

    if companiesPresent == 0 and not number in userForms.interactions:
        message = client.messages.create(body="Unfortunately we dont not have any workers within this particular trade", from_='+16475576348', to=number)

    #resp = MessagingResponse()
    #resp.message('Hello {}, you said: {}'.format("+19056060506", message_body[0]))
    #message = client.messages.create(body=message_body, from_='+16475576348', to='+19056060506')
    #print(message.sid)
    return str(message.sid)
