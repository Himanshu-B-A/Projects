import cv2
import random
import requests

camera=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    flag,image=camera.read()

    if flag:
        
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(gray,1.1,4)
        
        # for x,y,w,h in faces:
        #     cv2.rectangle(image,(x,y),(x+w,y+h),(255,125,0),2)
        
        cv2.imshow("Your image",image)
        k=cv2.waitKey(2)
        
        if k==ord('q'):
            break
        
        
        if k==ord('s'):
            num=random.randint(1,1000)
            filename=f"pallavi//myimage{num}.jpg"
            cv2.imwrite(filename,image)

camera.release()