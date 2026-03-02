import pandas as pd

# Load dataset
data = pd.read_csv("dataset/cicids.csv")

print("Dataset Loaded Successfully!")
print("Shape of dataset:", data.shape)
print("\nColumns:")
print(data.columns)
print("\nFirst 5 rows:")
print(data.head())