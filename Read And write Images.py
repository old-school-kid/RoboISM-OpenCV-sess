## Reading, Displaying and Resizing a Image

## Importing Modules Required
import cv2
import numpy
import matplotlib.pyplot as plt

# Reading Image
img = cv2.imread("Images/dogs.jpg")

# Showing Image
# cv2.imshow("Image",img)

# Shape of the image Array 
(h,w,c)=img.shape
# -->h height 
# -->w width
# -->c dimention
print(h,w,c)

# Resizing the Image Array 
# cv2.resize(width, height)
bigger = cv2.resize(img,(200,480))
# Shape of the image Array 
(h,w,c)=bigger.shape
print(h,w,c)
# cv2.imshow("Image",bigger)

# wait for user time (if 0 wait untill action)
cv2.waitKey(0)
# distroy cv2 window
cv2.destroyAllWindows()