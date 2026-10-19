import cv2 as cv
import numpy as np

#creating a blank image
blank = np.zeros((500,500,3), dtype='uint8') #500x500 black image
# cv.imshow("Blank", blank)

# cv.waitKey(0)

#1.paint the image a certain color
#blank[:] select all pixels #rows, columns
# blank[200:300, 100:400]= 0,255,0 #green BGR
# cv.imshow("Green", blank)

#2. Draw a rectangle
# cv.imshow("Rectangle", blank)
# #cv.rectangle(blank, (0,0), (250,300), (128, 0, 128), thickness=2) #thickness=-1 will fill the rectangle
# cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 128), thickness=-1) #thickness=-1 will fill the rectangle
# cv.imshow("Rectangle", blank)


#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 0), thickness=3) #thickness=-1 will fill the circle
cv.imshow("Circle", blank)


#4. Draw a line
cv.line(blank, (100,210), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

#write text
cv.putText(blank, "hallo! Ich Bin nads und du?", (100,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (191, 64, 191), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)


