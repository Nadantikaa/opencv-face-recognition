#focuses on a specific part of an image and hides the rest of the image
import cv2 as cv
import numpy as np

img= cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img)

img_large = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat_large.jpg")

blank = np.zeros(img.shape[:2], dtype='uint8') 

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #center of the image, radius, color, thickness(-1->filled)
cv.imshow("mask",circle)

rectangle = cv.rectangle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+100,img.shape[0]//2+100),255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("weird shape", weird_shape)

masked = cv.bitwise_and(img,img, mask= weird_shape)
cv.imshow("masked", masked)
cv.waitKey(0)