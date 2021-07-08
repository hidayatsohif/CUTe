import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

myColors = [[89,219,131,114,255,255],[139,111,183,179,255,255]]
myColorsValue = [[255,0,0],[0,0,255]]
myPoints = [] #[x,y,colorsID]

def findColor(img,myColors,myColorsValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for colors in myColors:
        lower = np.array(colors[0:3])
        upper = np.array(colors[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(str(colors[0]),mask)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorsValue[count],cv2.FILLED)

        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints

def getContours(img):
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>80:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints, myColorsValue):
    for point in myPoints :
        cv2.circle(imgResult,(point[0],point[1]),10, myColorsValue[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorsValue)

    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorsValue)

    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break