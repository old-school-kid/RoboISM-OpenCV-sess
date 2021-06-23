#Thresholding an Image

# Importing Module
import cv2 as cv
import numpy as np

# Reading images using imread()
img = cv.imread('Images/dogs.jpg',0)

# coverting specific value to (put 2 values)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) # Threash Binary
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) # Thresh Binary Inversion
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) #thresh truncate
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) #Thresh to zero
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) #threshto zero inversion

# Showing all the frames created
cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

# wait until any action
cv.waitKey(0)
# destroy the window
cv.destroyAllWindows()