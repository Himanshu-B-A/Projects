from os import listdir
import cv2
import numpy as np
import os

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def fetch_subfolder_and_files(folder_path):
    # Check if the provided path is a valid directory
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid directory.")
        return

    # Iterate through the subfolders and files in the given folder
    
    namelbl=[0,1,2,3]
    names=['ganavi','jayanth','keerthana','raghu']
    
    features=[]
    labels=[]
    i=0
    for root, dirs, files in os.walk(folder_path):
        for subdir in dirs:
            subfolder_path = os.path.join(root, subdir)
            print(f"Subfolder: {subfolder_path}")
            for file in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file)
                print(f"File: {file_path}")
                
                img=cv2.imread(file_path)
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                
                faces=cascade.detectMultiScale(gray,1.1,4)
        
                for x,y,w,h in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,125,0),2)
                
                roi=gray[y:y+w,x:x+h]

                features.append(roi)
                labels.append(namelbl[i])
                
                
                # cv2.imshow("your image",roi)
            
                # cv2.waitKey()
            
            i=i+1
    
    print(len(features),len(labels))   
    
    # print(features)         
    # print(labels)
    
    classifier=cv2.face.LBPHFaceRecognizer_create()
    
    classifier.train(features,np.array(labels))
    classifier.save("facemodel.yml")

# Provide the path of the folder you want to fetch subfolders and files from


folder_path = './dataset'
fetch_subfolder_and_files(folder_path)

