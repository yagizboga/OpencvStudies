import cv2
import numpy as np

drawing = False

img = np.zeros((512,512,3),np.uint8)

def draw_line(event,x,y,param,flags):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img,(x,y),(x,y),(50,50,50),20)

        


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_line)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()