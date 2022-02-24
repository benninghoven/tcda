from sauce import Sauce 
from gen import GenJSON

def Main():
    db = Sauce()
    with open("2-days.html", 'r') as f:
        dog = GenJSON(f)
    db.Gen(dog)
    db.Print()


if __name__ == "__main__":
    Main()
