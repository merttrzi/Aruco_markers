import cv2
import numpy as np
from object_detector import *

# load aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# load object detector
detector = HomogeneousBgDetector()

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
        cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

        # find the perimeter of the marker
        aruco_perimeter = cv2.arcLength(corners[0],True)

        # pixel to cm ratio
        pixe_cm_ratio = aruco_perimeter/20

        # draw object boundaries
        contours = detector.detect_objects(img)

        for cnt in contours:
            rect=cv2.minAreaRect(cnt)
            (x,y),(w,h),angle=rect

            w_cm = w/(aruco_perimeter/20)
            h_cm = h/(aruco_perimeter/20)

            box=cv2.boxPoints(rect)
            box=np.int0(box)

            cv2.circle(img,(int(x),int(y)),5,(0,0,255),-1)
            cv2.polylines(img,[box],True,(255,0,0),2)
            cv2.putText(img,"width {} cm".format(round(w_cm,1)),(int(x-100),int(y+20)),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),2)
            cv2.putText(img,"height {} cm".format(round(h_cm,1)),(int(x-100),int(y-15)),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),2)

    cv2.imshow("image",img)
    if cv2.waitKey(1) == '27':
        break

    

cap.release()
cv2.destroyAllWindows