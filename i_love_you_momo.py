import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2

t = np.linspace(0, 2 * np.pi, 300)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis('off')

# Set a romantic gradient background using imshow
gradient = np.linspace(0, 1, 400)
bg = np.outer(np.ones(400), gradient)
ax.imshow(
    np.dstack((
        np.ones_like(bg),           # Red channel (full)
        0.2 + 0.8 * bg,             # Green channel (gradient)
        0.6 + 0.4 * bg[::-1],       # Blue channel (reverse gradient)
    )),
    extent=[-20, 20, -20, 20],
    aspect='auto',
    zorder=0
)

# Load momo.jpg and display it in the background (centered, faded)
img = cv2.imread('momo.jpg')
if img is not None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (200, 200))
    ax.imshow(img, extent=[-10, 10, -10, 10], alpha=0.4, zorder=1)

heart, = ax.plot([], [], 'r-', linewidth=3, zorder=2)
emoji = ax.text(0, 0, "", fontsize=60, ha='center', va='center', zorder=3)
text = ax.text(0, -15, "", fontsize=20, color='magenta', ha='center', va='center', fontweight='bold', zorder=3)

def init():
    heart.set_data([], [])
    emoji.set_text("")
    text.set_text("")
    return heart, emoji, text

def animate(i):
    heart.set_data(x[:i], y[:i])
    if i > len(x) - 1:
        emoji.set_text("❤️")
    else:
        emoji.set_text("")
    if i > len(x) // 2:
        text.set_text("I LOVE YOU MOMO")
    return heart, emoji, text

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=len(x)+40, interval=20, blit=True, repeat=False
)

plt.show()