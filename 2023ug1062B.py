


import pandas as pd
import numpy as np

# Load the CSV file
file_path = '/Users/shivamkumar/Desktop/AQI_Data.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Extract the AQI column as a numpy array
aqi_values = data['AQI'].to_numpy()

# Calculate the mean, median, and standard deviation
aqi_mean = np.mean(aqi_values)
aqi_median = np.median(aqi_values)
aqi_std = np.std(aqi_values)

# Display the results
print(f"Mean AQI: {aqi_mean:.2f}")
print(f"Median AQI: {aqi_median:.2f}")
print(f"Standard Deviation of AQI: {aqi_std:.2f}")