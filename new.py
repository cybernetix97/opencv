import cv2 #importing the package, i downloaded the module in the pycharm terminal which is below

img = cv2.imread('logo.jpeg', 0) #imread is the function to load image it's first arguement is used for defining the path and the second arguement is used to define the mode -1 is transparecy,0 is gre scale 1 is as it is
#resizing

#img = cv2.resize(img, (400,400))#dimesions
img = cv2.resize(img, (0,0),fx=0.5,fy=0.5) #ratio defining

#rotating

img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
#try other options in the field of ROTATE......

#writing an image i.e saving

cv2.imwrite('new_img.jpg', img)


cv2.imshow('IMAGE', img)#IMAGE is the name of the application and img is tha variable that we declared
cv2.waitKey(0) #waits for infinite time for a key to be pressed which is used to exit from the application
cv2.destroyAllWindows() #all windows are closed
