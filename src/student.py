"""
class BankAccount():

    def __init__(self, **kwargs ):
        if kwargs is not None:
            if 'name' in kwargs:
                self.name = kwargs['name']
            else:
               raise ValueException('Name cannot be empty') 

            if 'balance' in kwargs:
                self.balance = kwargs['balance']
            else:
                self.balance = 0
"""

class Student:
    def __init__(self):  
        self.name = "student name" 
        self.ID = 1234567       # ID number, only unique info
        self.totalVisits = 0    # total number of visits, basically len(visits)
        self.hours = 1.0        # total hours spent at the TC
        self.visits = []        # holds our visit objects


    def __str__(self): # printing student
        return f"[{self.ID}] [{self.name}]"

    def AddVisit(self, visit): #FIXME add a better type checking # duck type checking
        self.visits.append(visit)

    def GetName(self):
        return self.name

    def SetName(self, newName):
        self.name = newName
        return

    def GetID(self):
        return self.ID

