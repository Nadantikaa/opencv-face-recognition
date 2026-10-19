import cv2 as cv

img= cv.imread(r"C:\Users\Myco\Downloads\ML\photos\group 1.jpg")
cv.imshow("Lady", img)

#we dont need color for detection face
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
#cacade classifier class will read in the xml n store in the variable

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)
#the rectangle coordinates for the faces in the img
#scalefactor -> how much the image size is reduced between successive detection passes so faces match the classifier detection window
#minneighbours= how many overlapping detections agree


#no of faces
print(len(face_rect),"the number of faces")
print(face_rect)
for (i,j,k,l)in face_rect: #x,y, width, height
    cv.rectangle(img,(i,j),(i+k,j+l),(0,255,0),1)
cv.imshow("Annotated", img)
cv.waitKey(0)