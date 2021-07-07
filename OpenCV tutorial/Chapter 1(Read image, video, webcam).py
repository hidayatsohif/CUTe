import cv2
print("Package Imported")

# Part 1: read images
# img = cv2.imread("Resources/pm.jpg")

# cv2.imshow("Output",img)
# cv2.waitKey(0)
# waitkey is delay, 1000millisecond=1s

# Part 2: read video
# cap = cv2.VideoCapture("Resources/5s cat.mp4")

# while True:
    #success, img = cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(1) & 0xFF ==ord('x'):
        #break
# video will close when we press x

# Part 3: read webcam
cap = cv2.VideoCapture(0)
#webcam id, 0 is default
cap.set(3,640)
#set the width size (3,size)
cap.set(4,480)
#set the height size (4,size)
cap.set(10,100)
#set the brighthness (10,value)

while True:
    success, img = cap.read()
    cv2.imshow("Webcam",img)
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break
