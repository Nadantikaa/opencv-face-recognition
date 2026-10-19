#switching between color spaces
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img) #BGR image


# plt.imshow(img) #RGB image(matplotlyst)
# plt.show()

#bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#bgr to HSV(hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

#bgr to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)


#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

plt.imshow(rgb)
plt.show()

#HSV to BGR (hsv->bgr->grayscale no direct conversion)
bgr_from_hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("bgr_from_hsv", bgr_from_hsv)
gray_from_bgr_from_hsv = cv.cvtColor(bgr_from_hsv, cv.COLOR_BGR2GRAY)
cv.imshow("gray_from_bgr_from_hsv", gray_from_bgr_from_hsv)

cv.waitKey(0)
