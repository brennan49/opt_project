import urllib
import requests
import smtplib

user = '' #To log onto SwiftKanban, for use with API calls
passwrd = ''

url = 'https://login.swiftkanban.com/axis2/services/KanbanCardService?wsdl'

#likely not necessary
def _getUrl(path):
     return 'https://SwiftKanban.org' + path

#request access to SwiftKanban
def requestAccess(url):
    kanbanApi = requests.urlopen('https://login.swiftkanban.com/axis2/services/KanbanCardService?wsdl', auth=('user', 'pass'))


"""call necessary API (getAllActiveUsersInOrg?) to get user data followed by getting
    the users information (getUserData?).  will place this information in a list."""
def getUserInfo(userName):
 {}

"""send out an e-mail on an scheduled loop.
    still not sure if I want to implement creating two bins
    for people that respond yes and those that respond no to the
    e-mail or do that in another function."""
def automatedEmail(userName, users):
 {}