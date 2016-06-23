import csv
import time
import datetime

#Note: date must be in the format of month/day/year
def compareDates(threeMonths, lastLogIn):
    if(lastLogIn <= threeMonths):
        return True
    else:
        return False

def validateDate(date):
    tmpDate = date
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

def getDateFromFile(file):
    #get date from user
    dateToCompare = input("Please enter the date from three months ago zero buffered: ")

    #open and read data from .csv file
    fd = open(file)
    data = csv.reader(fd)
    mailList = []
    checkDateFormat(dateToCompare)
    validateDate(dateToCompare)

    for row in data:
        print(row[2])
        lastLogIn = time.strftime(row[2], "%m/%e/%Y")
        checkDateFormat((lastLogIn))
        validateDate(dateToCompare)

        if(compareDates(dateToCompare, lastLogIn)):
            mailList.append(str(row[1]))

    for i in mailList:
        print(i)

getDateFromFile("test.csv")