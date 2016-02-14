import debugger
import cv2

def resize(image, length): # reduce the length of image to given value
	d = image.shape
	scale = max(d[:2]) / float(length)
	return cv2.resize(image, (int(round(d[1] / scale)), int(round(d[0] / scale))))
