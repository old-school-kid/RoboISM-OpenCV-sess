# Importing Module
import cv2
import numpy as np

# Reading Image
img = cv2.imread('Images/dogs.jpg')

# Converting BGR image to RGB format
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Adding Median Blur cv2.medianBlur(frame, ksize)
grey = cv2.medianBlur(grey, 5)
# Adaptive Threahold cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonize ---  
# Readusing unwanted Noice from Image 
color = cv2.bilateralFilter(img, 9, 250, 250)
# Applying Bitwize and operator only two input 1 then 1
cartoon = cv2.bitwise_or(color, color, mask = edges)

# Show Both Images
cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)

#save Image to a file
# cv2.imwrite("cartoon.jpg", cartoon)
# Wait Key
cv2.waitKey(0)
# Destroy window
cv2.destroyAllWindows()