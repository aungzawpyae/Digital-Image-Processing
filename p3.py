# Project 3: Image Filtering and Comparison
# 1. 2. 3. 4. Read a noisy image (add salt-and-pepper noise artificially if needed).
# Apply three filters: Gaussian blur, median blur, and bilateral filter.
# Display all versions in a single Matplotlib window using subplots.
# Save each processed image with a descriptive filename.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read an image (grayscale for simplicity)
image = cv2.imread('original_p3.jpg', cv2.IMREAD_GRAYSCALE)  # Change filename as needed
if image is None:
    raise FileNotFoundError("Image file not found. Please check the filename and path.")

# Add salt-and-pepper noise artificially
def add_salt_and_pepper_noise(img, amount=0.05, salt_vs_pepper=0.5):
    noisy = img.copy()
    num_salt = np.ceil(amount * img.size * salt_vs_pepper)
    num_pepper = np.ceil(amount * img.size * (1.0 - salt_vs_pepper))

    # Salt noise
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
    noisy[tuple(coords)] = 255

    # Pepper noise
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
    noisy[tuple(coords)] = 0
    return noisy

noisy_image = add_salt_and_pepper_noise(image)
cv2.imwrite('p2_noisy_image.jpg', noisy_image)

# 2. Apply three filters
gaussian = cv2.GaussianBlur(noisy_image, (5, 5), 0)
median = cv2.medianBlur(noisy_image, 5)
bilateral = cv2.bilateralFilter(noisy_image, 9, 75, 75)

cv2.imwrite('p3_gaussian_blur.jpg', gaussian)
cv2.imwrite('p3_median_blur.jpg', median)
cv2.imwrite('p3_bilateral_filter.jpg', bilateral)

# 3. Display all versions in a single Matplotlib window using subplots
titles = ['Original', 'Noisy', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [image, noisy_image, gaussian, median, bilateral]

plt.figure(figsize=(15, 5))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()