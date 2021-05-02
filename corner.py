import numpy as np
import cv2

img = cv2.imread('bedroom.jpg')



#img = cv2.resize(img, (0,0), fx=0.5,fy=0.5 )
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.0001, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 5, (0,0,255), -1 )



cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()