import pandas as pd
import numpy as np
import argparse

def voltage_to_int4(voltage):
    """
    Convert a voltage value to a 4-bit integer using a linear mapping.
    
    0.6 V corresponds to 0 and 0.7875 V corresponds to 15.
    The conversion is:
         INT4 = round(80 * (voltage - 0.6))
    and the result is clipped to the range [0, 15].
    """
    # Compute the raw value
    #int_value = np.round((15/(0.7875-0.6)) * (voltage - 0.6)).astype(int)
    int_value = np.round((15/(0.65-0.6)) * (voltage - 0.6)).astype(int)
    # Saturate the value to be within 0 and 15
    #int_value = np.clip(int_value, 0, 15)
    return int_value

def process_excel(input_file, output_file):
    # Read the Excel file into a DataFrame.
    # The first column is assumed to be the point number (untouched).
    df = pd.read_excel(input_file)
    
    # Create a copy of the dataframe for output
    df_result = df.copy()
    
    # Process columns starting from the second column.
    # Apply the conversion function to each value in the column.
    for col in df.columns[1:]:
        df_result[col] = df[col].apply(voltage_to_int4)
    
    # Save the converted DataFrame to a new Excel file.
    df_result.to_excel(output_file, index=False)
    print(f"Converted data saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert voltage data in an Excel sheet to INT4 values. "
                    "The first column is assumed to be point numbers, "
                    "and conversion starts from the second column."
    )
    parser.add_argument("input_file", help="Input Excel file (xlsx)")
    parser.add_argument("output_file", help="Output Excel file (xlsx)")
    args = parser.parse_args()
    
    process_excel(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
#python3.13 conv2_V2INT.py Conv2Outs.xlsx conv2Outs_INT4.xlsx