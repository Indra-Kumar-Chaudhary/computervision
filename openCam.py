import cv2 

# open camera with opencv for only one frame 

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Granny Cam', frame) 

