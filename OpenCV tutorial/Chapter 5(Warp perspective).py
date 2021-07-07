import cv2
import numpy as np

width, height = 250,350
img = cv2.imread("Resources/card.jpg")

pts1 = np.float32([[224,93],[431,136],[163,382],[369,426]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
