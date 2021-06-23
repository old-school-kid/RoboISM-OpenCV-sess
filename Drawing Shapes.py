#Drawing Shapes on Images

# Importing the modules 
import numpy as np
import cv2

# reading image 
#img = cv2.imread('lena.jpg', 1)
# creating an array which can be treated as a black image
img = np.zeros([512, 512, 3], np.uint8)

# Line cv2.line(freame to add, start, end, color, width)
img = cv2.line(img, (0,0), (255,255), (147, 96, 44), 10) # 44, 96, 147
# Arrow cv2.arrowedline(freame to add, start, end, color, width)
img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 10)

# Rectangle cv2.rectangle(frame to add, top left, bottom right, color, width)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
# Circle cv2.circle(frame to add, center, radius, color, thickness)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
# Note -- Using "-1 " will fill the element

# TEXT
font = cv2.FONT_HERSHEY_SIMPLEX # font defined
# put Text cv2.putText(frame, text, position bottom left, font, size, color, thickness, cv2.LINE_AA)
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

# Ellips cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# Note -- Using "-1 " will fill the element

# creating an array using numpy
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# resizing
pts = pts.reshape((-1,1,2))
# Polyline cv2.polylines(frame,array,True,color)
img = cv2.polylines(img,[pts],True,(0,255,255))

# Showing image 
cv2.imshow('image', img)

# wait untill action
cv2.waitKey(0)
# destroy window
cv2.destroyAllWindows() 