from visit import Visit
from student import Student

class Sauce:
    def __init__(self):
        self.lst = []

    # FIXME: grab json file from WINDOWS/MAC Directory
    # FIXME: add a "generated in {seconds}s"
    def Gen(self,jsonFile):
        self.lst = jsonFile

    def Print(self):
        for student in self.lst:
            print(student)
            for visit in student.visits:
                print(visit)




