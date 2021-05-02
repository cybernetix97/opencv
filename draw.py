import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0) , (width,height), (255,0,0),10 )#starting and ending co ordinates note: top left is (0,0) unlinke normal cartesian plane where bottom left is (0,0) #then color and pixel density\
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10)
    img = cv2.rectangle(img ,(0,0),(width,height),(0,0,255),10 )#source image , top left bottom right, color , pixel
    img = cv2.circle(img,(width//2,height//2),100,(128,128,128),10)#put the cursor in bw the blank arguements to know what to perform there

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'NAGZ WAS HERE', (200,250),font , 1, (0,0,0), 5, cv2.LINE_AA)#poition here should be bottom left hand cornor #cv2.line_aa helps in rendering it makes the text look better

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):  # if ascii value of waitkey is equal to ascii value of q it breaks
        break

cap.release()  # we are using the camera so we have to release it so other resources can use the camera
cv2.destroyAllWindows()  # explained in new
