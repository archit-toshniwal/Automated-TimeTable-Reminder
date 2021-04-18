import get_day as day_finder
import requests
import time

url = "https://www.fast2sms.com/dev/bulk"
headers = {

    'authorization': "Ka3o52e6HVcrQ0ZfnFMb8gtpTmJ4CRzIP1NhGBi7ysAlkXvOUDngX2lwZvHeRL7EdNrhVMWOtb631zAc",

    'Content-Type': "application/x-www-form-urlencoded",

    'Cache-Control': "no-cache",

}

#no on which msg have to be sended
no = 9079024693

#class for setting properties
class Period:
    def __init__(self, course, duration, start_time, end_time):
        self.course = course
        self.duration = duration
        self.start_time = start_time
        self.end_time = end_time

    def show(self):
        return f"Hello Harshita Course named {self.course} will be begin at {self.start_time}:00 and you have to study for {self.duration} hours. Good Luck!"

#dictionary with key as week-days and value as objects with different time
data = {
    "saturday": [Period("Javascript", "2hrs", "15", "16"), Period("Java", "2hrs", "16", "22"),
               Period("DSA", "2hrs", "22", "0")],
    "tuesday": [Period("React", "2hrs", "14", "16"), Period("Hackerrank", "2hrs", "20", "22"),
                Period("sql", "2hrs", "22", "0")],
    "monday": [Period("React", "2hrs", "14", "16"), Period("Hackerrank", "2hrs", "20", "22"),
                Period("sql", "2hrs", "22", "0")]
}

#function that will accept weekday and time
def task(day, time):
    for x in data:
        if x == day:
            for y in data[x]:
                if y.start_time == str(time):
                    print(y.show())
                    payload = f"sender_id=FSTSMS&message={y.show()}&language=english&route=p&numbers={no}"
                    response = requests.request("POST", url, data=payload, headers=headers)


#infinite loop so it will be running all time and call method return_day(),return_time() from get_day file and pass to its own method task
while True:
    print("Entered")
    day = day_finder.return_day()
    print(day)
    times = day_finder.return_time()
    print(times)
    task(day,times)
    time.sleep(200)
