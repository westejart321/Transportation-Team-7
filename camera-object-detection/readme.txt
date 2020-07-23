Useful information for 'bus' portion of the code

DESCRIPTION
Within this folder, there are 2 folders and 2 files.
yolo-object-detection contains the files and script for an open source project that uses YOLO, an object detection system, to count the number of people in a picture and send that information to a database
object-detection-deep-learning contains the files and script for an open source project that uses the MetroNet SSD (single shot detector) and a dnn (deep neural network) to count the number of people in a picture and send that information to a database
buscount.sh is a bash script with 2 commands on it. The first command takes a picture using a camera plugged into the Raspberry Pi, and the second executes the python script for the yolo-object-detection folder. This may need modified if your file path is not the same.
buscount2.sh is a bash script with 2 commands on it. The first command takes a picture using a camera plugged into the Raspberry Pi, and the second executes the python script for the object-detection-deep-learning folder. This may need modified if your file path is not the same.

PYTHON MODULES/LIBRARIES
This program uses the following python modules/libraries. Next to each name, I've listed instructions for how to easily install them, if needed.
These methods worked successfully on a Raspberry Pi 4 on the reccomended 32 bit OS. 
numpy - run 'pip3 install numpy' in the terminal. Should automatically install while trying to install OpenCV.
time - already installed by default.
os - already installed by default.
argparse - already installed by default.
cv2 - this may take several hours, as a warning. I reccomend going to 'https://docs.opencv.org/master/d2/de6/tutorial_py_setup_in_ubuntu.html' and following the instructions for 'Build OpenCV from Source'.
gspread - run 'pip3 install gspread'
fswebcam - run 'pip3 install fswebcam'
oauth2client - run 'pip3 install oauth2client'
datetime - already installed by default


Credits
Adrian Rosenbrock, PyimageSearch
Yolo Object Detection with OpenCV - "https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/"
Object Detection with Deep Learning and OpenCV - "https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/"
Accessed July 2020