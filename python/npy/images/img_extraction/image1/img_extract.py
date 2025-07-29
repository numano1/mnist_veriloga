import numpy as np
import matplotlib.pyplot as plt
import re

# Read numerical data directly from the updated text file
with open('result_1_image1.txt', 'r') as file:
    content = file.read()

# Extract numerical data
numbers = np.array(re.findall(r'-?\d+\.?\d*', content), dtype=float)

# Reshape data according to the known shape (1, 30, 30, 1)
data_array = numbers.reshape(1, 30, 30, 1)

# Convert pixel data to 4-bit binary representation
def pixel_to_4bit(value):
    value_int = int(np.clip(value, 0, 15))
    return format(value_int, '04b')

# Save pixel data to text file as a 30x30 image
with open('image_zero_padding_digital.txt', 'w') as f:
    for row in data_array[0, :, :, 0]:
        digital_values = [pixel_to_4bit(v) for v in row]
        f.write(' '.join(digital_values) + '\n')

# Save pixel data to another text file in a single concatenated line
with open('image_zero_padding_digital_single_line.txt', 'w') as f:
    single_line_data = ''.join([pixel_to_4bit(v) for v in data_array.flatten()])
    f.write(single_line_data)

# Additionally, visualize and save the image
plt.imshow(data_array[0, :, :, 0], cmap='gray', vmin=0, vmax=15)
plt.colorbar()
plt.title('Input Image')
plt.savefig('test_image.png')
