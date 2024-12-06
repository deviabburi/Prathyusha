import pandas as pd
import numpy as np

def clean_data():
    # Read the CSV file
    df = pd.read_csv('Assignment-7/PoliceKillingsUS.csv')
    
    # Make column names consistent (lowercase and replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Handle missing values
    # Fill missing age with median
    df['age'] = df['age'].fillna(df['age'].median())
    
    # Fill missing gender with 'Unknown'
    df['gender'] = df['gender'].fillna('Unknown')
    
    # Fill missing race with 'Unknown'
    df['race'] = df['race'].fillna('Unknown')
    
    # Fill missing city with 'Unknown'
    df['city'] = df['city'].fillna('Unknown')
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Remove any duplicate entries
    df = df.drop_duplicates()
    
    # Reset index after removing duplicates
    df = df.reset_index(drop=True)
    
    # Convert age to integer (round to nearest whole number)
    df['age'] = df['age'].round().astype(int)
    
    # Ensure state names are in uppercase
    df['state'] = df['state'].str.upper()
    
    # Save the cleaned dataset
    df.to_csv('Assignment-7/cleaned_police_killings.csv', index=False)
    
    return df

if __name__ == "__main__":
    cleaned_df = clean_data()
    print("Data cleaning completed successfully!")
    print(f"Dataset shape: {cleaned_df.shape}")
    print("\nSample of cleaned data:")
    print(cleaned_df.head())
