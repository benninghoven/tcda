from visit import Visit
from student import Student
from datetime import datetime
from popday import Day
import csv

class Sauce:

    def __init__(self):
        self.lst = [] # holds everything
        self.visits = [] 

    # FIXME: grab json file from WINDOWS/MAC Directory
    def Gen(self,jsonFile):
        self.lst = jsonFile
        for student in self.lst:
            for visit in student.visits:
                self.visits.append(visit)
        self.visits.sort(key = lambda date: datetime.strptime(date.date, '%m/%d/%Y'))


    def PrintAll(self):
        for student in self.lst:
            print(student)
            for visit in student.visits:
                print(visit)

    def PrintStudents(self):
        for student in self.lst:
            print(student)

    def PrintEmbedStudents(self):
        for student in self.lst:
            if student.hasEmbed:
                print(student)

    def GetVisits(self):
        return self.visits

    def PrintVisits(self):
        for x in self.visits:
            print(x)

    # generates a CSV of visits
    def GenCSV(self):
        tmp = self.visits
        header = ["date", "day", "ownerID", "timeIn", "milTimeIn", "timeOut", "milTimeOut", "hoursVisited", "reason", "subject", "classNumber","isEmbed"]
        with open('visits.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(header)
            for v in tmp:
                filewriter.writerow(v.GetList())


    def PopTimes(self, day): # we care about UNIQUE heads, and what time they're there
        day = day[:1].upper() + day[1:].lower()
        dayNames= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        if day not in dayNames:
            print(f"error {day} is not a valid day!")
            return
        d = Day(day)
        for x in self.visits:
            if x.day == day:
                d.AddVisit(x)

            d.Print()

    def PRE(self):  # print ratio embedded
        huge = len(self.lst)
        embedded = 0.0
        for s in self.lst:
            if s.hasEmbed:
                embedded += 1
        percentEmb = (embedded/huge) * 100
        percentEmb = round(percentEmb, 2)
        print(f"{int(embedded)} embedded students\n{huge} total students\n{percentEmb}% embedded")





            
        
        




