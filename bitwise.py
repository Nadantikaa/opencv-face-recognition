import cv2 as cv

import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) #-1 -> filled rectangle #255-> white
circle = cv.circle(blank.copy(), (200,200),200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

#bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

#bitwise OR ->non intersecting and intersecting area
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

#bitwise XOR -> non intersecting area
#1 when the bits are different and 0 when they are the same.

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

#bitwise NOT -> inverts the bits of an image
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)