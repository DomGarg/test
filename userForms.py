
# userForms.py
#
# Attribution Information: The RenovationApp was created at PAB @UWO campus
# The core projects were created by Dominic Gargala, Adrian Kalafut, and Elizabeth Lenkic

Companies = {"Painter":[], "Roofer":[], "Welder":[], "Mechanic":[], "Plaster":[], "Carpentry": [], "Drywall": [], "Electrician": [], "Plumber": [], "Taping": [], "Masonry": [], "Tiles":[], "Carpet Installer": [], "Cement & Concrete Finisher": [], "Fencer/Fence Erector": [], "Flooring Installer":[], "HVAC":[], "Insulation": [], "Laborer": [], "Landscaper":[], "Mason":[]}


class Company:
    ##Constructor for Company User form
    ##Will contain all important information about the Company
    ##All companies will be stored in a dictionary outlining there skills (what trades they speicalize in)
    def __init__(self, name, skills, phoneNumber, emailAddress, companyInfo):
        self.name = name

        ##Update our dictionay of Companies associated with particular skills
        ##Go through the skill(s) the company provided us with and add this Company to each skill they speicliaze within our dictionary
        ##This will be used to reference specific companies when receiving Customer renovation requests
        self.skills = skills
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

    ##Getter method
    ##Returns skills about the Company associated with this object
    def getSkills(self):
        return self.skills

    ##Setter method
    ##Changes the skills of the Company associated with this object with the one passed through param
    def setSkills(self, newSkills):
        self.skills = newSkills

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

