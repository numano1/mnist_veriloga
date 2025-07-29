#!/usr/bin/env python3
import numpy as np

def convert_to_4bit(value):
    """
    Convert a signed integer (range 0 to 7 in magnitude) to a 4-bit digital representation.
    For zero, return "1000".
    For nonzero:
        - The MSB is set to "1" for positive and "0" for negative.
        - The remaining 3 bits represent the absolute magnitude (in binary).
    """
    # For zero, output is defined as "1000"
    if value == 0:
        return "1000"
    
    # Determine sign bit: 1 for positive, 0 for negative.
    sign_bit = "1" if value > 0 else "0"
    magnitude = abs(value)
    
    # Ensure magnitude is within [0, 7]
    if magnitude > 7:
        raise ValueError(f"Value {value} is out of range (0 to 7).")
    
    # Convert magnitude to a 3-bit binary string.
    mag_bits = format(magnitude, '03b')
    return sign_bit + mag_bits

def main():
    # Load the bias data from the .npy file (assuming it contains 10 bias values)
    bias = np.load("biasFC2.npy")
    
    # Convert each bias value to its 4-bit digital representation.
    converted_bias = [convert_to_4bit(int(val)) for val in bias]
    
    # Create the header for the vector file.
    header = (
        "; Digital Vector File Header for bFC2_c1_<3:0> to bFC2_c10_<3:0>\n\n"
        "radix 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111\n\n"
        "io    iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii\n\n"
        "vname bFC2_c1_<[3:0]> bFC2_c2_<[3:0]> bFC2_c3_<[3:0]> bFC2_c4_<[3:0]> "
        "bFC2_c5_<[3:0]> bFC2_c6_<[3:0]> bFC2_c7_<[3:0]> bFC2_c8_<[3:0]> "
        "bFC2_c9_<[3:0]> bFC2_c10_<[3:0]>\n\n"
        "tunit 1ns           ; (Optional) Set the time unit (e.g., 1 nanoseconds)\n\n"
        "trise 0.01 \t; 10 picoseconds\n\n"
        "tfall 0.01 \t; 10 picoseconds\n\n"
        "vih 1.2\n\n"
        "vil 0\n\n"
        "voh 1.2\n\n"
        "vol 0\n\n"
        "period 10 ; 100 MHz \n\n"
        "; Data start from here:\n"
    )
    
    # Prepare the data line: one 4-bit group per bias value separated by a space.
    data_line = " ".join(converted_bias)
    
    # Combine header and data.
    output_content = header + data_line + "\n"
    
    # Write the content to a new vector file.
    output_filename = "biasFC2.vec"
    with open(output_filename, "w") as f:
        f.write(output_content)
    
    print(f"Conversion complete. Vector file saved as '{output_filename}'.")

if __name__ == "__main__":
    main()
