import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#zeros=black
print(img.shape)
#coloring image
#img[:]=255,0,0
#[:] = colour the whole image, put the heigt and width if you want to colour specific area
#255,0,0=blue; BGR

#create a line
#cv2.line(img,(0,0),(300,300),(0,255,0),3)
#(object,(start),(end),(colour),thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#(object,(start),(end width, end height),(colour),thickness)

#create rectangle
cv2.rectangle(img,(0,0),(250,300),(0,0,255),2)
#cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED)

#create circle
cv2.circle(img,(400,50),30,(255,255,0),5)
#(object,(centre),radius,(colour),thickness)

#put text
cv2.putText(img,"OpenCV",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),2)
#(object,"text",(location),font,size,(colour),thickness)

cv2.imshow("Image",img)

cv2.waitKey(0)