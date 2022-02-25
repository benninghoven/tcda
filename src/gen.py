from bs4 import BeautifulSoup
from checkdate import CheckDate
import json
import shlex
import time

from student import Student
from visit import Visit
from whatday import WhatDay

def Err(errMsg):
    print("error")
    print(errMsg)
    exit()

# FIXMEL generate the json in both WINDOWS and MAC
def GenJSON(file): # given an HTML file
    print("generating started")
    starttime = time.time()
    lasttime = starttime

    parser = "lxml"
    soup = BeautifulSoup(file, parser)
    try:
        table = soup.find("table", class_ = "reportListing")
    except:
        Err("unable to locate table")

    lst = []
    rows = []
    rows = table.find_all("tr")

    for row in rows:
        tds = row.find_all("td")
        temp = []
        for td in tds:
            if td.text != "": # remove empty elements
                temp.append(td.text)
        lst.append(temp)    

    if len(lst) < 3:
        Err("table size is too small") 

    # check if report was generated correctly
    title = "title"
    title = lst[0]
    if title != ['Cohort']:
        Err("wrong report style used")
    lst.pop(0) # remove top element
    title = lst[0]
    if title != ['ID', 'Visits', 'Hours', 'Date', 'Time In', 'Time Out', 'Tot Hrs', 'Reason', 'SectionTerm No']:
        Err("wrong report style used")
    lst.pop(0)
    lst.pop(-1) # remove final element
    
    stuDB = [] # all student objects stored here
    inx = -1
    for row in lst:
        if not CheckDate(row[0]): # create student if 0th element is not a date
            if len(row) < 4:
                continue
            temp = Student()
            temp.name = row[0]
            temp.ID = row[1]
            temp.totalVisits = row[2]
            temp.hours = row[3]
            stuDB.append(temp)
            inx += 1

        else: # create visit
            if len(row) < 6:
                continue
            temp = Visit()
            temp.date = row[0]
            temp.day =  WhatDay(temp.date)
            temp.ownerID = stuDB[inx].ID
            temp.timeIn = row[1]
            temp.SetMilTime(temp.timeIn,'i')
            temp.timeOut = row[2]
            temp.SetMilTime(temp.timeOut,'o')
            temp.hoursVisited = row[3]
            temp.reason = row[4]
            secTermNo = shlex.split(row[5])

            if len(secTermNo) > 1:
                temp.subject = secTermNo[0]
                temp.AddClassNumber(secTermNo[1])

            stuDB[inx].AddVisit(temp)
    sec = round((time.time() - lasttime), 2)
    print(f"generated in {sec} seconds")
    return stuDB
"""
    with open(newFilePath, 'w') as newFile: # generate new json file
        data = {}
        for stu in stuDB:
            #print(stu)
            visits = []
            for visit in stu.visits: # might be multiple visits
                temp = {
                    "date": visit.date,
                    "timeIn": visit.timeIn,
                    "timeOut": visit.timeOut,
                    "hoursVisited": visit.hoursVisited,
                    "reason": visit.reason,
                    "subject": visit.subject
                }
                visits.append(temp)
            data[stu.ID] = {
                    "name": stu.name,
                    "id": stu.ID,
                    "totalVisits": stu.totalVisits,
                    "visits": visits
                    }
        json.dump(data,newFile, indent=5)
    print(f"new .json successfully generated in\n{newFilePath}\n🦑")
    """
