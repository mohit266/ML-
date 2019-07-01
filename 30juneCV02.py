#!/usr/bin/python

import cv2

# Starting Camera
cap= cv2.VideoCapture(0)
#                    First Camera
# to check camera is started or not
if cap.isOpened():
    print("Camera is ready to take picture")
else:
    print("Check your web cam drivers")    

# now we can take read input from cammera
#print(cap.read()) # it will take first picture
status,img=cap.read()

# now showing
cv2.imshow('liveimage',img)
cv2.waitKey(0)

# to close camera
cap.release()