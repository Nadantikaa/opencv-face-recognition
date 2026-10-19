import cv2 as cv

# #takes in path to a image n return a matrix
img=cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")
# #print(img)


# #displays the image as a new window 
cv.imshow("cat",img) #winname #matrix


# #waits for a key to be pressed then continues program w the next line
cv.waitKey(0)

# #displayinng a image larger than ur computer screen
# largeimg=cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat_large.jpg")
# cv.imshow("cat_large",largeimg)
# cv.waitKey(0)


#capture = cv.VideoCapture(0) #0 is the default camera
# capture = cv.VideoCapture(r"C:\Users\Myco\Downloads\ML\videos\dog.mp4")

#use a while loop n read the video frame by frame
# while True:
#     isTrue, frame = capture.read() #returns a boolean(wheather the  frame was succesfully read ornot) n the frame
#     cv.imshow("Video", frame)

#     #to stop the video from playing indefinitely we can use a key to break the loop
#     if cv.waitKey(20) and 0xFF == ord('d'): #waits for 20ms n checks if the key pressed is 'd' or not
#         break

# capture.realease() #releases the connection to the video source
# cv.destroyAllWindows() #destroys all the windows created by opencv

# ##NOTE: error: (-215:Assertion failed) means the ath does not have a vlid photo or