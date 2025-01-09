import pandas as pd

# File paths (update these paths to the location of your files)
contacts_file_path = "./output.csv"  # Path to contacts file
properties_file_path = "./Properties10years.csv"  # Path to properties file
output_file_path = "./Updated_Properties.csv"  # Path to save the updated properties file

# Load the CSV files
contacts_df = pd.read_csv(contacts_file_path)
properties_df = pd.read_csv(properties_file_path)

# Select relevant columns from the contacts file
contacts_columns = [
    "Address", "Phone", "SecondPhone", "PhoneExt", 
    "SecondPhoneExt", "Email", "FirstName", "LastName"
]
contacts_filtered = contacts_df[contacts_columns]

# Merge the properties file with the contacts file based on address
merged_df = properties_df.merge(
    contacts_filtered, 
    left_on="full_street_line",  # Column name in properties file
    right_on="Address",  # Column name in contacts file
    how="left", 
    suffixes=("", "_contact")
)

# Calculate the number of matches
num_matches = merged_df["Address"].notna().sum()
print(f"Number of matches found: {num_matches}")

# Update the properties dataframe with the contact details
for col in ["Phone", "SecondPhone", "PhoneExt", "SecondPhoneExt", "Email", "FirstName", "LastName"]:
    if f"{col}_contact" in merged_df:
        merged_df[col] = merged_df[col].combine_first(merged_df[f"{col}_contact"])

# Drop temporary columns and Address column from contacts
merged_df = merged_df.drop(columns=[f"{col}_contact" for col in contacts_columns if f"{col}_contact" in merged_df])
merged_df = merged_df.drop(columns=["Address"], errors="ignore")

# Save the updated properties dataframe to a new CSV file
merged_df.to_csv(output_file_path, index=False)

print(f"Updated properties file has been saved to {output_file_path}")
