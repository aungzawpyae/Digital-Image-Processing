# Project 1: Image Enhancement and Histogram Equalization
# 1. Read an image using OpenCV and convert it to grayscale.
# 2. Apply histogram equalization using OpenCV (cv2.equalizeHist()).
# 3. Display the original and enhanced images side-by-side using Matplotlib.
# 4. Save the equalized image.
import cv2
import matplotlib.pyplot as plt

# Load image and convert to grayscale
img = cv2.imread('original_p1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram equalization
equalized = cv2.equalizeHist(gray)

# Display images
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original Grayscale")
plt.imshow(gray, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Histogram Equalized")
plt.imshow(equalized, cmap='gray')
plt.tight_layout()
plt.show()

# Save the equalized image
cv2.imwrite('p1_equalized_image.jpg', equalized)
