import os
import cv2
import csv


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

directories = ["TrainingImage", "StudentDetails"]
def create_folder_and_file():
    # Check if both "TrainingImage" and "StudentDetails" directories exist, if not, create them
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Create 'StudentDetails.csv' file if it doesn't exist
    csv_file_path = "StudentDetails" + os.sep + "StudentDetails.csv"
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)


def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        har_Cascade = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(har_Cascade)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum = sampleNum+1
                # Saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        print(res)

        row = [Id, name]

        # Check if the file exists and if it is empty, add headers
        file_exists = os.path.isfile("StudentDetails"+os.sep+"StudentDetails.csv")
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)

            if not file_exists:  # If file doesn't exist, write the header
                writer.writerow(['Id', 'Name'])

            # Move to the start of the file and check if it's empty
            csvFile.seek(0)
            first_char = csvFile.read(1)
            if not first_char:  # If file is empty, add the header
                writer.writerow(['Id', 'Name'])

            # Add the student's ID and name to the CSV file
            writer.writerow(row)
    else:
        if is_number(Id):
            print("Enter Alphabetical Name")
        if name.isalpha():
            print("Enter Numeric ID")