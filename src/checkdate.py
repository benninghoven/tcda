from dateutil.parser import parse
# taken from stack overflow link below
# https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
def CheckDate(string, fuzzy=False):
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

