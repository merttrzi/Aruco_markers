import cv2
import numpy as np
import face_recognition



cap = cv2.VideoCapture("abc1.mp4")
while True:
    ret, frame = cap.read()

    imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
    facesCurFrame = face_recognition.face_locations(imgS)
    for (y1, x2, y2, x1) in facesCurFrame:
     
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)


    cv2.imshow("Frame",frame)
    key =cv2.waitKey(1)
    if key == 27:
        break



cap.release()
cv2.destroyAllWindows()
