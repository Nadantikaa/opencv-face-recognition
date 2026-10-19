import cv2 as cv 
import numpy as np

img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img)

#translation is the shifting of an image along the x and y axis
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    #[1,0,x] 1x + 0y + x
    dim = (img.shape[1], img.shape[0]) #width, height
    return cv.warpAffine(img, transMat, dim)
    #img → the original image.
    #transMat → instructions for shifting the pixels.
    #dim → the dimensions of the output image.
    #-x-> left, +x-> right, -y-> up, +y-> down

translated = translate(img, -100, 100)
cv.imshow("translated", translated)
cv.waitKey(0)

#Rotation is the turning of an image around a fixed point
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)#scale- how big or small you want your image

    dim = (width, height)
    return cv.warpAffine(img, rotMat, dim)

rotated = rotate(img, -45)
cv.imshow("rotated", rotated)

rotate_rotated = rotate(rotated, -90)
cv.imshow("rotate_rotated", rotate_rotated)

cv.waitKey(0)

#Resizing 
resized = cv.resize(img,(500,500), interpolation = cv.INTER_CUBIC)
cv.imshow("resized", resized)

cv.waitKey(0)

#flipping
flip = cv.flip(img, -1) #0-> vertical, 1-> horizontal, -1-> both
cv.imshow("flip", flip) 
cv.waitKey(0)

#cropping
cropped = img[200:400, 300:400] #y1:y2, x1:x2
#Selects rows from 200 to 399(y)
cv.imshow("cropped", cropped)
cv.waitKey(0)