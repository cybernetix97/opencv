import cv2
import numpy as np  # arrays

cap = cv2.VideoCapture(0)  # 0 because it has to access one camera
# replace 0 with name of the video which should be in the same folder within ''

while True:
    ret, frame = cap.read()  # return a frame from the capturing video

    width = cap.shape[0]  # cap.get6 gives the width property of the frame
    height = cap.shape[1]  # using int cause by default they are float

    image = np.zeros(frame.shape, np.uint8)  # array of images all 0 by default i.e. displayed in black


    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5,fy=0.5)
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height // 2:, :width // 2] = smaller_frame
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height // 2:, width // 2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):  # if ascii value of waitkey is equal to ascii value of q it breaks
        break

cap.release()  # we are using the camera so we have to release it so other resources can use the camera
cv2.destroyAllWindows()  # explained in new


