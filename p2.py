# Project 2: Edge Detection and Overlay
# 1. 2. 3. 4. 5. Read a color image using OpenCV.
# Convert it to grayscale and apply Gaussian blur.
# Use the Canny edge detector to find edges.
# Overlay the edges on the original image (e.g., in red).
# Display and save the result using OpenCV or Matplotlib.

import cv2
import numpy as np

# 1. Read a color image using OpenCV
image = cv2.imread('original_p2.jpg')  # Replace 'input.jpg' with your image filename

if image is None:
    raise FileNotFoundError("Image file not found. Please check the filename and path.")

# 2. Convert to grayscale and apply Gaussian blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. Use the Canny edge detector to find edges
edges = cv2.Canny(blurred, 50, 150)

# 4. Overlay the edges on the original image (in red)
overlay = image.copy()
overlay[edges != 0] = [0, 0, 255]  # Set edge pixels to red (BGR)

# 5. Display and save the result
cv2.imshow('Edge Overlay', overlay)
cv2.imwrite('p2_edge_overlay.jpg', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()