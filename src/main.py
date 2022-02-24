from src.gen import *

from src.classes.student import Student
from src.classes.visit import Visit
from src.sauce import Sauce

def Main():
    db = []
    with open ("2-days.html", 'r') as f:
        db = GenDB(f)

    sauce = Sauce()
    sauce.Gen("bobby")




if __name__ == "__main__":
    Main()
