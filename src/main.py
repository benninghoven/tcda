from sauce import Sauce 
from gen import GenJSON

def Main():

    db = Sauce() 
    file = "goodreport.html"
    with open(file, 'r') as f:
        dog = GenJSON(f)

    db.Gen(dog)

    # DONE
    #db.PrintAll()
    db.GenCSV()
    #db.PrintStudents()
    #db.PrintEmbedStudents()
    #db.PrintVisits()
    #db.PRE()

    # FIXME
    #db.PopTimes("monday")


if __name__ == "__main__":
    Main()
