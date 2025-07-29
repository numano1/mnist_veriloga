import numpy as np
import matplotlib.pyplot as plt

# Load the convolutional weights (make sure the file path is correct)
weights = np.load("/Users/omarnuman/Desktop/Vmodel_paper/Python_VerilogA/npy/conv2d_3_kernel_0.npy")
kernel_height, kernel_width, in_channels, out_channels = weights.shape

print("Weight shape:", weights.shape)

# Check that each kernel is 3x3 and that there are 32 matrices
assert kernel_height == 3 and kernel_width == 3, "Kernels are not 3x3"
assert out_channels * in_channels == 32, "Expected 32 matrices in total"

# Arrange the 32 matrices in a grid (for example 4 rows x 8 columns)
rows, cols = 4, 8
fig, axes = plt.subplots(rows, cols, figsize=(cols * 2, rows * 2))

# Iterate over all output and input channels and plot the corresponding kernel
matrix_idx = 0
for out_ch in range(out_channels):
    for in_ch in range(in_channels):
        # Calculate row and column index for the subplot
        r = matrix_idx // cols
        c = matrix_idx % cols
        
        ax = axes[r, c]
        kernel = weights[:, :, in_ch, out_ch]
        
        im = ax.imshow(kernel, cmap='gray', vmin=-7, vmax=7)
        ax.set_title(f"Out {out_ch}, In {in_ch}", fontsize=8)
        ax.axis('off')
        
        # Overlay numerical values on each cell of the 3x3 kernel
        for i in range(kernel_height):
            for j in range(kernel_width):
                # Choose text color based on the kernel value for contrast
                text_color = "white" if kernel[i, j] < 0 else "black"
                ax.text(j, i, f"{kernel[i, j]:.2f}", ha="center", va="center", color=text_color, fontsize=8)
        
        # Optional: Add a colorbar for each subplot
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        
        matrix_idx += 1

plt.tight_layout()
plt.show()
