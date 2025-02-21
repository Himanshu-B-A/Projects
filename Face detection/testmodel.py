import cv2
import requests

fr = cv2.face.LBPHFaceRecognizer_create()
fr.read('facemodel.yml')#Load saved training data

name = {0 : "gaanavi",1 : "jayanth",2 : "keerthana",3 : "raghu",4:"Himanshu B A"}


cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    
    gray=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,1.32,5)
    
    for x,y,w,h in faces:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,255),3)
        
        roi=gray[y:y+w, x:x+h]
        
        label,confidence=fr.predict(roi)

        print(f"{label},{confidence}")
        
        if confidence<=38:
            print(f"{label},{confidence}")
            lbl=name[label]

            userdata = {"firstname": lbl}
            print(userdata)
            resp = requests.post('http://localhost/attend/save.php', params=userdata)

            print(resp)

            cv2.putText(test_img,lbl,(100,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        else:
            print("No result found")
            cv2.putText(test_img,"Unkown",(100,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        
    cv2.imshow("demo",test_img)
    
    k=cv2.waitKey(1)
    
    if k==ord('q'):
        break

cap.release()
    
    