import csv
import time
import datetime

dateToCompare = "3/23/2016"

#Note: date must be in the format of month/day/year
def compareDates(threeMonths, lastLogIn):
    if(lastLogIn <= threeMonths):
        return True
    else:
        return False

#validate the format of the date is month/day/year
def checkDateFormat(date):
    try:
        datetime.datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        raise ValueError("Incorrect data format, should be MM/DD/YYYY.")

def getDateFromFile(file):
    fd = open(file)
    data = csv.reader(fd)
    mailList = []
    checkDateFormat(dateToCompare)

    for row in data:
        lastLogIn = time.strftime(row[2], "%m/%d/%Y")
        checkDateFormat((lastLogIn))
        if(compareDates(dateToCompare, lastLogIn)):
            mailList.append(row[1])

