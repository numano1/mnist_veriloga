import numpy as np

# Load .npy file
data = np.load('model_1_conv2d_2_Conv2D_ReadVariableOp_0.npy')

# Function to convert weight to 4-bit digital value
def weight_to_4bit(weight):
    sign_bit = '1' if weight >= 0 else '0'
    magnitude = abs(int(weight))
    magnitude_bits = format(magnitude, '03b')
    return sign_bit + magnitude_bits

# Open text file to write results
with open('weights_digital.txt', 'w') as f:
    for i, kernel in enumerate(data):
        f.write(f'kernel {i + 1}:\n')
        kernel_weights = kernel.flatten()
        digital_values = [weight_to_4bit(w) for w in kernel_weights]
        f.write(' '.join(digital_values) + '\n')
