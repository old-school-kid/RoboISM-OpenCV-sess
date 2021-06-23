# importing Module
import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)

# function click
def click_event(event, x, y, flags, param):
    # Checking Event left Key Down
    if event == cv2.EVENT_LBUTTONDOWN:
        # printing the x and y coordinate
        print(x,', ' ,y)

        # Creating the Text to put on screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        # Note -- Can also create string f"{x} , {y}"
        # Putting string at the coordinate the user clicked  
        # cv2.putText(img, text, coordinate bottom left, font, fontscale, color,thickness)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)

        # Showing the Image
        cv2.imshow('image', img)

    # Checking Event right Key Down
    if event == cv2.EVENT_RBUTTONDOWN:
        # getting value of blue , green , red at the coordinate clicked
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        # Creating the Text to put on screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        # Note -- Can also create string f"{blue} , {green} , {red}"
        # Putting string at the coordinate the user clicked  
        # cv2.putText(img, text, coordinate bottom left, font, fontscale, color,thickness)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)

        # Showing the Image
        cv2.imshow('image', img)

# Reading Image
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('Images/dogs.jpg')
# Show Image
cv2.imshow('image', img)

# Calling Image and added click event
cv2.setMouseCallback('image', click_event)

# wait key
cv2.waitKey(0)
# Destroy window
cv2.destroyAllWindows()