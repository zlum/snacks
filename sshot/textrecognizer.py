import cv2
import numpy
import os
import pytesseract

# Get grayscale image
def get_grayscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding
def thresholding(image):
	return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def recognize(im):
    # Convert image to cv2 format
    im = numpy.array(im.convert('RGB')) 
    im = im[:, :, ::-1].copy() 

    # Preparing img
    im = get_grayscale(im)
    im = thresholding(im)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    # Recognize text in box
    # Set enviroment variable with path to tesseract trained data
    os.environ["TESSDATA_PREFIX"] = "data"
    
    return pytesseract.image_to_string(im, config = "--oem 1 --psm 6 -l best-eng")