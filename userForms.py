
# userForms.py
#
# Attribution Information: The RenovationApp was created at PAB @UWO campus
# The core projects were created by Dominic Gargala, Adrian Kalafut, and Elizabeth Lenkic

Companies = {"Painter":[], "Roofer":[], "Welder":[], "Mechanic":[], "Plaster":[], "Carpenter": [], "Drywall": [], "Electrician": [], "Plumber": [], "Taping": [], "Masonry": [], "Tiles":[], "Carpet Installer": [], "Cement & Concrete Finisher": [], "Fencer/Fence Erector": [], "Flooring Installer":[], "HVAC":[], "Insulation": [], "Laborer": [], "Landscaper":[], "Mason":[]}


class Company(object):
    ##Constructor for Company User form
    ##Will contain all important information about the Company
    ##All companies will be stored in a dictionary outlining there skills (what trades they speicalize in)
    def __init__(self, name, skills, phoneNumber, emailAddress, companyInfo):
        self.name = name

        ##Update our dictionay of Companies associated with particular skills
        ##Go through the skill(s) the company provided us with and add this Company to each skill they speicliaze within our dictionary
        ##This will be used to reference specific companies when receiving Customer renovation requests
        if isinstance(skills, list):
            for i in skills:
                temp = Companies.pop(i)
                temp.append(self)
                Companies.update({i:temp})
        else:
            temp = Companies.pop(skills)
            temp.append(self)
            Companies.update({skills:temp})
        self.phoneNumber = phoneNumber
        self.email = emailAddress
        self.info = companyInfo

    ##Getter method
    ##Returns the name of the Company associated with this object
    def getName(self):
        return self.name

    ##Getter method
    ##Returns the phone number of the Company associated with this object
    def getPhoneNumber(self):
        return self.phoneNumber

    ##Getter method
    ##Returns the email address of the Company associated with this object
    def getEmail(self):
        return self.email

    ##Getter method
    ##Returns info about the Company associated with this object
    def getInfo(self):
        return self.companyInfo

    ##Setter method
    ##Changes the name of the Company associated with this object with the one passed through param
    def setName(self, newName):
        self.name = name

    ##Setter method
    ##Changes the name of the Company associated with this object with the one passed through param
    def setName(self, newName):
        self.name = name

    ##Setter method
    ##Changes the phone number of the Company associated with this object with the one passed through param
    def setPhoneNumber(self, newNumber):
        self.phoneNumber = newNumber

    ##Setter method
    ##Changes the email address of the Company associated with this object with the one passed through param
    def setEmail(self, newEmail):
        self.email = newEmail

    ##Setter method
    ##Changes info about the Company associated with this object with the one passed through param
    def setInfo(self, newInfo):
        self.companyInfo = newInfo

