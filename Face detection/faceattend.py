import datetime
import face_recognition
import cv2
import numpy as np
import os
import glob
directory='photo'
faces_encodings = []
faces_names = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        #print(f)
        basename_without_ext = os.path.splitext(os.path.basename(f))[0]
        print(basename_without_ext)
        faces_names.append(basename_without_ext)

        img1 = face_recognition.load_image_file(f)
        img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        faces_encodings.append( face_recognition.face_encodings(img1)[0])



face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


def checkname(chkname):
    my_file = open("userlog.txt", "w+")
    # reading the file
    data = my_file.read()
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    data_into_list = data
    my_file.close()
    print("dataintolist : ",data_into_list)
    print("chkname : ",chkname)
    if chkname in data_into_list:
        return True
    else:
        return False









video_capture = cv2.videoCapture(2)
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resizewe(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = facerecognition.face_locations( rgb_small_frame)
        face_encodings = face_recognition.face_encodings( rgb_small_frame, face_locations)
        face_names = []
        i=0
        distlist=[]

        my_file = open("userlog.txt", "r")
        # reading the file
        data = my_file.read()
        # replacing end of line('/n') with ' ' and
        # splitting the text it further when '.' is seen.
        data_into_list = data
        my_file.close()


        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces (faces_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance( faces_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            distlist.append(face_distances)

            if matches[best_match_index]:
                name = faces_names[best_match_index]

                timenow = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
                predicted_name = name

                print(predicted_name)
                flag=0
                if (name in data_into_list) or name=="Unknown":
                    print("found")
                    flag=1
                else:
                    flag=0
                    print("not found")
                    file = open("userlog.txt", "a")
                    file.write(predicted_name)
                    file.write("\n")
                    file.close()
            face_names.append(name)


        for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                if flag==1:
                    name="Taken"
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        cv2.imshow('Video', frame)

    process_this_frame = not process_this_frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
