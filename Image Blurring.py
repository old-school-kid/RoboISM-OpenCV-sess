#Smoothning and Blurring Images

# Importing Module
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading Image
img = cv2.imread('Images/dogs.jpg')
# Converting the BGR image to RBG image using cvtColor()
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# creating a array containing 1's and diving it all by 25
kernel = np.ones((5, 5), np.float32)/25

# Adding Filter to the image filter2D(src, ddepth, kernel)
dst = cv2.filter2D(img, -1, kernel)

# Blur cv2.blur(src, ksize)
blur = cv2.blur(img, (10, 10))

# GaussionBlur cv2.GaussianBlur(src, ksize, sigmaX)
gblur = cv2.GaussianBlur(img, (11, 11), 0)

# Median Blur cv2.medianBlur(src, ksize)
median = cv2.medianBlur(img, 5)

# Bilateral FIlter cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

# storing the frames and title in list 
titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]
# looping on it to add all the frames in the same plot using for loop
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]) #title
    plt.xticks([]),plt.yticks([])  # x,y reference none 

# Show Plot created
plt.show()