from visit import Visit
from student import Student
from datetime import datetime
from popday import Day

class Sauce:

    def __init__(self):
        self.lst = [] # holds everything
        self.visits = [] 


    # FIXME: grab json file from WINDOWS/MAC Directory
    # FIXME: add a "generated in {seconds}s"
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

    def GetVisits(self):
        return self.visits

    def PrintVisits(self):
        for x in self.visits:
            print(x)

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

        #sortedDic = sorted(dic, key=lambda s: dic.get(s), reverse=True)


            
        
        




