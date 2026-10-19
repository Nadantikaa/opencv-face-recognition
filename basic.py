import cv2 as cv

img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img)

#converting a image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Blur a image (reduces a noice)
#BORDER_DEFAULT uses reflection to handle missing pixels at image boundaries, helping produce a smooth blur near the edges.

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #(7,7) is the kernel size, has to be odd
cv.imshow("Blur", blur)


#edge cascade (detects the edges in a image)
canny = cv.Canny(blur, 125, 175) #125 is the lower threshold n 175 is the upper threshold
cv.imshow("Canny", canny)  

# Dilating the image (increases the white region in the image or increases the size of foreground object)
dilated = cv.dilate(canny, (7,7), iterations=3) #iterations is the no of times the dilation is applied
cv.imshow("Dilated", dilated)

#eroding the image (opposite of dilation, reduces the white region in the image or reduces the size of foreground object)   
eroded = cv.erode(dilated, (7,7), iterations=3) #iterations is the no of times the erosion is applied
cv.imshow("Eroded", eroded)


#Resize 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #interpolation is used to resize the image    
cv.imshow("Resized", resized)

#cropping (selecting a region of interest)
crop = img[50:200, 200:400] #rows, columns
cv.imshow("Cropped", crop)

cv.waitKey(0)