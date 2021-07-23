import sys
import numpy as np
import time
import imutils
import cv2

print("Package Imported")

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

CamR=cv2.VideoCapture(1)
CamL=cv2.VideoCapture(2)

CamR.set(10,100)
CamL.set(10,100)

cv_file = cv2.FileStorage()
cv_file.open('stereoMap.xml', cv2.FileStorage_READ)

stereoMapL_x = cv_file.getNode('stereoMapL_x').mat()
stereoMapL_y = cv_file.getNode('stereoMapL_y').mat()
stereoMapR_x = cv_file.getNode('stereoMapR_x').mat()
stereoMapR_y = cv_file.getNode('stereoMapR_y').mat()

while True:

        succes_right, frame_right = CamR.read()
        succes_left, frame_left = CamL.read()

    #CALIBRATION

        undistortedL = cv2.remap(frame_left, stereoMapL_x, stereoMapL_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)
        undistortedR = cv2.remap(frame_right, stereoMapR_x, stereoMapR_y, cv2.INTER_LANCZOS4, cv2.BORDER_CONSTANT, 0)

        #cv2.imshow("Right", frame_right)
        #cv2.imshow("Left", frame_left)

        cv2.putText(frame_right, "R", (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 150, 0), 3)
        cv2.putText(frame_left, "L", (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 150, 0), 3)

        imgStack = stackImages(0.5, ([frame_left,frame_right]))

        cv2.imshow("ImageStack", imgStack)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

