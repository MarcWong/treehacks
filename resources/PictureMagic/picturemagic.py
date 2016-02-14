import debugger
from toning import *
from parameters import *
from partition import *
import cv2
from wolframcloud import *
import re

def PictureMagic(inputurl, inputfile, outputfile):
	areas = Partition(inputfile)
	wc = WolframCloud()
	labels = wc.call(inputurl)
	labels = re.findall(r'"([^:"]*)::[^"]*"', labels)
	print labels

	for l in BUILDING_LABELS:
		if l in labels :
			area_id = range(1, len(areas))
			area_id.sort(lambda x, y: cmp(areas[x][3], areas[y][3])) # sort by inscending order
			areas[area_id[0]][1] = "building"
			areas[area_id[1]][1] = "building"
			break

	# area : [filename, label, size(percent), average, variance]

	#print areas
	image = cv2.imread(inputfile)
	mix = deepcopy(image)

	d_all = [[RADIUS] * mix.shape[1]] * mix.shape[0]

	for area in areas[1:]:
		selected = cv2.imread(area[0], 0)
		d = Distance(selected)
		if area[1] != "unknown" :
			print area[0], ":", area[1]
		if area[1] == "sky" :
			r, g, b = Midtone(area[3])
			diff = SKY_BRIGHTNESS - Value(area[3])
		
			processed = image
			processed = Brightness(processed, d, diff)
			processed = ColorBalance(processed, d, [0]*3, (SKY_B-b, SKY_G-g, SKY_R-r), [0]*3)
			processed = Level(processed, d, 0, 120, 255)
		
			#cv2.imwrite("test_result_1.png", processed)
			mix = Feather(processed, mix, d)
		elif area[1] == "building" :
			print area
			processed = image
			processed = Level(processed, d, 0, pow(pow(128, BUILDING_ENHANCE) / Value(area[3]), 1.0 / (BUILDING_ENHANCE - 1)), 255)
			#diff = BUILDING_BRIGHTNESS - Value(area[3])
			#processed = Brightness(processed, d, diff)
		
			mix = Feather(processed, mix, d)

	shadow, highlight = areas[0]
	midtone = shadow * 255 / float(shadow + highlight)
	mix = Feather(SoftLight(mix, mix), mix, d_all, 0.4)
	mix = Level(mix, d_all, 0, pow(midtone * 128, 0.5), 255)

	cv2.imwrite(outputfile, mix)
