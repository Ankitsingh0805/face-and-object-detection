import numpy as np
import cv2
import os


cascade_dir = '/ipynb_checkpoints/haarcascade_frontalface_default.xml/'
face_classifier = cv2.CascadeClassifier(os.path.join(cascade_dir, 'haarcascade_frontalface_default.xml'))
eye_classifier = cv2.CascadeClassifier(os.path.join(cascade_dir, 'haarcascade_eye.xml'))


if face_classifier.empty() or eye_classifier.empty():
    print("Error: Unable to load Haar Cascade classifiers.")
    exit()


img = cv2.imread('object.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if len(faces) == 0:
    print("No Face Found")
    exit()

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (127, 0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)

cv2.imshow('Detected Faces and Eyes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
