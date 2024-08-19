# Face Detection and Centering with Arduino
## Description
This project focuses on detecting a face in an image and then sending the relative position of the face's center to an Arduino, which controls a servo motor using PyFirmata. The servo motor is used to adjust the camera's orientation, ensuring the face remains centered in the frame. The algorithm calculates the position of the face relative to the image size and sends this information to the Arduino, which then adjusts the servo motor to reposition the camera.

## Features
Face Detection: Identifies a face in the image using computer vision techniques.
Position Calculation: Calculates the position of the face's center relative to the size of the image.
Arduino Control with PyFirmata: Communicates with an Arduino via PyFirmata to control a servo motor.
Servo Motor Adjustment: The servo motor adjusts the camera's orientation to center the face in the frame.

##  Requirements
- Python 3.x
- OpenCV 4.x
- PyFirmata
- Arduino with a servo motor

## Usage
- Face Detection: The algorithm processes the image to detect a face.

- Position Calculation: It calculates the face's center position relative to the image dimensions.

- Data Transmission to Arduino: The position data is sent to the Arduino using PyFirmata.

- Servo Motor Adjustment: The Arduino controls the servo motor to adjust the camera, ensuring the face remains centered (If no face is found within a given time, the program sweeps the room to locate one). 

- Real-Time Feedback: The system continually updates to keep the face centered as it moves within the frame.
