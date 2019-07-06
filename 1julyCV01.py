#!/usr/bin/python

import cv2

# Starting Camera
cap= cv2.VideoCapture(0)
# adding plugin
plugin = cv2.VideWriter_fourcc(*'XVID')
# saving video                              --width,height--
output = cv2.VideoWriter('class.avi',plugin,20,(640,480))

while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    # draw pattern 
    output.write(frame)
    if cv2.waitKey(10)  &  oxff == ord('q'):
        break
cv2.destroyAllWindows()  # this will destroy all window 
cap.release()