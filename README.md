# Pill Dimension Measurement using OpenCV and Python

This Python script utilizes OpenCV and various libraries to measure the dimensions of a pill from an image.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)




## Requirements
Before running the code, ensure you have the following libraries installed:

- [scipy](https://pypi.org/project/scipy/)
- [imutils](https://pypi.org/project/imutils/)
- [numpy](https://pypi.org/project/numpy/)
- [OpenCV (cv2)](https://pypi.org/project/opencv-python/)

You can install these libraries using pip:
```bash
pip install scipy imutils numpy opencv-python
```




## Installation
```bash
git clone https://github.com/yourusername/pill-dimension-measurement.git
cd pill-dimension-measurement
```

Edit the IMAGE_PATH and the PPM variable in the script to specify the path to your input image and your PPM value of the camera:
```bash
IMAGE_PATH = 'your_image.jpg'
PPMR = 0.1015625 # chage according to your camera

```


## Usage

```bash
python measure_pill_dimensions.py
```


## Explanation

This script performs the following steps:

1. Reads an input image and resizes it for processing.
2. Converts the image to grayscale and applies thresholding to create a binary image.
3. Detects contours in the binary image and identifies the contour of the pill.
4. Estimates the dimensions of the pill by finding its minimum bounding rectangle.
5. Calculates the dimensions in millimeters using a predefined pixels-per-millimeter (PPMR) value.
6. Displays the dimensions on the image.

Feel free to modify the code and PPMR value to suit your specific requirements.
