import numpy as np
import cv2
import os

def preprocess_image(image_path):
   
    if not os.path.isfile(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return None


    img = cv2.imread(image_path)

 
    if img is None:
        print("Error: Failed to load image.")
        return None

    resized_img = cv2.resize(img, (800, 600))


    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    blurred_img = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred_img, threshold1=30, threshold2=100)

    _, thresholded_img = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY)

    return thresholded_img

image_path = 'object.png'
preprocessed_image = preprocess_image(image_path)

if preprocessed_image is not None:
    cv2.imshow('Preprocessed Image', preprocessed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
