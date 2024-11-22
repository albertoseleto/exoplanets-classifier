import sys
import pandas as pd
from astropy.io.votable import parse

def vot_to_csv(vot_file, csv_file):
    # Parse the VOTable file
    votable = parse(vot_file)
    table = votable.get_first_table().to_table()

    # Convert the table to a pandas DataFrame
    df = table.to_pandas()

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f"Converted {vot_file} to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vot.py <input_vot_file> <output_csv_file>")
        sys.exit(1)

    input_vot_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    vot_to_csv(input_vot_file, output_csv_file)