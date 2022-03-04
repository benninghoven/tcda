from sauce import Sauce 
from gen import GenJSON

def Main():

    db = Sauce() 
    file = "chungus.html"
    with open(file, 'r') as f:
        temp = GenJSON(f)

    db.Gen(temp)

    # DONE
    #db.PrintAll()
    #db.GenCSV()
    #db.PrintStudents()
    #db.PrintEmbedStudents()
    #db.PrintVisits()
    #db.PRE()
    #db.PrintClasses()

    # FIXME
    dayNames= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Sunday']
    for day in dayNames:
        db.PrintPopTimes(day)


if __name__ == "__main__":
    Main()
