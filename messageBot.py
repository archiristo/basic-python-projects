import pywhatkit
import datetime
import time

number = "*"
sendtime = "*"
message = "Sent from Python 3.10.2"

sendtime_hour = int(sendtime.split(":")[0])
sendtime_minute = int(sendtime.split(":")[1])

sendtime = datetime.datetime.now().replace(hour=sendtime_hour, minute=sendtime_minute, second=0, microsecond=0)

if sendtime < datetime.datetime.now():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    sendtime = datetime.datetime.combine(tomorrow, datetime.time(sendtime_hour, sendtime_minute))

later = sendtime + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    if now.hour == sendtime_hour and now.minute == sendtime_minute and now.day == sendtime_.day:
        pywhatkit.sendwhatmsg(number, message, sendtime_hour, sendtime_minute + 1)
        print("Sent")