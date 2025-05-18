import cv2
import matplotlib.pyplot as plt

# 1. Read an RGB image using OpenCV
image = cv2.imread('original_p4.jpg')  # Change filename as needed
if image is None:
    raise FileNotFoundError("Image file not found. Please check the filename and path.")

# 2. Convert to HSV using cv2.cvtColor()
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 3. Display the H, S, and V channels using Matplotlib
titles = ['Hue', 'Saturation', 'Value']
channels = [h, s, v]

plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(channels[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

# 4. Save each channel as a separate grayscale image file
cv2.imwrite('p4_hue_channel.jpg', h)
cv2.imwrite('p4_saturation_channel.jpg', s)
cv2.imwrite('p4_value_channel.jpg', v)