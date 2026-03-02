import pandas as pd
import numpy as np

print("Loading dataset...")

data = pd.read_csv("dataset/cicids.csv")

print("Original Shape:", data.shape)

# Remove infinite values
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop missing values
data.dropna(inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

print("After Cleaning Shape:", data.shape)

# Save cleaned dataset
data.to_csv("dataset/cleaned_cicids.csv", index=False)

print("Cleaned dataset saved successfully!")