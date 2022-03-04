from visit import Visit
from student import Student

class Day:
    def __init__(self,day,visits):
        self.day = day
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


