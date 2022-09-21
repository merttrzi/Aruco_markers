import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture("abc1.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        # w = width, h = height 
       
        color = (255,0,0)
        thickness = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,thickness)


    cv2.imshow("Frame",frame)
    key =cv2.waitKey(1)
    if key == 27:
        break



cap.release()
# out.release()
cv2.destroyAllWindows()

               





