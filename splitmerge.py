#take a image n split it into 3 color channel
import cv2 as cv
import numpy as np



img = cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img) #splits the image into 3 channels
cv.imshow("blue", b)    
cv.imshow("green", g)
cv.imshow("red", r) 

print(img.shape) #(height, width, channels)
print(b.shape) #(height, width)     
print(g.shape) #(height, width)
print(r.shape) #(height, width)
#lighter -> high conc of that color n vis versa
#gre scale image has 1 channel

merged = cv.merge([b,g,r]) #merges the 3 channels into 1 image
cv.imshow("merged", merged)

merged_rgb = cv.merge([r,g,b]) #merges the 3 channels into 1 image
cv.imshow("merged_rgb", merged_rgb)

blue= cv.merge([b,blank,blank]) #merges the 3 channels into 1 image
cv.imshow("blue", blue)

green= cv.merge([blank,g,blank]) #merges the 3 channels into 1 image
cv.imshow("green", green)

red= cv.merge([blank,blank,r]) #merges the 3 channels into 1 image
cv.imshow("red", red)

cv.waitKey(0)