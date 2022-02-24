class Visit:
    def __init__(self):
        self.date = "date"
        self.day = "monday"
        self.timeIn = "timeIn"
        self.milTimeIn = 1400
        self.timeOut = "timeOut"
        self.milTimeOut = 1500
        self.hoursVisited = 0.0
        self.reason = "reason"
        self.subject = "subject"
        self.classNumber = 12345

    def __str__(self):
        return f"{self.date} {self.timeIn} {self.timeOut} {self.hoursVisited} {self.reason} {self.subject} {self.classNumber}"

