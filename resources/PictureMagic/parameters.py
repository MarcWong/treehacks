def Value(color):
	b, g, r = map(float, color)
	return (r + g + b) / 3

def Midtone(color):
	b, g, r = map(float, color)
	a = r + g + b
	return (b / a * 128 * 3, g / a * 128 * 3, r / a * 128 * 3)

RESIZE_LENGTH = 100

__SKY_R = 190
__SKY_G = 232
__SKY_B = 255
SKY_BRIGHTNESS = Value((__SKY_R, __SKY_G, __SKY_B))

SKY_B, SKY_G, SKY_R = Midtone((__SKY_B, __SKY_G, __SKY_R))

__BUILDING_R = 95
__BUILDING_G = 77
__BUILDING_B = 62
BUILDING_BRIGHTNESS = Value((__BUILDING_R, __BUILDING_G, __BUILDING_B))

BUILDING_ENHANCE = 5 # the bigger, the less effect

RADIUS = 20

BUILDING_LABELS = ["Building", "House", "Hotel", "Architecture", "Tree", "Shed", "Dwell", "Mount", "NaturalElevation"]
