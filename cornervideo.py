import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) 

    if corners is not None:
        corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
#lines
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            color = tuple(map(lambda x: int(x), np.random.randint(0, 255 , size=3)))
            cv2.line(frame ,corner1 ,corner2, color, 1)

    cv2.imshow('mask', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.waitKey(0)
cv2.exitallwindows()
