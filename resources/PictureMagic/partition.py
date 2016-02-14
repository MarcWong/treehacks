import debugger
from copy import *
from resize import *
from parameters import *
import cv2
import numpy as np
import matplotlib.pyplot as plt

def __Partition(image):
	#change image(2D) to 1D
	image1D = image.reshape((image.shape[0] * image.shape[1], 1))
	image1D = np.float32(image1D)

	#define criteria = (type,max_iter,epsilon)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

	#set flags: hou to choose the initial center
	#---cv2.KMEANS_PP_CENTERS ; cv2.KMEANS_RANDOM_CENTERS
	flags = cv2.KMEANS_RANDOM_CENTERS
	# apply kmeans
	compactness,labels,centers = cv2.kmeans(image1D, 5, criteria, 10, flags)

	return labels.reshape((image.shape[0], image.shape[1]))

def MedianBlur(image):
	WINDOW_SIZE = 5
	result = np.zeros(image.shape)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			l = []
			for i in range(max(x - WINDOW_SIZE / 2, 0), min(x + (WINDOW_SIZE+1) / 2, image.shape[0])):
				for j in range(max(y - WINDOW_SIZE / 2, 0), min(y + (WINDOW_SIZE+1) / 2, image.shape[1])):
					l.append(image[i][j])
			l.sort()
			result[x][y] = l[len(l) / 2]
	return result

def Normalize(image):
	mx = 0
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			mx = max(mx, image[x][y])
	scale = 255 / mx
	result = deepcopy(image)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			result[x][y] *= scale
	return result

def GetBestChannel(channels):
	best = None
	best_diff = 0
	for channel in channels:
		avg = 0
		for x in range(channel.shape[0]):
			for y in range(channel.shape[1]):
				avg += channel[x][y]
		diff = 0
		for x in range(channel.shape[0]):
			for y in range(channel.shape[1]):
				diff += pow(channel[x][y] - avg, 2)
		if diff > best_diff :
			best_diff = diff
			best = channel
	return best

def Partition(inputfile):
	raw = cv2.imread(inputfile)
	color = resize(raw, RESIZE_LENGTH) # color image (resized)
	image = GetBestChannel(cv2.split(color))
	image2 = MedianBlur(__Partition(image))

	cv2.imwrite(inputfile[:-4] + "_partition.png", cv2.resize(Normalize(np.uint8(image2)), (raw.shape[1], raw.shape[0])))
	result = np.uint8(image2)
	mx = 0
	for x in range(result.shape[0]):
		for y in range(result.shape[1]):
			mx = max(mx, result[x][y])
	shadow = 0
	highlight = 0
	for i in range(result.shape[0]):
		for j in range(result.shape[1]):
			v = Value(color[i][j])
			if v < 128:
				shadow += 1
			else :
				highlight += 1
	l = [[shadow, highlight]]
	sky_id = 0
	sky_pos = 100000
	for x in range(mx+1):
		size = result.shape[0] * result.shape[1]
		avg = [0] * color.shape[2]
		var = [0] * color.shape[2]
		pos = 0
		result1 = deepcopy(color)
		#result2 = deepcopy(color)
		for i in range(result.shape[0]):
			for j in range(result.shape[1]):
				if result[i][j] != x:
					size -= 1
					for k in range(color.shape[2]):
						result1[i][j][k] = 0
				else:
					for k in range(color.shape[2]):
						avg[k] += color[i][j][k]
					pos += i
				#	for k in range(result2.shape[2]):
				#		result2[i][j][k] = 0
		avg = map(lambda x: x / float(size), avg)
		for i in range(result.shape[0]):
			for j in range(result.shape[1]):
				if result[i][j] == x:
					for k in range(color.shape[2]):
						var[k] += pow(color[i][j][k] - avg[k], 2)
		pos /= size
		if pos < sky_pos :
			sky_pos = pos
			sky_id = x + 1
		filename = inputfile[:-4] + "_%d.png" % x
		info = [filename, "unknown"]
		info.append(float(size) / (result.shape[0] * result.shape[1]))
		info.append(avg)
		info.append(map(lambda x: x / float(size), var))
		l.append(info)
		cv2.imwrite(filename, cv2.resize(result1, (raw.shape[1], raw.shape[0])))
		#cv2.imwrite(filename, cv2.resize(result2, (raw.shape[1], raw.shape[0])))
	l[sky_id][1] = "sky"
	return l
