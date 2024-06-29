import pandas as pd
from pathlib import Path
import chardet

def combine_csv_files(directory_path, output_file):
    # Create a Path object for the directory
    base_path = Path(directory_path)

    # List to hold dataframes
    dataframes = []

    # Iterate over each CSV file in subdirectories of the given directory
    for csv_file in base_path.rglob('*.csv'):
        # Read the current CSV file
        df = pd.read_csv(csv_file, encoding='shift_jis')
        # Append the dataframe to the list
        dataframes.append(df)

    # Concatenate all dataframes into a single dataframe
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(output_file, index=False, encoding='shift_jis')

    print(f"All CSV files have been combined into {output_file}")

# Example usage: Combine CSV files from 'wards' folder into 'combined.csv'
combine_csv_files('/app/data/wards', '/app/data/geolocation.csv')
