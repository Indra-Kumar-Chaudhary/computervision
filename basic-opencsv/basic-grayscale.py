import numpy as np 
import cv2 

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    # change into gray scale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame1',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('frame3',frame)
    cv2.imshow('frame4',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break