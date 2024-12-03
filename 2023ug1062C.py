


import pandas as pd
import numpy as np

# Load the dataset
file_path = '/Users/shivamkumar/Desktop/AQI_Data.csv' 
data = pd.read_csv(file_path)

# Task A: Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Task B: Display the last 6 rows of the dataset
print("\nLast 6 rows of the dataset:")
print(data.tail(6))

# Task C: Show the summary statistics for all numeric columns
print("\nSummary statistics for all numeric columns:")
print(data.describe())

# Task D: Compute the mean AQI, PM2.5, and PM10 values for each city
mean_values_per_city = data.groupby('City')[['AQI', 'PM2.5', 'PM10']].mean()
print("\nMean AQI, PM2.5, and PM10 values for each city:")
print(mean_values_per_city)