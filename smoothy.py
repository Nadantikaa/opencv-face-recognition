import cv2 as cv

img= cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img)

#averaging the pixel values of an middle pixel(in a kernel) with its neighbors to reduce noise and smooth the image
average = cv.blur(img, (3,3)) #higher kernel size -> higher blur
cv.imshow("average", average)

#Gaussian blur- uses a gaussian kernel to calculate the pixel values of the middle pixel with its neighbors pixels WIGHTS 
#much more natural blur than average blur
gauss = cv.GaussianBlur(img, (3,3), 0) #higher kernel size -> higher blur
#0 is the sigmaX, how much blurring happens horizontally (how weigths are spread from the center)
#small sigma concentrated near the center larger-> spread out

cv.imshow("gauss", gauss)

#median blur- takes the median of all the pixels under the kernel area and the central pixel is replaced with this median value
#Salt-and-pepper noise is a type of image noise where random pixels become either completely white or completely black.
median = cv.medianBlur(img, 3) #higher kernel size -> higher blur
cv.imshow("median", median)

#Bilateral blur- very effective in noise removal while keeping edges sharp
bilateral = cv.bilateralFilter(img, 5, 35, 35)
#5 is the diameter of the pixel neighborhood, 35 is sigmaColor, 35 is sigmaSpace
#sigmaColor- How different two pixel colours can be while still influencing each other
#This helps preserve boundaries between different colours.
#sigmaSpace- How far away pixels can be and still influence each other

cv.imshow("bilateral", bilateral)

cv.waitKey(0)