import cv2 as cv


cam = cv.VideoCapture(0)
canRead,camFrame = cam.read()
while(True):
    hsvcamFrame = cv.cvtColor(camFrame,cv.COLOR_BGR2HSV)

    cv.imshow('window',hsvcamFrame)
    