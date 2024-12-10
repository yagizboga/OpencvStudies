import cv2
import numpy as np

img = cv2.imread('image.png')

px = img[100,100]
print(px)

blue = img[100,100,0]
green = img.item(100,100,1)

for i in range(0,100):
    for j in range(0,100):
        img[i,j] = [255,0,0]

print(blue)
print(green)
print("image size:" , img.shape)


cv2.imshow('image',img)
cv2.waitKey(0)


