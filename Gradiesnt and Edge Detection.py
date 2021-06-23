#Gradient and Edge Detection

# Importing Modules 
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Geting image and reading it using imread()
img = cv2.imread("Images/dogs.jpg", cv2.IMREAD_GRAYSCALE)

# laplacing shadded black to white strokes
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# canny dark as white sharp line
canny = cv2.Canny(img, 100, 200)

# sobel X black to white in x direction
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

# sobel Y black to white in y direction
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

# sobel Combined 
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# storing the frames and title in list 
titles = ['image', 'Laplacian', 'canny', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, canny, sobelX, sobelY, sobelCombined]
# looping on it to add all the frames in the same plot using for loop
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray') # creating subplot
    plt.title(titles[i]) # title 
    plt.xticks([]),plt.yticks([]) # x,y reference none 

# Show Plot created
plt.show()