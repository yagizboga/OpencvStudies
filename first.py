import cv2
import numpy as np

drawing = False;
mode = True

img = np.zeros((512,512,3),np.uint8)
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(250,0,0),4)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x-100,y-100),(x+100,y+100),(100,100,100),5)
    


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while True:
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


