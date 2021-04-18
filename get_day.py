import calendar
import datetime
import time


def return_day():
    Date = str(datetime.date.today())
    Date = Date.replace('-', ',')
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    year, month, day = Date.split(',')

    no_of_day_in_week = calendar.weekday(int(year), int(month), int(day))

    return days[no_of_day_in_week - 1]


def return_time():
    return time.strftime("%H")
