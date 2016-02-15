from picturemagic import *
import sys

if len(sys.argv) != 2:
	print "Invalid arguments!"
else :
        aa = sys.argv[1].split(",",2)
	PictureMagic(aa[0], aa[1], aa[2])

