import random

class Notify_content:

    global messages
    messages = ["Keep it up buddy", "Keep on keepin' on", "Don´t look too much at the clock", "Have a break, you dereve it", "It might seem a lot, but you can do it", "You've been doing your chores, right?"]

    global final_message
    final_message = "Time to go!"

    def __init__(self, time, friday):
        self.hour = time.hour
        if friday:
            self.hour_left = 15 - time.hour
        else:
            self.hour_left = 16 - time.hour
        self.friday = friday

    def title_message(self):
        return "It's " + str(self.hour) + " o'clock"

    def time_left_message(self):
        if self.hour_left == 1:
            return str(self.hour_left) + " hour left until end of shift"
        else:
            return str(self.hour_left) + " hours left until end of shift"

    def body_message(self):
        if self.friday:
            if self.hour == 8:
                return "It's friday, last push of the week!"
            elif self.hour_left == 0:
                return "Oficially weekend!"
            else:
                return random.choice(messages)
        else:
            if self.hour_left == 0:
                return final_message
            else:
                return random.choice(messages)
