import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def plot_images_from_excel(input_file, output_pdf):
    # Read the Excel file. The first column is the point number (1-36),
    # and the remaining 8 columns represent the 8 channels.
    df = pd.read_excel(input_file)
    
    # Extract the channel data (assumes columns 2 through 9 are the channel data)
    channels = df.iloc[:, 1:]
    
    # Create a figure with 2 rows x 4 columns of subplots for the 8 images.
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    axes = axes.flatten()
    
    # For each channel, reshape its 36 values into a 6x6 matrix and plot.
    for i, col in enumerate(channels.columns):
        data = channels[col].values
        if len(data) != 36:
            print(f"Warning: Column '{col}' does not contain 36 values. Skipping this channel.")
            continue
        
        # Reshape the 36 values into a 6x6 matrix (row-major order).
        image = data.reshape(6, 6)
        
        # Plot the image on the corresponding subplot.
        ax = axes[i]
        #im = ax.imshow(image, cmap='gray', vmin=0, vmax=15, interpolation='nearest')
        im = ax.imshow(image, cmap='gray', vmin=0, vmax=15, interpolation='nearest')
        ax.set_title(f"Channel {col}")
        ax.axis('off')
    
    # Hide any extra axes if there are (should not be in this case).
    for j in range(i+1, len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_pdf, format='pdf')
    print(f"Grayscale images saved to: {output_pdf}")

def main():
    parser = argparse.ArgumentParser(
        description="Plot 8 6x6 grayscale images from an Excel file and save the output as a PDF."
    )
    parser.add_argument("input_file", help="Path to the input Excel file")
    parser.add_argument("output_pdf", help="Path for the output PDF file")
    args = parser.parse_args()
    
    plot_images_from_excel(args.input_file, args.output_pdf)

if __name__ == "__main__":
    main()
#python3.13 conv2_image_8CHNLs.py conv2Outs_INT4.xlsx 8CHNLS_pix_Image_Conv2.pdf
