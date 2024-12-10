import cv2
import numpy as np

img = cv2.imread('image.png')
newimg = cv2.imread('new_iamge.png')

print(img.shape)

flower = img[100:500 , 300:370]

img[50:450, 60:130] = flower
constant = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REPLICATE)
newimg = newimg[50:50+img.shape[0],50:50+img.shape[1]]

res = cv2.addWeighted(img,0.3,newimg,0.7,0)


cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()