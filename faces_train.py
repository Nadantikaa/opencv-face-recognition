import os
import cv2 as cv
import numpy as np

p =[]
for i in os.listdir(r"C:\Users\Myco\Downloads\ML\Faces\train"):
    p.append(i)

DIR = r"C:\Users\Myco\Downloads\ML\Faces\train"
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features=[]
labels=[]

def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path,image)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)
            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w] #extracts just the face region from the grayscale image using the face's coordinates.
                face_roi = cv.resize(face_roi,(100,100))
                features.append(face_roi)
                labels.append(label)

create_train()

# cv.imshow("extrcated feature",features[0])


# us ethe feature and label list to train our recognizer on it 
face_recognizer = cv.face.LBPHFaceRecognizer_create()


features =np.array(features)
labels = np.array(labels)
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)