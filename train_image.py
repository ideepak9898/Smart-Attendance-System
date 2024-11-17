import os
import time
import cv2
import csv
import numpy as np
from PIL import Image
from threading import Thread

def create_folder_and_file():
    # Create 'TrainingImageLabel' directory if it doesn't exist
    if not os.path.exists("TrainingImageLabel"):
        os.makedirs("TrainingImageLabel")

    # Create 'Trainner.yml' file if it doesn't exist
    csv_file_path = "TrainingImageLabel" + os.sep + "Trainner.yml"
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)


def getImagesAndLabels(path):
    # path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    # empty ID list
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("TrainingImage")
    Thread(target = recognizer.train(faces, np.array(Id))).start()
    Thread(target = counter_img("TrainingImage")).start()
    recognizer.save("TrainingImageLabel"+os.sep+"Trainner.yml")
    print("All Images")


def counter_img(path):
    imgcounter = 1
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        print(str(imgcounter) + " Images Trained", end="\r")
        time.sleep(0.008)
        imgcounter += 1