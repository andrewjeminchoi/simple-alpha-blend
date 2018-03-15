# We'll build a linear blender in python using opencv

import sys
import cv2

# Parse the image files
if len(sys.argv) != 4:
    print("Should be in format: script.py img_name1.png img_name2.png alpha value")
    sys.exit("Aborting...")
imgF = sys.argv[1]
imgB = sys.argv[2]
alpha = sys.argv[3]

# Convert alpha value and check if within bounds
alpha = float(alpha)
if not(alpha > 0 and alpha < 1):
    print("Alpha value needs to be 0 < a < 1 !")
    

# Read images
foreground = cv2.imread(imgF)
background = cv2.imread(imgB)

foreground = foreground.astype(float)
background = background.astype(float)

# Use linear blending to foreground and background
beta = 1.0 - alpha
outImage = cv2.addWeighted(foreground, alpha, background, beta, 0.0)


#display image
cv2.imshow("output", outImage/255)
cv2.waitKey(0)
