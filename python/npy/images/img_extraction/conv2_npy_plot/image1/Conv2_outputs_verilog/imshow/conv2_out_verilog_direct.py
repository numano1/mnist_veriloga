import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def plot_voltage_images_from_excel(input_file, output_pdf):
    # Read the Excel file.
    # Assumes the first column is a point number (ignored) and
    # the rest of the columns contain voltage values.
    df = pd.read_excel(input_file)
    
    # Extract channel data from all columns except the first.
    channels = df.iloc[:, 1:]
    
    # Create a figure with 2 rows x 4 columns for 8 channels.
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    axes = axes.flatten()
    
    # For each channel, reshape the 36 voltage values into a 6x6 image.
    for i, col in enumerate(channels.columns):
        data = channels[col].values
        if len(data) != 36:
            print(f"Warning: Column '{col}' does not contain 36 values. Skipping this channel.")
            continue
        
        image = data.reshape(6, 6)  # Reshape into 6x6 matrix.
        
        ax = axes[i]
        # Plot the voltage image in grayscale. No conversion or vmin/vmax is set.
        ax.imshow(image, cmap='gray', interpolation='nearest')
        ax.set_title(f"Channel {col}")
        ax.axis('off')
    
    # Hide any extra subplots (if there are any).
    for j in range(i+1, len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_pdf, format='pdf')
    print(f"Grayscale voltage images saved to: {output_pdf}")
    plt.show()

def main():
    parser = argparse.ArgumentParser(
        description="Plot 6x6 grayscale images from voltage values in an Excel file. "
                    "The first column is assumed to be point numbers, and the remaining columns contain voltage values."
    )
    parser.add_argument("input_file", help="Path to the input Excel file containing voltage values")
    parser.add_argument("output_pdf", help="Path for the output PDF file")
    args = parser.parse_args()
    
    plot_voltage_images_from_excel(args.input_file, args.output_pdf)

if __name__ == "__main__":
    main()
#python3.13 conv2_out_verilog_direct.py Conv2Outs.xlsx output_no_ADC.pdf