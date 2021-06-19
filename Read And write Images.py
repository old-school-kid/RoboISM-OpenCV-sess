## Reading, Displaying and Resizing a Image

import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("Images/dogs.jpg")
#cv2.imshow("Image",img)
(h,w,c)=img.shape
print(h,w,c)

bigger = cv2.resize(img,(480,480))
(h,w,c)=bigger.shape
print(h,w,c)
#cv2.imshow("Image",bigger)

cv2.waitKey(0)
cv2.destroyAllWindows()