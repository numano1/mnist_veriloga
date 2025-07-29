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
    # Load the bias data from the npy file (expected to contain 120 bias values)
    bias = np.load("biasFLT.npy")
    
    # Convert each bias value to its 4-bit digital representation.
    converted_bias = [convert_to_4bit(int(val)) for val in bias]
    
    # Join all converted values with a single space.
    data_line = " ".join(converted_bias)
    
    # Header for the vector file as provided.
    header = (
        "; Digital Vector File Header for bFLT_c1_<3:0> to bFLT_c120_<3:0>\n\n"
        "radix 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111\n\n"
        "io    iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii iiii\n\n"
        "vname bFLT_c1_<[3:0]> bFLT_c2_<[3:0]> bFLT_c3_<[3:0]> bFLT_c4_<[3:0]> bFLT_c5_<[3:0]> bFLT_c6_<[3:0]> bFLT_c7_<[3:0]> bFLT_c8_<[3:0]> bFLT_c9_<[3:0]> bFLT_c10_<[3:0]> "
        "bFLT_c11_<[3:0]> bFLT_c12_<[3:0]> bFLT_c13_<[3:0]> bFLT_c14_<[3:0]> bFLT_c15_<[3:0]> bFLT_c16_<[3:0]> bFLT_c17_<[3:0]> bFLT_c18_<[3:0]> bFLT_c19_<[3:0]> bFLT_c20_<[3:0]> "
        "bFLT_c21_<[3:0]> bFLT_c22_<[3:0]> bFLT_c23_<[3:0]> bFLT_c24_<[3:0]> bFLT_c25_<[3:0]> bFLT_c26_<[3:0]> bFLT_c27_<[3:0]> bFLT_c28_<[3:0]> bFLT_c29_<[3:0]> bFLT_c30_<[3:0]> "
        "bFLT_c31_<[3:0]> bFLT_c32_<[3:0]> bFLT_c33_<[3:0]> bFLT_c34_<[3:0]> bFLT_c35_<[3:0]> bFLT_c36_<[3:0]> bFLT_c37_<[3:0]> bFLT_c38_<[3:0]> bFLT_c39_<[3:0]> bFLT_c40_<[3:0]> "
        "bFLT_c41_<[3:0]> bFLT_c42_<[3:0]> bFLT_c43_<[3:0]> bFLT_c44_<[3:0]> bFLT_c45_<[3:0]> bFLT_c46_<[3:0]> bFLT_c47_<[3:0]> bFLT_c48_<[3:0]> bFLT_c49_<[3:0]> bFLT_c50_<[3:0]> "
        "bFLT_c51_<[3:0]> bFLT_c52_<[3:0]> bFLT_c53_<[3:0]> bFLT_c54_<[3:0]> bFLT_c55_<[3:0]> bFLT_c56_<[3:0]> bFLT_c57_<[3:0]> bFLT_c58_<[3:0]> bFLT_c59_<[3:0]> bFLT_c60_<[3:0]> "
        "bFLT_c61_<[3:0]> bFLT_c62_<[3:0]> bFLT_c63_<[3:0]> bFLT_c64_<[3:0]> bFLT_c65_<[3:0]> bFLT_c66_<[3:0]> bFLT_c67_<[3:0]> bFLT_c68_<[3:0]> bFLT_c69_<[3:0]> bFLT_c70_<[3:0]> "
        "bFLT_c71_<[3:0]> bFLT_c72_<[3:0]> bFLT_c73_<[3:0]> bFLT_c74_<[3:0]> bFLT_c75_<[3:0]> bFLT_c76_<[3:0]> bFLT_c77_<[3:0]> bFLT_c78_<[3:0]> bFLT_c79_<[3:0]> bFLT_c80_<[3:0]> "
        "bFLT_c81_<[3:0]> bFLT_c82_<[3:0]> bFLT_c83_<[3:0]> bFLT_c84_<[3:0]> bFLT_c85_<[3:0]> bFLT_c86_<[3:0]> bFLT_c87_<[3:0]> bFLT_c88_<[3:0]> bFLT_c89_<[3:0]> bFLT_c90_<[3:0]> "
        "bFLT_c91_<[3:0]> bFLT_c92_<[3:0]> bFLT_c93_<[3:0]> bFLT_c94_<[3:0]> bFLT_c95_<[3:0]> bFLT_c96_<[3:0]> bFLT_c97_<[3:0]> bFLT_c98_<[3:0]> bFLT_c99_<[3:0]> "
        "bFLT_c100_<[3:0]> bFLT_c101_<[3:0]> bFLT_c102_<[3:0]> bFLT_c103_<[3:0]> bFLT_c104_<[3:0]> bFLT_c105_<[3:0]> bFLT_c106_<[3:0]> bFLT_c107_<[3:0]> "
        "bFLT_c108_<[3:0]> bFLT_c109_<[3:0]> bFLT_c110_<[3:0]> bFLT_c111_<[3:0]> bFLT_c112_<[3:0]> bFLT_c113_<[3:0]> bFLT_c114_<[3:0]> bFLT_c115_<[3:0]> "
        "bFLT_c116_<[3:0]> bFLT_c117_<[3:0]> bFLT_c118_<[3:0]> bFLT_c119_<[3:0]> bFLT_c120_<[3:0]>\n\n"
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
    output_filename = "biasFLT.vec"
    with open(output_filename, "w") as f:
        f.write(output_content)
    
    print(f"Conversion complete. Vector file saved as '{output_filename}'.")

if __name__ == "__main__":
    main()
