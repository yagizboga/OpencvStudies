import cv2 as cv
import numpy as np

img = cv.imread('seapic.jpg')

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.namedWindow('seapic')
cv.createTrackbar('H','seapic',0,180,lambda x:None)
cv.createTrackbar('S','seapic',0,255,lambda x:None)
cv.createTrackbar('V','seapic',0,255,lambda x:None)

while(1):
    h = cv.getTrackbarPos('H','seapic')
    s = cv.getTrackbarPos('S','seapic')
    v = cv.getTrackbarPos('V','seapic')

    lower_hsv = np.array([h,s,v])
    upper_hsv = np.array([180,255,255])

    mask = cv.inRange(hsv,lower_hsv,upper_hsv)
    result = cv.bitwise_and(img,img,mask=mask)


    cv.imshow('seapic',result)
    if cv.waitKey(0) and 0xFF == 27:
        break
cv.destroyAllWindows()