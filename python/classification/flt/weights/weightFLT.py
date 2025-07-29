#!/usr/bin/env python3
import numpy as np

def convert_to_4bit(value):
    """
    Convert an integer weight to its 4-bit digital representation:
    - For 0, return "1000".
    - For nonzero values:
        * The first (MSB) bit is "1" if positive, "0" if negative.
        * The remaining 3 bits represent the absolute value in binary.
    Assumes that |value| <= 7.
    """
    if value == 0:
        return "1000"
    sign_bit = "1" if value > 0 else "0"
    magnitude = abs(value)
    if magnitude > 7:
        raise ValueError(f"Value {value} is out of allowed range (absolute value must be <= 7).")
    mag_bits = format(magnitude, '03b')
    return sign_bit + mag_bits

def main():
    # Load the weight data from the npy file (expected shape: 288 x 120)
    weights = np.load("weightFLT.npy")
    
    digital_words = []
    for row in weights:
        # Convert each weight in the row to a 4-bit string
        converted = [convert_to_4bit(int(val)) for val in row]
        # Concatenate the 120 4-bit values to form a 480-bit digital word
        digital_word = "".join(converted)
        digital_words.append(digital_word)
    
    # Join all 288 digital words with a single space (no line breaks)
    data_line = " ".join(digital_words)
    
    # Construct the vector file header with placeholder values for radix and io.
    header = (
        "; Digital Vector File Header for wFLT_r1_<[479:0]> to wFLT_r288_<[479:0]>\n\n"
        "radix <placeholder> ; Replace with appropriate radix information\n\n"
        "io    <placeholder> ; Replace with appropriate io values\n\n"
        "vname wFLT_r1_<[479:0]> wFLT_r2_<[479:0]> wFLT_r3_<[479:0]> ... wFLT_r288_<[479:0]>\n\n"
        "tunit 1ns       ; (Optional) Set the time unit (e.g., 1 nanosecond)\n\n"
        "trise 0.01 \t; 10 picoseconds\n\n"
        "tfall 0.01 \t; 10 picoseconds\n\n"
        "vih 1.2\n\n"
        "vil 0\n\n"
        "voh 1.2\n\n"
        "vol 0\n\n"
        "period 10 ; 100 MHz \n\n"
        "; Data start from here:\n"
    )
    
    # Combine the header and the data line
    output_content = header + data_line + "\n"
    
    # Write the result to a vector file
    output_filename = "weightFLT.vec"
    with open(output_filename, "w") as f:
        f.write(output_content)
    
    print(f"Conversion complete. Vector file saved as '{output_filename}'.")

if __name__ == "__main__":
    main()
