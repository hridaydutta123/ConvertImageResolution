from PIL import Image
import os
import sys

# Check command line arguments
if len(sys.argv) < 3:
	print '\t\t Format: python <EXECUTABLE_FILE> <INPUT_FOLDER_NAME> <OUTPUT_FOLDER_NAME> \t\t'
	sys.exit()

# Reading command line arguments
INPUT_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]

# Expected resolution
print "Desired Resolution ?? e.g. 1024x768"
try:
	resolution = map(int,raw_input().split("x"))
except :
	raise ValueError("Invalid input !")

# Here Magic Happens
for root, dirs, files in os.walk(INPUT_FOLDER):
  for file in files:
  	print file
  	im = Image.open(os.path.join(INPUT_FOLDER,file))
  	im_resized = im.resize(resolution, Image.ANTIALIAS)
	im_resized.save(os.path.join(OUTPUT_FOLDER,file))





