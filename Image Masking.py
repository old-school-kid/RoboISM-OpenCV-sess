#Masking an image
#In mask operations the value of each pixel of an image is recalculated
#based on a given mask matrix, this is known as the kernel.
#Masking is otherwise known as filtering.

# Importing module
import cv2
import numpy as np

# passing function
def nothing(x):
    pass

# Naming the tracking window
cv2.namedWindow("Tracking")
# creating track objects
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing) #lower Hue value  
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing) #Lower Saturation value
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing) #Lower Value value
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing) #Upper Hue value
cv2.createTrackbar("US", "Tracking", 255, 255, nothing) #Upper Saturation value
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing) #Upper Value value

# WHile Loop 
while True:
    # Reading Image 
    frame = cv2.imread('Images/dogs.jpg')

    # Converting the BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #  Setting Position for lower trackbar
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    #  Setting Position for upper trackbar
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Preparing a array of respactive lower and upper trackbar
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # created a mask to apply on frame
    mask = cv2.inRange(hsv, l_b, u_b)

    # Bitwize and operator 
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Showing all the frames original, mask, res
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

# Destroy the window
cv2.destroyAllWindows()