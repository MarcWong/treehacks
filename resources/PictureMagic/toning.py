from copy import *
from parameters import *
import numpy as np

def Check(x) :
	return max(min(int(round(x)), 255), 0)

def Distance(a) :
	d = np.zeros(a.shape)
	q = []
	for x in range(d.shape[0]):
		for y in range(d.shape[1]):
			if x > 0 and bool(a[x][y]) != bool(a[x-1][y]):
				d[x][y] = RADIUS / 2
				q.append((x, y))
			elif y > 0 and bool(a[x][y]) != bool(a[x][y-1]):
				d[x][y] = RADIUS / 2
				q.append((x, y))
			elif x < a.shape[0]-1 and bool(a[x][y]) != bool(a[x+1][y]):
				d[x][y] = RADIUS / 2
				q.append((x, y))
			elif y < a.shape[1]-1 and bool(a[x][y]) != bool(a[x][y+1]):
				d[x][y] = RADIUS / 2
				q.append((x, y))
			else:
				d[x][y] = -10
	i = 0
	while i < len(q):
		x, y = q[i]
		d[x][y] = min(max(d[x][y], 0), RADIUS)
		if x > 0 and d[x-1][y] == -10:
			d[x-1][y] = d[x][y] + (1 if a[x][y] else -1) 
			q.append((x-1, y))
		if y > 0 and d[x][y-1] == -10:
			d[x][y-1] = d[x][y] + (1 if a[x][y] else -1)
			q.append((x, y-1))
		if x < a.shape[0]-1 and d[x+1][y] == -10:
			d[x+1][y] = d[x][y] + (1 if a[x][y] else -1)
			q.append((x+1, y))
		if y < a.shape[1]-1 and d[x][y+1] == -10:
			d[x][y+1] = d[x][y] + (1 if a[x][y] else -1)
			q.append((x, y+1))
		i += 1
	return d

def Feather(image1,image2,d,p=1.0):
	result = deepcopy(image2)
	for x in range(image1.shape[0]):
		for y in range(image1.shape[1]):
			if d[x][y] > 0:
				for c in range(image1.shape[2]):
					w = p * d[x][y] / float(RADIUS)
					result[x][y][c] = image1[x][y][c] * w + image2[x][y][c] * (1-w)
	return result

def ColorBalance(image, d, shadow, midtone, highlight):
	result = deepcopy(image)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if d[x][y] == 0:
				continue
			for k in range(image.shape[2]):
				result[x][y][k] += (128 - abs(image[x][y][k] - 128)) / 128.0 * midtone[k]
				if image[x][y][k] < 128 :
					result[x][y][k] += (128 - image[x][y][k]) / 128.0 * shadow[k]
				else :
					result[x][y][k] += (image[x][y][k] - 128) / 128.0 * highlight[k]
	return result

def Brightness(image, d, brightness):
	result = deepcopy(image)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if d[x][y] == 0:
				continue
			for k in range(image.shape[2]):
				result[x][y][k] = Check(result[x][y][k] + brightness)
	return result

def Contrast(image, d, contrast) :
	result = deepcopy(image)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if d[x][y] == 0:
				continue
			for k in range(image.shape[2]):
				result[x][y][k] = Check(result[x][y][k] + (image[x][y][k] - 128) / 128.0 * contrast)
	return result

def SoftLight(image, cover) :
	result = deepcopy(image)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			for k in range(image.shape[2]):
				if cover[x][y][k] > 128:
					result[x][y][k] = 255 - (255 - image[x][y][k]) * (255 - (cover[x][y][k] - 128)) / 255.0
				else:
					result[x][y][k] = image[x][y][k] * (cover[x][y][k] + 128) / 255.0
	return result

def Level(image, d, low, mid, high) :
	result = deepcopy(image)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if d[x][y] == 0:
				continue
			for k in range(image.shape[2]):
				if image[x][y][k] > 128 :
					result[x][y][k] = mid + (image[x][y][k] - 128) / 128.0 * (high - mid)
				else:
					result[x][y][k] = mid + (image[x][y][k] - 128) / 128.0 * (mid - low)
	return result

def GetAverage(image, area) :
	result = [0] * image.shape[2]
	cnt = 0
	for x in range(area.shape[0]):
		for y in range(area.shape[1]):
			if area[x][y] :
				cnt += 1
				for k in range(image.shape[2]):
					result[k] += image[x][y][k]
	return map(lambda x: x / float(cnt), result)
