import cv2
import os
#for inbuilt webcam use 0
cam = cv2.VideoCapture(0)
cam.set(3, 640) #  width
cam.set(4, 480) #  height
#harcaascade .xml  calling syntax
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Enter the input
face_id = input('\n enter name and press enter ')

print("\n Initializing face save Look the camera and smile ;)")
# Initialize count
count = 0

while(True):
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5) #trial and error depends on webcam
# x,y=coordinates w,h=width height x+w,y+h=other vertice point
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/"+ str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press ESC for exiting video
    if k == 27:
        break
    elif count >=30: # Take 30 face sample and stop video
         break

# Ending
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()




