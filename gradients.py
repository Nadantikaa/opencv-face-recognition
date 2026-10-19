#a gradient tells you how quickly image brightness changes, while an edge is where that change is significant.
#then we use them gradient to detect edges
import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#Laplacian -> second order intesity change chnage n rate of change
lap = cv.Laplacian(gray, cv.CV_64F)
#store the result as a 64-bit floating-point image.
#coz laplacian calc produces negative values
#The sign tells us about the local intensity pattern. The magnitude tells us how strong the change in that pattern is.
lap = np.uint8(np.absolute(lap))
#absolut hy do this? Because we want to highlight changes in either direction, whether the intensity increases or decreases.

cv.imshow('Laplacian',lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)#x direction, y direction
#vertical boundaries, because brightness changes when you cross them horizontally
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)#includes dignoacal edge
cv.imshow("Combined sobel", combined_sobel)
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)

canny = cv.Canny(img,125,255)
cv.imshow("canny", canny)
cv.waitKey(0)