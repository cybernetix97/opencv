import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#BGR to HSV values conversion is done in this line
    #now we define 2 values anything that comes under these two values will be displayed

    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])

    mask = cv2.inRange(hsv,low_red,high_red)

    result = cv2.bitwise_and(frame, frame, mask =mask)#display frame when frame and mask=mask are true

    cv2.imshow('frame',result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.exitallwindows()