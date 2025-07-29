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
    if value == 0:
        return "1000"
    sign_bit = "1" if value > 0 else "0"
    magnitude = abs(value)
    if magnitude > 7:
        raise ValueError(f"Value {value} is out of range (0 to 7).")
    mag_bits = format(magnitude, '03b')
    return sign_bit + mag_bits

def main():
    # Load the weight data from the npy file; expected shape is 84x10.
    weights = np.load("weightFC2.npy")
    
    # Process each row: convert each element to its 4-bit representation,
    # then concatenate the 10 values (resulting in a 40-bit string).
    digital_words = []
    for row in weights:
        # Convert each element in the row.
        converted_row = [convert_to_4bit(int(val)) for val in row]
        # Concatenate without any separator.
        word = "".join(converted_row)
        digital_words.append(word)
    
    # Join all 84 digital words with a single space between them.
    data_line = " ".join(digital_words)
    
    # Define the header for the weight vector file.
    header = (
        "; Digital Vector File Header for wFC2_r1_<39:0> to wFC2_r84_<39:0>\n\n"
        "radix 1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111 "
        "1111111111111111111111111111111111111111 1111111111111111111111111111111111111111\n\n"
        "io    iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii "
        "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii "
        "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii "
        "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii "
        "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\n\n"
        "vname wFC2_r1_<[39:0]> wFC2_r2_<[39:0]> wFC2_r3_<[39:0]> wFC2_r4_<[39:0]> "
        "wFC2_r5_<[39:0]> wFC2_r6_<[39:0]> wFC2_r7_<[39:0]> wFC2_r8_<[39:0]> wFC2_r9_<[39:0]> "
        "wFC2_r10_<[39:0]> wFC2_r11_<[39:0]> wFC2_r12_<[39:0]> wFC2_r13_<[39:0]> wFC2_r14_<[39:0]> "
        "wFC2_r15_<[39:0]> wFC2_r16_<[39:0]> wFC2_r17_<[39:0]> wFC2_r18_<[39:0]> wFC2_r19_<[39:0]> "
        "wFC2_r20_<[39:0]> wFC2_r21_<[39:0]> wFC2_r22_<[39:0]> wFC2_r23_<[39:0]> wFC2_r24_<[39:0]> "
        "wFC2_r25_<[39:0]> wFC2_r26_<[39:0]> wFC2_r27_<[39:0]> wFC2_r28_<[39:0]> wFC2_r29_<[39:0]> "
        "wFC2_r30_<[39:0]> wFC2_r31_<[39:0]> wFC2_r32_<[39:0]> wFC2_r33_<[39:0]> wFC2_r34_<[39:0]> "
        "wFC2_r35_<[39:0]> wFC2_r36_<[39:0]> wFC2_r37_<[39:0]> wFC2_r38_<[39:0]> wFC2_r39_<[39:0]> "
        "wFC2_r40_<[39:0]> wFC2_r41_<[39:0]> wFC2_r42_<[39:0]> wFC2_r43_<[39:0]> wFC2_r44_<[39:0]> "
        "wFC2_r45_<[39:0]> wFC2_r46_<[39:0]> wFC2_r47_<[39:0]> wFC2_r48_<[39:0]> wFC2_r49_<[39:0]> "
        "wFC2_r50_<[39:0]> wFC2_r51_<[39:0]> wFC2_r52_<[39:0]> wFC2_r53_<[39:0]> wFC2_r54_<[39:0]> "
        "wFC2_r55_<[39:0]> wFC2_r56_<[39:0]> wFC2_r57_<[39:0]> wFC2_r58_<[39:0]> wFC2_r59_<[39:0]> "
        "wFC2_r60_<[39:0]> wFC2_r61_<[39:0]> wFC2_r62_<[39:0]> wFC2_r63_<[39:0]> wFC2_r64_<[39:0]> "
        "wFC2_r65_<[39:0]> wFC2_r66_<[39:0]> wFC2_r67_<[39:0]> wFC2_r68_<[39:0]> wFC2_r69_<[39:0]> "
        "wFC2_r70_<[39:0]> wFC2_r71_<[39:0]> wFC2_r72_<[39:0]> wFC2_r73_<[39:0]> wFC2_r74_<[39:0]> "
        "wFC2_r75_<[39:0]> wFC2_r76_<[39:0]> wFC2_r77_<[39:0]> wFC2_r78_<[39:0]> wFC2_r79_<[39:0]> "
        "wFC2_r80_<[39:0]> wFC2_r81_<[39:0]> wFC2_r82_<[39:0]> wFC2_r83_<[39:0]> wFC2_r84_<[39:0]>\n\n"
        "tunit 1ns       ; (Optional) Set the time unit (e.g., 1 nanoseconds)\n\n"
        "trise 0.01 \t; 10 picoseconds\n\n"
        "tfall 0.01 \t; 10 picoseconds\n\n"
        "vih 1.2\n\n"
        "vil 0\n\n"
        "voh 1.2\n\n"
        "vol 0\n\n"
        "period 10 ; 100 MHz \n\n"
        "; Data start from here:\n"
    )
    
    # Combine header and data.
    output_content = header + data_line + "\n"
    
    # Write the content to a new vector file.
    output_filename = "weightFC2.vec"
    with open(output_filename, "w") as f:
        f.write(output_content)
    
    print(f"Conversion complete. Vector file saved as '{output_filename}'.")

if __name__ == "__main__":
    main()
