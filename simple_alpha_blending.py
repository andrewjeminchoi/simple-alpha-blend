# We'll build a simple alpha-blender in python using opencv

import sys
import cv2

# Parse the image files
if len(sys.argv) != 4:
    print("Should be in format: simple_alpha_blender.py img_name1.png img_name2.png background_name.png")
imgF = sys.argv[1]
imgB = sys.argv[2]
bg = sys.argv[3]

# Read images
foreground = cv2.imread(imgF)
background = cv2.imread(imgB)
alpha = cv2.imread(bg)

foreground = foreground.astype(float)
background = background.astype(float)

# Normalize intensity of alpha mask
alpha = alpha.astype(float)/255

foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)

# Add masked foreground and background
outImage = cv2.add(foreground, background)

#display image
cv2.imshow("output", outImage/255)
cv2.waitKey(0)
