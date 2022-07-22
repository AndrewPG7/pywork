import notify2
from notify_content import Notify_content
from datetime import datetime
from time import sleep

friday = False
if datetime.now().weekday() == 4:
    friday = True

def launch_notification(content):
    #hour
    notify2.init(content.title_message())
    #time left, message
    n = notify2.Notification(content.time_left_message(), content.body_message())
    n.show()

def task():
    now = datetime.now()
    notify = Notify_content(now, friday)
    end = False
    if notify.hour_left == 0:
        end = True;
    launch_notification(notify)
    return end

task()

while datetime.now().minute != 0:
    sleep(60)


while 1:
    if task():
        break
    sleep(60*60)

print("See you next time")
