from homeharvest import scrape_property
from datetime import datetime
import pandas as pd

# Define the zip codes to scrape
zip_codes = ["17601", "17602", "17603", "17604", "17605", "17606", "17607", "17608"]
listing_type="sold"
# Define the starting and ending year
start_year = 2014
end_year = 2024

# Loop through each year and fetch data for all zip codes
for year in range(start_year, end_year):
    date_from = f"{year}-01-01"
    date_to = f"{year + 1}-01-01"
    print(f"Fetching data for the year {year} (from {date_from} to {date_to})")
    
    # Initialize a DataFrame for the current year
    year_properties = pd.DataFrame()
    
    for zip_code in zip_codes:
        print(f"Scraping properties for ZIP code: {zip_code}")
        try:
            properties = scrape_property(
                location=zip_code,
                listing_type=listing_type, 
                property_type=[
                    "single_family",
                    "multi_family",
                    "condos",
                    "condo_townhome_rowhome_coop",
                    "condo_townhome",
                    "townhomes",
                    "duplex_triplex",
                    "farm",
                    "land",
                    "mobile"
                ],
                date_from=date_from,
                date_to=date_to,
                extra_property_data=True,  
                limit=10000  
            )
            year_properties = pd.concat([year_properties, properties], ignore_index=True)
            print(f"Successfully fetched {len(properties)} properties for ZIP code: {zip_code}")
        except Exception as e:
            print(f"Failed to fetch data for ZIP code {zip_code}: {e}")
    
    # Generate a filename for the current year and save the results
    filename = f"{listing_type}_{year}.csv"
    year_properties.to_csv(filename, index=False)
    print(f"Data for the year {year} saved to {filename}")
    print(year_properties.head())
