import cv2
import numpy as np

print("Package Imported")

img = cv2.imread("Resources/pm.jpg")
print(img.shape)

imgResize = cv2.resize(img,(150,200))
print(imgResize.shape)

imgCropped = img[0:200, 0:150]
#cropped image [height,width]=[start:end,start:end]

cv2.imshow("Image",img)
cv2.imshow("Resize Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)
