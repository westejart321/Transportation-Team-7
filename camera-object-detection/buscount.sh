#!/bin/bash
fswebcam /home/pi/Desktop/yolo-object-detection/images/test.jpg
python3 /home/pi/Desktop/yolo-object-detection/yolo.py --image /home/pi/Desktop/yolo-object-detection/images/test.jpg --yolo /home/pi/Desktop/yolo-object-detection/yolo-coco