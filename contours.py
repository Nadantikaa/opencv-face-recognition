import cv2 as cv
import numpy as np
##contour Curves or outlines that represent the boundaries of objects or shapes.


img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(img, 150, 175)
cv.imshow("canny", canny)

# ##binnarising a image
# ret, thresh = cv.threshold(gray, 150, 175, cv.THRESH_BINARY)
# #below 150 pixel set to black 0 above 175 set to white 1
# cv.imshow("thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#mode cv.RETR_LIST → retrieves all of the contours without establishing any hierarchical relationships.
#mode cv.RETR_EXTERNAL → retrieves only the extreme outer contours.
#mode cv.RETR_CCOMP → retrieves all of the contours and organizes them into a two-level hierarchy.
#mode cv.RETR_TREE → retrieves all of the contours and reconstructs a full hierarchy of

#Chain_approx_none- does all returns all contouts. how u want to approx the contours
#chain_approx_simple - compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangular contour is encoded with 4 points.
#contours- python list of all coordinated of the contours that were found
#hierarchies - information about how the detected contours relate to one another.
print(f"{len(contours)} contours found")
print(f"{hierarchies} hierarchies found")

##gonna draw the contours on the blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1) #-1 means draw all contours
#last arg is scale
cv.imshow("contours drawn", blank)

cv.waitKey(0)
