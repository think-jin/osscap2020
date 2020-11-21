import datetime
import pygame
import time
import os
import math
from datetime import datetime
from time import sleep

pygame.mixer.init()

audio_volume = 0.5 #default audio volume
sound = pygame.mixer.Sound('alarm.wav')


MusicList = { 
            1: ('Alarm signal', 'alarm.wav'), 
            2: ('Campfire', 'fire.wav'),
            3: ('Boiling water', 'boiling.wav')
}

def SelectMusic():
    global sound
    while True: 
        print("1. Alarm signal\n2. Campfire\n3. Boiling water")
        choice = int(input("Select the alarm sound(1~3): "))
        if 1 <= choice <= 3:
            sound = pygame.mixer.Sound(MusicList[choice][1])
            print("You have set '{}' to the alarm sound.".format(MusicList[choice][0]))
            break
        else:
            print("Out of input range. Please re-enter.")

def SelectVolume():
    global sound
    while True:
        audio_volume = float(input("Please enter the size of the alarm(0~1 float): "))
        if 0 <= audio_volume <=1:
            sound.set_volume(audio_volume)
            print("Audio volume: %.2f" % (sound.get_volume()))
            break
        else:
            print("Out of input range. Please re-enter.")

def SelectAlarmTime():
    while True:
        ahour = int(input("HOUR (24 hour time): "))
        if (ahour > 23 or ahour < 0):
            print("Please  re-enter.")
            continue
        break

    while True:
        aminute = int(input ("MINUTE : "))
        if (aminute > 60 or aminute < 0):
            print("Please re-enter.")
            continue
        break

    pmh = 12

    if ahour >= pmh:
        ap = "PM"
    else:
        ap = "AM"

    if ahour < 10:
        ahour = "0" + str(ahour)
    if aminute < 10:
        aminute = "0" + str(aminute)

    atime = "%s:%s %s" % (ahour, aminute, ap)
    print("Alarm at {}".format(atime))
    return atime

def Alarm(alarm_time):

    while True:
        now = datetime.now()
        second = now.second
        minute = now.minute
        hour = now.hour
        
        if hour >= 12:
            pa = "PM"
        else:
            pa = "AM"
            
        real_time = "%s:%s %s" % (hour, minute, pa)

        if (alarm_time == real_time and second == 0):
            print("WAKE UP")
            while True:
                sound.play()
                time.sleep(4)

#실행 부분
while True:
    print("1.Set alarm\t2.Set alarm tone\t3.Set alarm size\t4. Exit")
    choice = int(input("Please enter your number.(1~4): "))
    if choice == 1:
        alarm_time = SelectAlarmTime()
        Alarm(alarm_time)
    elif choice == 2:
        SelectMusic()
    elif choice == 3:
        SelectVolume()
    elif choice == 4:
        print("Exit Smart Alarm")
        break
    else:
        print("Out of input range. Please re-enter.")