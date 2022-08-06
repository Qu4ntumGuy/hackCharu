from ast import While
import json
from tkinter import E
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#Detect one hand from Img 
detector = HandDetector(detectionCon=0.7, maxHands=1)
result = -1


def get_hand_position():
    while True:
      #    print("get_hand_position")

       _, img = cap.read()
       img = cv2.flip(img, 1)

       #Save values of diff hand data in hands obj..
       hands, img = detector.findHands(img, flipType=False)


       # Showing Video (only for temp)
       # Will comment in future and resize it in diif size and put it at bottom-right corner.
       cv2.imshow("Image", img)
       key = cv2.waitKey(1)

       hands, img = detector.findHands(img)
       if hands:
           hand = hands[0]
           fingers = detector.fingersUp(hand)

           if fingers == [1,1,1,1,1]:
            
               result = 0
               # return 0

           if fingers == [0,0,0,0,0]:
               
               result = 1
               # return 1

           if fingers == [1,1,0,0,0]:

               result = 2
               # return 2
