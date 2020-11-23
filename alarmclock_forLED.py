import datetime
import pygame
import time
import os
import math
from datetime import datetime
from time import sleep
from matrix import *
import LED_display as LMD
import threading

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                LMD.set_pixel(y, x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, x, 4)
            else:
                continue
        print()

iScreenDy = 16
iScreenDx = 32

arrayScreen = [[0 for col in range(32)] for row in range(16)]

arrayNumDict = { 1: [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]], 
                 2: [[0, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0], [1, 1, 1]], 
                 3: [[1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0]], 
                 4: [[1, 0, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 5: [[0, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 0]], 
                 6: [[0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0]], 
                 7: [[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 0, 1], [0, 0, 1]], 
                 8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]], 
                 9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
                 ':': [[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0]] } 

arrayAlphabetDict = {'A': [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'B': [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]],
                     'C': [[0, 1, 0], [1, 0, 1], [1, 0, 0], [1, 0, 1], [0, 1, 0]],
                     'D': [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
                     'E': [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
                     'F': [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 0], [1, 0, 0]],
                     'G': [[0, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 0]],
                     'H': [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'I': [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
                     'J': [[1, 1, 1], [0, 1, 0], [0, 1, 0], [1, 0, 1], [0, 1, 0]],
                     'K' : [[1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1]],
                     'L' : [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0 ,0], [1, 1, 1]],
                     'M' : [[1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]],
                     'N' : [[1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'O' : [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
                     'P' : [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
                     'Q' : [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]],
                     'R' : [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]],
                     'S' : [[1, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 1]],
                     'T' : [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
                     'U' : [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
                     'V' : [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
                     'W' : [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]],
                     'X' : [[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]],
                     'Y' : [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
                     'Z' : [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]}


LED_init()
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)

###
### prepare the initial screen output
###  
count = 0
top = 0
left = 5

for i in ['A', 'L', 'A', 'R', 'M', 'M', 'U', 'S', 'I', 'C', 'V', 'O', 'L', 'U', 'M', 'E']:
    arrayBlk = arrayAlphabetDict[i]
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)
    left += 4
    count+=1
    if count==5:
        top = 5
        left = 6
    if count==10:
        top = 11
        left = 2

top = 5
left = 25
for i in range(2):
    arrayBlk = arrayNumDict[':']
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)

draw_matrix(oScreen); print()

###
### make function used for alarm
###
pygame.mixer.init()
audio_volume = 0.5 #default audio volume
sound = pygame.mixer.Sound('alarm.wav')

UserList = ("None", "Jihwan", "Jiho", "Myungjin")
MusicList = { 
            1: ('Alarm signal', 'alarm.wav'), 
            2: ('Campfire', 'fire.wav'),
            3: ('Boiling water', 'boiling.wav')
}

def SelectSound():
    global sound
    while True: 
        print("1. Alarm signal\n2. Campfire\n3. Boiling water")
        choice = int(input("Select the alarm sound(1~3): "))
        if 1 <= choice <= 3:
            sound = pygame.mixer.Sound(MusicList[choice][1])
            print("You have set '{}' to the alarm sound.".format(MusicList[choice][0]))
            top = 5
            left = 27
            arrayBlk = arrayNumDict[choice]
            currBlk = Matrix(arrayBlk)
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            oScreen.paste(tempBlk, top, left)
            draw_matrix(oScreen); print()
            break
        else:
            print("Out of input range. Please re-enter.")

def SelectVolume():
    global sound
    while True:
        audio_volume = int(input("Please enter the size of the alarm(0~10 int): "))
        if 0 <= audio_volume <=10:
            print("Audio volume: %d" %(audio_volume))
            sound.set_volume(audio_volume / 10.0)
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
        SelectSound()
    elif choice == 3:
        SelectVolume()
    elif choice == 4:
        print("Exit Smart Alarm")
        break
    else:
        print("Out of input range. Please re-enter.")