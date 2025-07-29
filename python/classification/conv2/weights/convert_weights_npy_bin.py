import numpy as np

# Load .npy file
data = np.load('model_1_conv2d_3_Conv2D_ReadVariableOp_0.npy')

# Function to convert weight to 4-bit digital value
def weight_to_4bit(weight):
    sign_bit = '1' if weight >= 0 else '0'
    magnitude = abs(int(weight))
    magnitude_bits = format(magnitude, '03b')
    return sign_bit + magnitude_bits

# Open text file to write results
with open('weights_digital_layer2.txt', 'w') as f:
    for kernel_idx, kernel in enumerate(data):
        f.write(f'Kernel {kernel_idx + 1}:\n')
        for depth_idx, depth_slice in enumerate(kernel):
            f.write(f'Depth{depth_idx + 1}:\n')
            digital_values = [weight_to_4bit(w) for w in depth_slice.flatten()]
            f.write(' '.join(digital_values) + '\n')