import cv2
import numpy as np
img= cv2.imread("S:/PROGRAM/ImageProcessing/Ch2-images/apple.jpg",0)
max=np.max(img)
min=np.min(img)
r,c=img.shape[:2]
for i in range(0,r):
    for j in range(0,c):
        img[i,j]=(img[i,j]-min)*255/(max-min)
cv2.imshow("Contrast stretched image",img)
cv2.waitKey(0)
