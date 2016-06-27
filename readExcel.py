import csv
import time
import datetime
import sys

lasLogIn = ''
dateToCompare = ''

def validateDate(date):
    tmpDate = date
    if(tmpDate[1] == "/"):
        tmpDate = "0" + tmpDate
    if(tmpDate[5] != "/"):
        tmpDate = tmpDate[:3] + "0" + tmpDate[3:9]
    month = int(tmpDate[:2])
    day = int(tmpDate[3:5])
    year = int(tmpDate[6:10])
    try:
        datetime.datetime(month = month, day = day, year = year)
    except ValueError:
        raise ValueError("Month, day, or year incorrect, Please re-enter date")

#validate the format of the date is month/day/year
def checkDateFormat(date):
    tmpDate = date
    try:
        datetime.datetime.strptime(tmpDate, "%m/%d/%Y")
    except ValueError:
        raise ValueError("Incorrect data format, should be MM/DD/YYYY.")

'''after being fed a file, read the data and create a mail list based on people's last
   log in date if 3 month or longer from the current date.'''
def getDateFromFile(file):
    #get date from user
    dateToCompare = input("Please enter the date from three months ago zero buffered: ")
    mailFile = input("Please give a file name for the mail list that will be created: ")
    #open and read data from .csv file
    fd = open(file)
    data = csv.reader(fd)
    mailList = []
    #checkDateFormat(dateToCompare)
    validateDate(dateToCompare)

    #iterate through the rows of data comparing dates
    """criteria to add to mail list are that the date of last log in
       must be 3 months or more ago from the current date"""
    for row in data:
        lastLogIn = row[2]
        validateDate(lastLogIn)
        #checkDateFormat((lastLogIn))
        #lastLogIn = time.strftime(row[2], "%m/%d/%Y")
        logInDate = lastLogIn.split("/")
        threeMonths = dateToCompare.split("/")
        if(int(logInDate[2]) >= int(threeMonths[2])):
            if((int(threeMonths[0])) > int(logInDate[0])):
                mailList.append(row[1] + ", " + row[2])
            elif((int(threeMonths[0])) == int(logInDate[0])):
                if(int(threeMonths[1]) >= int(logInDate[1])):
                    mailList.append(row[1] + ", " + row[2])
        else:
            mailList.append(row[1] + ", " + row[2])
    fd.close()
    fd = open(mailFile, "w")
    sys.stdout = fd
    for item in mailList:
        print(item)
    fd.close()

def read_excel():
    file = input("Please enter an existing filename to read from: ")
    getDateFromFile(file)

read_excel()