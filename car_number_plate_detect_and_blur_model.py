#license plate detection
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img=cv2.imread('C:/Users/GOWTHAM/OneDrive/Desktop/tfframework/object detection/number plate.jpg')

def display(img):
    fig=plt.figure(figsize=(10,8))
    ax=fig.add_subplot(111)
    new_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ax.imshow(new_img)

display(img)

plate_cascade=cv2.CascadeClassifier('C:/Users/GOWTHAM/OneDrive/Desktop/tfframework/object detection/haarcascade_russian_plate_number.xml')

def detect_plate(img):
    plate_img=img.copy()

    plate_rects=plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)

    for (x,y,w,h) in plate_rects:
        cv2.rectangle(plate_img,(x,y),(x+w,y+h),(0,0,255),4)

    return plate_img

result=detect_plate(img)

display(result)

def detect_and_blur_plate(img):
    plate_img=img.copy()
    roi=img.copy()

    plate_rects=plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)

    for (x,y,w,h) in plate_rects:

        roi=roi[y:y+h,x:x+w]
        blurred_roi=cv2.medianBlur(roi,7)

        plate_img[y:y+h,x:x+w]=blurred_roi

    return plate_img

result=detect_and_blur_plate(img)
display(result)