class Visit:
    def __init__(self):
        self.date = "date"
        self.day = "monday"
        self.ownerID = 1231231
        self.timeIn = "timeIn"
        self.milTimeIn = 1400
        self.timeOut = "timeOut"
        self.milTimeOut = 1500
        self.hoursVisited = 0.0
        self.reason = "reason"
        self.subject = "subject"
        self.classNumber = 12345
        self.isEmbed = False


    def GetList(self):
        lst = [self.date, self.day, self.ownerID, self.timeIn, 
                    self.milTimeIn, self.timeOut, self.milTimeOut, 
                    self.hoursVisited,self.reason,self.subject, 
                    self.classNumber, self.isEmbed]
        return lst

    def __str__(self):
        return f"{self.date} {self.day} {self.ownerID} {self.timeIn} {self.milTimeIn} {self.timeOut} {self.milTimeOut} {self.hoursVisited} {self.reason} {self.subject} {self.classNumber} {self.isEmbed}"

    def AddClassNumber(self, no):
        self.classNumber = int(no)

    def MilTime(self, s):
        end = s[-2:]
        newS = ""
        for c in s:
            if c.isdigit():
                newS += c
        digits = int(newS)
        if end == "PM" and digits < 1200:
            digits += 1200
        return digits

    def SetMilTime(self, s , st):
        if st == "i":
            self.milTimeIn = self.MilTime(s)
        elif st == "o":
            self.milTimeOut = self.MilTime(s)
