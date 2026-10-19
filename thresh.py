#binarization of image
import cv2 as cv

img= cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#source image, threshold value, if value greater than threshold value what to set it to(maxvalue), threholding type
#return the threshold value(wtv is passed in)
#and the thresh the image

cv.imshow("Thresholded", thresh)

#inversing a thresgold
threshold, thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
#set to max value lesser than the threshold
cv.imshow("Simple threshold inverse", thresh_inv)

##Adaptive Thresholding
#let the computer find the optimal threshold value

adaptive_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
#adaptive_thresh_mean_c calc the mean intensity of neighboring pixels n subtracts it from c
#11 kernel size
#3 C increase c->threshold decreases -> more pixels are white n vis versa
cv.imshow("Adaptive_threshold", adaptive_thresh)
cv.waitKey(0)
