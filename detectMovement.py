# compare two frame and detect the movement 
import cv2 
from pydub import AudioSegment 
from pydub.playback import play 

sound = AudioSegment.from_wav('alert.wav')

cam = cv2.VideoCapture(0) 
while cam.isOpened():
    ret, frame1 = cam.read() 
    ret, frame2 = cam.read() 
    # check absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)
    # convert colar to gray color 
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    # blue 
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    # some threhold to blue 
    _, thresh = cv2. threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    # specifying the contours (boundary of the object)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # drop the contours 
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    # detecting specific things 
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)
        play(sound)
    if cv2.waitKey(10)== ord('q'):
        break 
    cv2.imshow('Indra Cam', frame1)