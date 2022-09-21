import cv2
import numpy as np
from object_detector import *

# load aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)


# to get better quality
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret,img = cap.read()
    # get aruco marker
    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    if corners:

        # draw a line around the object
        int_corners = np.int0(corners)
        
        for cnt in int_corners:
            rect=cv2.minAreaRect(cnt)
            (x,y),(w,h),angle=rect

            
            W=5
            # d=50
            # f=(w*d)/W
            # print(f)
            # measured f
            f=1030
            d=(W*f)/w
            text = "distance: {}".format(round(d,1))
            scale = 1.2 + d/75
            

            box=cv2.boxPoints(rect)
            box=np.int0(box)

            cv2.circle(img,(int(x),int(y)),5,(0,0,255),-1)
            cv2.polylines(img,[box],True,(255,0,0),2)
            cv2.putText(img,text,(int(x),int(y)),cv2.FONT_HERSHEY_PLAIN,scale,(0,255,0),2)
            
            

    cv2.imshow("image",img)
    if cv2.waitKey(1) == '27':
        break

    

cap.release()
cv2.destroyAllWindows