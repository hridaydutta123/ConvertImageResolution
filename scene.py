from PIL import Image
import os
import sys

# Check command line arguments
if len(sys.argv) < 3:
	print '\t\t Format: python <INPUT_FOLDER_NAME> <OUTPUT_FOLDER_NAME> \t\t'
	sys.exit()

# Reading command line arguments
INPUT_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]

# Changing resolution
resolution_x = 1024
resolution_y = 768

for root, dirs, files in os.walk(INPUT_FOLDER):
  for file in files:
  	print file
  	im = Image.open(os.path.join(INPUT_FOLDER,file))
	im.save(os.path.join(OUTPUT_FOLDER,file), dpi=(resolution_x,resolution_y))