#!/bin/bash
fswebcam /home/pi/Desktop/object-detection-deep-learning/images/test.jpg
python3 /home/pi/Desktop/object-detection-deep-learning/deep_learning_object_detection.py --image /home/pi/Desktop/object-detection-deep-learning/images/test.jpg --prototxt /home/pi/Desktop/object-detection-deep-learning/MobileNetSSD_deploy.prototxt.txt --model /home/pi/Desktop/object-detection-deep-learning/MobileNetSSD_deploy.caffemodel