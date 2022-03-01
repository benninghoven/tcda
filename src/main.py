from sauce import Sauce 
from gen import GenJSON

def Main():

    db = Sauce() 
    file = "goodreport.html"
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
    db.PrintClasses()

    # FIXME
    #db.PopTimes("monday")


if __name__ == "__main__":
    Main()
