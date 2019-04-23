#! Python
# This is a program that plays a alarm

import time
from playsound import playsound

# Write a number in minutes to play the alarm
alarm_count = int(input('Write a number in minutes to play the alarm'))
alarm_seconds = alarm_count * 60
time.sleep(alarm_seconds)

# Open the alarm file when the time goes out
your_file = input('Write the path where your file is')
playsound(your_file)
