import cv2
import math
videoFile = "carcrash2.mp4"

cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = f'D:/Users/ProgFiles/PyProjects/Competitions/2020-06 IBM SCDF 2020/video-crash/test_images/image' +  str(int(x)) + ".jpg";x+=1
        print(filename)
        cv2.imwrite(filename, frame)

cap.release()
print ("Done!")
