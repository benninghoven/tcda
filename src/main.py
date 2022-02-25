from sauce import Sauce 
from gen import GenJSON

def Main():

    db = Sauce() 
    with open("fatboy.html", 'r') as f:
        dog = GenJSON(f)
    db.Gen(dog)

    # DONE
    #db.PrintAll()
    #db.PrintVisits()
    db.PrintStudents()

    # FIXME
    #db.PopTimes("monday")


if __name__ == "__main__":
    Main()
