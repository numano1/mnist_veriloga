#!/usr/bin/env python3
import numpy as np

def convert_to_4bit(value):
    """
    Convert a signed integer (range 0 to 7 in magnitude) to a 4-bit digital representation.
    For zero, return "1000".
    For nonzero:
      - The MSB is "1" if positive and "0" if negative.
      - The remaining 3 bits represent the absolute magnitude in binary.
    """
    if value == 0:
        return "1000"
    sign_bit = "1" if value > 0 else "0"
    magnitude = abs(value)
    if magnitude > 7:
        raise ValueError(f"Value {value} is out of range (0 to 7).")
    mag_bits = format(magnitude, '03b')
    return sign_bit + mag_bits

def main():
    # Load the bias data from the npy file (expected to contain 84 bias values)
    bias = np.load("biasFC1.npy")
    
    # Convert each bias value to its 4-bit digital representation
    converted_bias = [convert_to_4bit(int(val)) for val in bias]
    
    # Join the converted values with a single space
    data_line = " ".join(converted_bias)
    
    # Create the header for the vector file using the provided format
    header = (
        "; Digital Vector File Header for bFC1_c1_<3:0> to bFC1_c84_<3:0>\n\n"
        "radix 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111  1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111\n\n"
        "io    iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii\n\n"
        "vname bFC1_c1_<[3:0]> bFC1_c2_<[3:0]> bFC1_c3_<[3:0]> bFC1_c4_<[3:0]> bFC1_c5_<[3:0]> bFC1_c6_<[3:0]> bFC1_c7_<[3:0]> bFC1_c8_<[3:0]> bFC1_c9_<[3:0]> bFC1_c10_<[3:0]> "
        "bFC1_c11_<[3:0]> bFC1_c12_<[3:0]> bFC1_c13_<[3:0]> bFC1_c14_<[3:0]> bFC1_c15_<[3:0]> bFC1_c16_<[3:0]> bFC1_c17_<[3:0]> bFC1_c18_<[3:0]> bFC1_c19_<[3:0]> bFC1_c20_<[3:0]> "
        "bFC1_c21_<[3:0]> bFC1_c22_<[3:0]> bFC1_c23_<[3:0]> bFC1_c24_<[3:0]> bFC1_c25_<[3:0]> bFC1_c26_<[3:0]> bFC1_c27_<[3:0]> bFC1_c28_<[3:0]> bFC1_c29_<[3:0]> bFC1_c30_<[3:0]> "
        "bFC1_c31_<[3:0]> bFC1_c32_<[3:0]> bFC1_c33_<[3:0]> bFC1_c34_<[3:0]> bFC1_c35_<[3:0]> bFC1_c36_<[3:0]> bFC1_c37_<[3:0]> bFC1_c38_<[3:0]> bFC1_c39_<[3:0]> bFC1_c40_<[3:0]> "
        "bFC1_c41_<[3:0]> bFC1_c42_<[3:0]> bFC1_c43_<[3:0]> bFC1_c44_<[3:0]> bFC1_c45_<[3:0]> bFC1_c46_<[3:0]> bFC1_c47_<[3:0]> bFC1_c48_<[3:0]> bFC1_c49_<[3:0]> bFC1_c50_<[3:0]> "
        "bFC1_c51_<[3:0]> bFC1_c52_<[3:0]> bFC1_c53_<[3:0]> bFC1_c54_<[3:0]> bFC1_c55_<[3:0]> bFC1_c56_<[3:0]> bFC1_c57_<[3:0]> bFC1_c58_<[3:0]> bFC1_c59_<[3:0]> bFC1_c60_<[3:0]> "
        "bFC1_c61_<[3:0]> bFC1_c62_<[3:0]> bFC1_c63_<[3:0]> bFC1_c64_<[3:0]> bFC1_c65_<[3:0]> bFC1_c66_<[3:0]> bFC1_c67_<[3:0]> bFC1_c68_<[3:0]> bFC1_c69_<[3:0]> bFC1_c70_<[3:0]> "
        "bFC1_c71_<[3:0]> bFC1_c72_<[3:0]> bFC1_c73_<[3:0]> bFC1_c74_<[3:0]> bFC1_c75_<[3:0]> bFC1_c76_<[3:0]> bFC1_c77_<[3:0]> bFC1_c78_<[3:0]> bFC1_c79_<[3:0]> bFC1_c80_<[3:0]> "
        "bFC1_c81_<[3:0]> bFC1_c82_<[3:0]> bFC1_c83_<[3:0]> bFC1_c84_<[3:0]>\n\n"
        "tunit 1ns       ; (Optional) Set the time unit (e.g., 1 nanoseconds)\n\n"
        "trise 0.01 \t; 10 picoseconds\n\n"
        "tfall 0.01 \t; 10 picoseconds\n\n"
        "vih 1.2\n\n"
        "vil 0\n\n"
        "voh 1.2\n\n"
        "vol 0\n\n"
        "period 10 ; 100 MHz \n\n"
        "; Data start from here: \n"
    )
    
    # Combine header and data line.
    output_content = header + data_line + "\n"
    
    # Write the content to a new vector file.
    output_filename = "biasFC1.vec"
    with open(output_filename, "w") as f:
        f.write(output_content)
    
    print(f"Conversion complete. Vector file saved as '{output_filename}'.")

if __name__ == "__main__":
    main()