import numpy as np
import cv2 as cv
import os

haar_cascade= cv.CascadeClassifier('haar_face.xml')

p=[]
for i in os.listdir(r"Faces/train"):
    p.append(i)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img= cv.imread(r"C:\Users\Myco\Downloads\ML\Faces\val\mindy_kaling\1.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("person", img)

#detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.5,3)

for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label ={label} with a confidence of {confidence}')
    cv.putText(img, str(p[label]),(20,20),fontFace= cv.FONT_HERSHEY_COMPLEX, color=255, fontScale=0.8)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow(f"p[label]",img)

    cv.waitKey(0)