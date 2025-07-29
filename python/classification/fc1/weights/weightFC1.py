#!/usr/bin/env python3
import numpy as np

def convert_to_4bit(value):
    """
    Convert a signed integer (range 0 to 7 in magnitude) to a 4-bit digital representation.
    For zero, return "1000".
    For nonzero:
      - The MSB is "1" if the value is positive and "0" if negative.
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
    # Load the weight data from the npy file; expected shape is (120, 84)
    weights = np.load("weightFC1.npy")
    
    # Process each row: convert each element to its 4-bit representation,
    # then concatenate the 84 converted values to form a 336-bit digital word.
    digital_words = []
    for row in weights:
        # Convert each weight in the row to a 4-bit string
        converted_row = [convert_to_4bit(int(val)) for val in row]
        # Concatenate the 84 4-bit values (without separator)
        digital_word = "".join(converted_row)
        digital_words.append(digital_word)
    
    # Join all 120 digital words with a single space
    data_line = " ".join(digital_words)
    
    # Vector file header as provided:
    header = (
        "; Digital Vector File Header for wFC1_r1_<[335:0]> to wFC1_r120_<[335:0]>\n\n"
        "radix 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\n\n"
        "io    iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\n\n"
        "vname wFC1_r1_<[335:0]> wFC1_r2_<[335:0]> wFC1_r3_<[335:0]> wFC1_r4_<[335:0]> wFC1_r5_<[335:0]> wFC1_r6_<[335:0]> wFC1_r7_<[335:0]> wFC1_r8_<[335:0]> wFC1_r9_<[335:0]> wFC1_r10_<[335:0]> "
        "wFC1_r11_<[335:0]> wFC1_r12_<[335:0]> wFC1_r13_<[335:0]> wFC1_r14_<[335:0]> wFC1_r15_<[335:0]> wFC1_r16_<[335:0]> wFC1_r17_<[335:0]> wFC1_r18_<[335:0]> wFC1_r19_<[335:0]> wFC1_r20_<[335:0]> "
        "wFC1_r21_<[335:0]> wFC1_r22_<[335:0]> wFC1_r23_<[335:0]> wFC1_r24_<[335:0]> wFC1_r25_<[335:0]> wFC1_r26_<[335:0]> wFC1_r27_<[335:0]> wFC1_r28_<[335:0]> wFC1_r29_<[335:0]> wFC1_r30_<[335:0]> "
        "wFC1_r31_<[335:0]> wFC1_r32_<[335:0]> wFC1_r33_<[335:0]> wFC1_r34_<[335:0]> wFC1_r35_<[335:0]> wFC1_r36_<[335:0]> wFC1_r37_<[335:0]> wFC1_r38_<[335:0]> wFC1_r39_<[335:0]> wFC1_r40_<[335:0]> "
        "wFC1_r41_<[335:0]> wFC1_r42_<[335:0]> wFC1_r43_<[335:0]> wFC1_r44_<[335:0]> wFC1_r45_<[335:0]> wFC1_r46_<[335:0]> wFC1_r47_<[335:0]> wFC1_r48_<[335:0]> wFC1_r49_<[335:0]> wFC1_r50_<[335:0]> "
        "wFC1_r51_<[335:0]> wFC1_r52_<[335:0]> wFC1_r53_<[335:0]> wFC1_r54_<[335:0]> wFC1_r55_<[335:0]> wFC1_r56_<[335:0]> wFC1_r57_<[335:0]> wFC1_r58_<[335:0]> wFC1_r59_<[335:0]> wFC1_r60_<[335:0]> "
        "wFC1_r61_<[335:0]> wFC1_r62_<[335:0]> wFC1_r63_<[335:0]> wFC1_r64_<[335:0]> wFC1_r65_<[335:0]> wFC1_r66_<[335:0]> wFC1_r67_<[335:0]> wFC1_r68_<[335:0]> wFC1_r69_<[335:0]> wFC1_r70_<[335:0]> "
        "wFC1_r71_<[335:0]> wFC1_r72_<[335:0]> wFC1_r73_<[335:0]> wFC1_r74_<[335:0]> wFC1_r75_<[335:0]> wFC1_r76_<[335:0]> wFC1_r77_<[335:0]> wFC1_r78_<[335:0]> wFC1_r79_<[335:0]> wFC1_r80_<[335:0]> "
        "wFC1_r81_<[335:0]> wFC1_r82_<[335:0]> wFC1_r83_<[335:0]> wFC1_r84_<[335:0]> wFC1_r85_<[335:0]> wFC1_r86_<[335:0]> wFC1_r87_<[335:0]> wFC1_r88_<[335:0]> wFC1_r89_<[335:0]> wFC1_r90_<[335:0]> "
        "wFC1_r91_<[335:0]> wFC1_r92_<[335:0]> wFC1_r93_<[335:0]> wFC1_r94_<[335:0]> wFC1_r95_<[335:0]> wFC1_r96_<[335:0]> wFC1_r97_<[335:0]> wFC1_r98_<[335:0]> wFC1_r99_<[335:0]> wFC1_r100_<[335:0]> "
        "wFC1_r101_<[335:0]> wFC1_r102_<[335:0]> wFC1_r103_<[335:0]> wFC1_r104_<[335:0]> wFC1_r105_<[335:0]> wFC1_r106_<[335:0]> wFC1_r107_<[335:0]> wFC1_r108_<[335:0]> wFC1_r109_<[335:0]> wFC1_r110_<[335:0]> "
        "wFC1_r111_<[335:0]> wFC1_r112_<[335:0]> wFC1_r113_<[335:0]> wFC1_r114_<[335:0]> wFC1_r115_<[335:0]> wFC1_r116_<[335:0]> wFC1_r117_<[335:0]> wFC1_r118_<[335:0]> wFC1_r119_<[335:0]> wFC1_r120_<[335:0]>\n\n"
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
    
    # Combine header and data line
    output_content = header + data_line + "\n"
    
    # Write the vector file
    output_filename = "weightFC1.vec"
    with open(output_filename, "w") as f:
        f.write(output_content)
    
    print(f"Conversion complete. Vector file saved as '{output_filename}'.")

if __name__ == "__main__":
    main()
