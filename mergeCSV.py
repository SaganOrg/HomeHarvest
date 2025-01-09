import pandas as pd
import os

# Directory containing the CSV files
csv_directory = './files'

# Output file name
output_file = 'Properties10years.csv'

# List to hold DataFrames
dataframes = []

# Iterate through all files in the directory
for file in os.listdir(csv_directory):
    if file.endswith('.csv'):
        file_path = os.path.join(csv_directory, file)
        # Read the CSV file into a DataFrame and append to the list
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Concatenate all DataFrames
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a CSV file
merged_df.to_csv(output_file, index=False)

print(f'Merged CSV file saved as {output_file}')
