import cv2 as cv
from sympy import capture

def rescaleFrame(frame, scale=0.75):
    #will work for images,video annd live video
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #interpolation is used to resize the image

def changeRes(width,height):
    #works only for live video
    capture.set(3,width) #3 is the property id for width
    capture.set(4,height) #4 is the property id for height

# capture = cv.VideoCapture(0) #0 is the default camera
# capture = cv.VideoCapture(r"C:\Users\Myco\Downloads\ML\videos\dog.mp4")


# while True:
#     isTrue, frame = capture.read() #returns a boolean(wheather the  frame was succesfully read ornot) n the frame

#     frane_resized = rescaleFrame(frame, scale=0.2)#resizing to 20% of the original size

#     cv.imshow("Video", frame)
#     cv.imshow("Video Resized", frane_resized)

#     #to stop the video from playing indefinitely we can use a key to break the loop
#     if cv.waitKey(20) and 0xFF == ord('d'): #waits for 20ms n checks if the key pressed is 'd' or not
#         break

# capture.realease() #releases the connection to the video source
# cv.destroyAllWindows() #destroys all the windows created by opencv


##applying the same function to images
#takes in path to a image n return a matrix
img=cv.imread(r"C:\Users\Myco\Downloads\ML\photos\cat.jpeg")

rescaled_img = rescaleFrame(img, scale=0.5)

# #displays the image as a new window 
cv.imshow("cat",img) #winname #matrix
cv.imshow("Rescaled Cat", rescaled_img)

cv.waitKey(0)