import datetime
import pygame
import time
import os
import math
from datetime import datetime
from time import sleep

pygame.mixer.init()

audio_volume = 0.5
audio_interval = 1

sound = pygame.mixer.Sound('alarmaudiostart.wav')
print('{0}'.format(sound.get_volume()))
sound.set_volume(audio_volume)


ah = input("What hour would you like to wake up at?(24 hour time): ")

ahour = ah

if ahour == "creator" or int(ahour) > 23:
    print("Program created by Bugman5352 on 6/4/16")

am = input ("What minute would you like to wake up at?: ")
aminute = am

pmh = 12

str(pmh)

if int(ahour) >= int(pmh):
    ap = "PM"
else:
    ap = "AM"

str(aminute)

atime = "You want to wake up at %s:%s %s" % (ahour, aminute, ap)

atimeo = "%s:%s %s" % (ahour, aminute, ap)

print(atime)

timesran = 0

amounttimesran = 0

def counttimesran():
    global timesran
    timesran = timesran + 1

while True:
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour
    str(minute)
    
    if hour >= 12:
        pa = "PM"
    else:
        pa = "AM"
        
    y = "The time is:%s:%s:%s %s" % (hour, minute, second, pa)
    x = "%s:%s %s" % (hour, minute, pa)

    if (atimeo == x):
        print("WAKE UP")
        while (timesran <= 3):
            sound = pygame.mixer.Sound('alarmaudiostart.wav')
            sound.set_volume(audio_volume)
            sound.play()
            time.sleep(3)
            counttimesran()
                
    if (timesran >= 3):
        print("good")
        break
print("End")