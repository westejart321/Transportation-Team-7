#Person Detector using SSD
#This script implements an open source project created by Adrien Rosenbrock at 'https://pyimagesearch.com/2018/11/12/object-detetion-with-deep-learning-and-opencv/'
# and modifies it to output the number of persons detected and send it to a database

# USAGE
# python deep_learning_object_detection.py --image images/img_name.jpg --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
# replace 'img_name.jpg' after the --image tag with the name of the image you want to check. Make sure the image is saved to the 'images' folder.
#if you are not running the script from the location of the 'object-detection-deep-learning' folder, either modify the file paths before 'deep_learning_object_detection.py', '/images/img_name.jpg', 'MobileNetSSD_deploy.prototxt.txt', and 'MobileNetSSD_deploy.caffemodel' to show the correct path, or use the cd function to move to the correct location.
#the buscount2.sh bash script works for this code running from the root folder, run by typing './buscount2.sh' into the terminal

# import the necessary packages
import numpy as np
import argparse
import cv2

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import datetime

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
ap.add_argument("-p", "--prototxt", required=True,
    help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
    help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
    help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
# (note: normalization is done via the authors of the MobileNet SSD
# implementation)
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

# pass the blob through the network and obtain the detections and
# predictions
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

#Variable to count number of persons later
person_count = 0

# loop over the detections
for i in np.arange(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with the
    # prediction
    confidence = detections[0, 0, i, 2]

    # filter out weak detections by ensuring the `confidence` is
    # greater than the minimum confidence
    if confidence > args["confidence"]:
        # extract the index of the class label from the `detections`,
        # then compute the (x, y)-coordinates of the bounding box for
        # the object
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # display the prediction
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[INFO] {}".format(label))
        #adds to variable counting number of people in image
        if "person" in label:
            person_count = person_count+1
        cv2.rectangle(image, (startX, startY), (endX, endY),
            COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

#prints the number of people counted
print("[INFO] There are", person_count, "people in the image")
#sends to database
print("[INFO] Validating...")
#code from 'https://medium.com/datadriveninvestor/use-google-sheets-as-your-database-using-python-77d40009860f'
#credentials
#scope = ['https://spreadsheets.google.com/feeds']

#references ajson file for validation. make sure to change the file path if this is different, the json should be saved in the same folder as this python code.
bustracker='/home/pi/Desktop/object-detection-deep-learning/bus_tracking.json'
#creds = ServiceAccountCredentials.from_json_keyfile_name('bus_tracking.json', scope)
client = gspread.service_account(bustracker)
sheet = client.open('bus').sheet1

#sends the data
#set this first variable to the id of the bus you want, and it will update the database as needed by assigning the output to the proper column number.
bus_id=2
row_no = bus_id+1
bus_route=1
sheet.update_cell(row_no,1,bus_id)
sheet.update_cell(row_no,2,person_count)
sheet.update_cell(row_no,3,20)
bustime = datetime.datetime.now()
sheet.update_cell(row_no,4,str(bustime))
sheet.update_cell(row_no,5,bus_route)
print("[INFO] Sent to database")

# show the output image
#cv2.imshow("Output", image)
#cv2.waitKey(0)