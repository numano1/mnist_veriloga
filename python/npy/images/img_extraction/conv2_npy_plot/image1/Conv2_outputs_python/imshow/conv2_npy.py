import numpy as np
import matplotlib.pyplot as plt
import re

# Read numerical data directly from the provided text file
with open('conv2_npy.txt', 'r') as file:
    content = file.read()

# Extract numerical values including scientific notation
numbers = np.array(re.findall(r'-?\d+\.?\d*(?:e[+-]?\d+)?', content), dtype=float)

# Confirm the extracted number of elements matches expected shape (1,6,6,8)
data_array = numbers.reshape(1, 6, 6, 8)

# Plot each of the 8 channels in grayscale
fig, axes = plt.subplots(2, 4, figsize=(12, 6))
axes = axes.flatten()

for i in range(8):
    ax = axes[i]
    img = data_array[0, :, :, i]
    axes[i].imshow(img, cmap='gray')
    axes[i].set_title(f'Channel {i+1}')
    axes[i].axis('off')

plt.tight_layout()
plt.savefig('conv_layer_output_channels.pdf')
plt.show()