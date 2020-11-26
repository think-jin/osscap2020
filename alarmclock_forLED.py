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
import cv2
from recognition import face_recognition

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
                LMD.set_pixel(y, x, 6)
            else:
                continue
        print()

###
### initialize variables
###     
iScreenDy = 16
iScreenDx = 32

arrayScreen = [[0 for col in range(32)] for row in range(16)]

arrayNumDict = { 1: [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]], 
                 2: [[0, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0], [1, 1, 1]], 
                 3: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]], 
                 4: [[1, 0, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 5: [[0, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 0]], 
                 6: [[0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0]], 
                 7: [[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 0, 1], [0, 0, 1]], 
                 8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]], 
                 9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]], 
                 0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
                 'Non': [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] } 

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
                     'M' : [[1, 0, 1], [1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
                     'N' : [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]],
                     'O' : [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
                     'P' : [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
                     'Q' : [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]],
                     'R' : [[1, 1, 1], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]],
                     'S' : [[0, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0]],
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

def updateScreen(arrayBlk, top, left):
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)

###
### prepare the initial screen output
###  
word_count = 0
top = 0
left = 0

for word in "TIMESOUNDVOLUME": # TIME \n SOUND \n VOLUME
    arrayBlk = arrayAlphabetDict[word]
    updateScreen(arrayBlk, top, left)
    left += 4
    word_count+=1
    if word_count==4: # word = 'S'
        top = 5
        left = 0
    if word_count==9: # word = 'V'
        top = 11
        left = 0

draw_matrix(oScreen); print()

###
### make functions, variables used for alarm
###

pygame.mixer.init()
audio_volume = 0.5 #default audio volume
sound = pygame.mixer.Sound('alarm.wav')

UserNameList = ("Jihwan", "Jiho", "Myungjin")
SoundList = { 
            1: ('Alarm signal', 'alarm.wav'), 
            2: ('Campfire', 'fire.wav'),
            3: ('Boiling water', 'boiling.wav')
}

def SelectSound():
    global sound
    while True: 
        print("1. Alarm signal\n2. Campfire\n3. Boiling water")
        audio_sound = int(input("Select the alarm sound(1~3): "))
        if 1 <= audio_sound <= 3:
            sound = pygame.mixer.Sound(SoundList[audio_sound][1])
            print("You have set '{}' to the alarm sound.".format(SoundList[audio_sound][0]))
            
        else:
            print("Out of input range. Please re-enter.")
            continue

        top = 5
        left = 27        
        arrayBlk = arrayNumDict[audio_sound]
        updateScreen(arrayBlk, top, left)
        break

def SelectVolume():
    global sound
    while True:
        audio_volume = int(input("Please enter the size of the alarm(0~10 int): "))
        if 0 <= audio_volume <=10:
            print("Audio volume: %d" %(audio_volume))
            sound.set_volume(audio_volume / 10.0)
            top = 11
            left = 25
            arrayBlk = arrayNumDict['Non']
            updateScreen(arrayBlk, top, left)
            left += 4
            if audio_volume == 10:
                left = 25
        else:
            print("Out of input range. Please re-enter.")
            continue

        for i in str(audio_volume):
            arrayBlk = arrayNumDict[int(i)]
            updateScreen(arrayBlk, top, left)
            left += 4
        break

def Alarm():
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

    if aminute < 10: #출력할때 minute < 10 -> [][]:[0][] 방식
        print_aminute = "0" + str(aminute)
        print_time = "%s:%s %s" % (ahour, print_aminute, ap)
        print("Alarm at {}".format(print_time))
    else:
        print_time = "%s:%s %s" % (ahour, aminute, ap)
        print("Alarm at {}".format(print_time))

    top = 0
    if len(str(ahour))==1:
        left = 21
        arrayBlk = arrayNumDict[ahour]
        updateScreen(arrayBlk, top, left)
    else:
        left = 17
        for num in str(ahour):
            arrayBlk = arrayNumDict[int(num)]
            updateScreen(arrayBlk, top, left)
            left += 4

    if len(str(aminute))==1:
        lst = [0, aminute]
        left = 25
        for num in lst:
            arrayBlk = arrayNumDict[num]
            updateScreen(arrayBlk, top, left)
            left += 4
    else:
        left = 25
        for num in str(aminute):
            arrayBlk = arrayNumDict[int(num)]
            updateScreen(arrayBlk, top, left)
            left += 4

    draw_matrix(oScreen); print()

    now = datetime.now()
    if now.hour > ahour:
        alarmtime = datetime(now.year, now.month, (now.day + 1), ahour, aminute, 0)
    else:
        alarmtime = datetime(now.year, now.month, now.day, ahour, aminute, 0)

    time_gap=(alarmtime-now).seconds
    time.sleep(time_gap)

    print("WAKE UP")
    '''while True:
        sound.play()
        return_name = face_recognition()
        if user_name == return_name:
            print("%s, Have a nice day" % user_name)
            break
        else:
            continue'''
###
### execute the loop
###
while True:
    user_name = input("Please input user name(1. Jihwan 2.Jiho 3.Myungjin): ")
    if user_name not in UserNameList:
        continue
    break

while True:
    print("1.Set alarm\t2.Set alarm tone\t3.Set alarm size\t4. Exit")
    choice = int(input("Please enter your number.(1~4): "))
    if choice == 1:
        Alarm()
    elif choice == 2:
        SelectSound()
    elif choice == 3:
        SelectVolume()
    elif choice == 4:
        print("Exit Smart Alarm")
        iScreen = Matrix(arrayScreen)
        oScreen = Matrix(iScreen)
        draw_matrix(oScreen); print()
        break
    else:
        print("Out of input range. Please re-enter.")
        continue

    draw_matrix(oScreen); print()

###
### end of the loop
###
