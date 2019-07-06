# Motion Detector 
import cv2

# starting camera
cap=cv2.VideoCapture(0)

tp1=cap.read()[1] # Take 1
tp2=cap.read()[1] # Take 2
tp3=cap.read()[1] # Take 3

# to make more  perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY) # Converting into gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

# now creating image difference 
def image_diff(x,y,z):
    # Difference between x,y--gray1,gray2 --d1
    d1=cv2.absdiff(x,y)
    # Difference between y,z--gray2,gray3 --d2
    d2=cv2.absdiff(y,z)
    # Absolute difference between d1-d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg

# now apply function 
while cap.isOpened():
    status,frame=cap.read()
    motionimg=image_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    # cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)  # motion detect
    if cv2.waitKey(10)  & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
