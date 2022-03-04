from visit import Visit
from student import Student
from datetime import datetime
from popday import Day
import sys
import csv

class Day:
    def __init__(self,visit):
        self.normSlots = {
                "9:00 AM":  0,
                "10:00 AM": 0,
                "11:00 AM": 0,
                "12:00 PM": 0,
                "1:00 PM":  0,
                "2:00 PM":  0,
                "3:00 PM":  0,
                "4:00 PM":  0,
                "5:00 PM":  0,
                "6:00 PM":  0,
                "7:00 PM":  0,
                "8:00 PM":  0
                }

        self.milSlots = {
                900  : False,
                1000 : False,
                1100 : False,
                1200 : False,
                1300 : False,
                1400 : False,
                1500 : False,
                1600 : False,
                1700 : False,
                1800 : False,
                1900 : False,
                2000 : False
                }
        
        for k,v in self.milSlots.items():
            tin = int((visit.milTimeIn/100)%100)
            tout = int((visit.milTimeOut/100)%100)
            key = int((k/100)%100)

            if key >= tin and key <= tout:
                self.milSlots[k] = True


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

    #FIXME put this with the other func
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

    def PrintClasses(self):
        sett = set()
        for v in self.visits:
            sett.add(v.subject)

        classes = {}
        for s in sett:
            res = s.partition("-")[0]
            # Make our new pair in the dictionary if we don't exist
            if classes.get(res) == None:
                pair = {res : []}
                classes.update(pair)

            classes[res].append(s)

        for v in classes.values():
            v.sort()


        for k,v in classes.items():
            print(f"[{k}]")
            for x in v:
                sys.stdout.write(f"{x} ")
            print()
        return

    def PrintPopTimes(self, day):
        timeSlots =[ 
                {"9:00 AM":  0.0},
                {"10:00 AM": 0.0},
                {"11:00 AM": 0.0},
                {"12:00 PM": 0.0},
                {"1:00 PM":  0.0},
                {"2:00 PM":  0.0},
                {"3:00 PM":  0.0},
                {"4:00 PM":  0.0},
                {"5:00 PM":  0.0},
                {"6:00 PM":  0.0},
                {"7:00 PM":  0.0},
                {"8:00 PM":  0.0}
                ]

        weeks = set()
        for v in self.visits:
            if v.day == day:
                weeks.add(v.date)
                temp = Day(v)
                index = 0
                for val in temp.milSlots.values():
                    if val:
                        keylst = list(timeSlots[index].keys())
                        timeSlots[index][keylst[0]] += 1

                    index += 1

        index = 0

        for slot in timeSlots:
            keylst = list(slot.keys())
            timeSlots[index][keylst[0]] /= len(weeks)
            index += 1


        print(f"Popular Times for {day}")
        for dic in timeSlots:
            for x,y in dic.items():
                print(f"{x} {int(round(y,0))} students")
