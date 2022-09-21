import cv2
import numpy as np

img = cv2.imread("pers_17.jpg", cv2.IMREAD_GRAYSCALE)

#sift = cv2.xfeatures2d.SIFT_create()
orb = cv2.ORB_create(nfeatures=1500)

#keypoints_sift, descriptors = sift.detectAndCompute(img, None)
keypoints_orb, descriptors = orb.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, keypoints_orb, None)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

