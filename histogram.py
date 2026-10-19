#A histogram in OpenCV is a graph that shows how many pixels in an image have each intensity or colour value.
#visualize pixel intensity distribituions w a histogram(graph or plot)
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow('Ctas', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2-100), 100 , 255 , -1)
cv.imshow("mask", mask)

# masked_img = cv.bitwise_and(gray, gray, mask= mask)
# cv.imshow("masked image",masked_img)

#grayscal histogram
# gray_hist = cv.calcHist([masked_img],[0], mask, [256], [0,256])
#list of images, index of channel grayscale [0]
#Mask ->None
#256 -> histogram bins
#range of intensity
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No of pixels")
# plt.plot(gray_hist)
# plt.show()

#Color histogram

masked_img = cv.bitwise_and(img, img, mask= mask)
cv.imshow("masked image",masked_img)

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
colors =('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask, [256],[0,256])
    #[i] selects the color channel
    plt.plot(hist, color=col)

plt.show()

cv.waitKey(0)