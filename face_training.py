import cv2
import numpy as np #for arrays used in the code
from PIL import Image #all image.. codes
import os

# Path for face image database
path = 'dataset'#to take dataset folder file path used later

recognizer = cv2.face.LBPHFaceRecognizer_create()#already in opencv
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');

# function to get the images and label data
def getImagesAndLabels(path): #to obtain images as input in dataset folder
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]  #to obtain images as input in dataset folder
    faceSamples=[] #two arrays will be created for training
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale#face detection harcascde supports only grayscale
        img_numpy = np.array(PIL_img,'uint8')#unint8 stands for 0 to 255 images u can take
        id = int(os.path.split(imagePath)[-1].split(".")[1])#split two arrays
        faces = detector.detectMultiScale(img_numpy) #inbuilt to detect faces
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])#save whole rectangular portion of face
            ids.append(id)    #save all faces according to their respective id
    return faceSamples,ids

print ("\n Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer.yml
recognizer.write('trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the number of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))