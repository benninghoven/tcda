import datetime 

def WhatDay(date):
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return day_name[day]
