# Real-Time Face Detection and Smile Recognition

## Overview

This Python script demonstrates real-time face detection and smile recognition using OpenCV, a popular computer vision library. It utilizes pre-trained Haar cascade classifiers for detecting frontal faces and smiles from live webcam feed.

## Features

- Detects frontal faces in real-time using a Haar cascade classifier.
- Recognizes smiles within detected faces using another Haar cascade classifier.
- Draws rectangles around detected faces and smiles.
- Labels smiling faces with "Smiling" text below the face rectangle.

## Requirements

- Python 3.x
- OpenCV (cv2) library
- Pre-trained Haar cascade classifiers for face and smile detection (`haarcascade_frontalface_default.xml` and `haarcascade_smile.xml`, respectively)

## Usage

1. Clone or download the repository.
2. Ensure that Python and OpenCV are installed on your system.
3. Run the Python script (`face_smile_detection.py`).
4. View the real-time face detection and smile recognition from your webcam feed.

## Note

- The Haar cascade classifiers (`haarcascade_frontalface_default.xml` and `haarcascade_smile.xml`) are included in the repository. However, you may replace them with other classifiers for improved performance or different use cases.

## Credits

- This project is inspired by various tutorials and examples on face detection and smile recognition using OpenCV.

Feel free to contribute, provide feedback, or report issues!
