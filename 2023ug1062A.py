

import pandas as pd

# Load the CSV file
file_path = '/Users/shivamkumar/Desktop/AQI_Data.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Check for missing values
print("Missing values before replacement:")
print(data.isnull().sum())

# Replace missing values in numeric columns with the column mean
numeric_columns = data.select_dtypes(include='number').columns
data[numeric_columns] = data[numeric_columns].apply(lambda col: col.fillna(col.mean()))

# Print the updated DataFrame
print("\nMissing values after replacement:")
print(data.isnull().sum())

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(data)