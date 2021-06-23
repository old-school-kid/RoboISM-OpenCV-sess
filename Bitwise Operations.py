#bitwise operations

# Importing Module
import cv2
import numpy as np

# Creating a array having all value as Zero
img1 = np.zeros((253 ,450, 3), np.uint8)
# Rectange cv2.rectange(frame,start top left ,end bottom right,color,fill or stroke (-1 or val>0))
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1)
# Reading a image
img2 = cv2.imread("Images/dogs.jpg")

# Binnary Operation 
bitAnd = cv2.bitwise_and(img2, img1) # and operation between two frame
bitOr = cv2.bitwise_or(img2, img1) # or operation between two frame
bitXor = cv2.bitwise_xor(img1, img2) # X-or operation between two frame
bitNot1 = cv2.bitwise_not(img1) # Not operation on img1 (zero array)
bitNot2 = cv2.bitwise_not(img2) # Not operation on img2 (image)


# Show all the frames Created 
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

# Wait Key
cv2.waitKey(0)
# Destroy all Windows
cv2.destroyAllWindows()