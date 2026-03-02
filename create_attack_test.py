import pandas as pd

# Load cleaned dataset
data = pd.read_csv("dataset/cleaned_cicids.csv")

# Detect label column
label_column = data.columns[-1]

# Filter attack rows
attack_rows = data[data[label_column] != "BENIGN"]

# Drop label column and save only features
attack_rows.drop(label_column, axis=1).head(5).to_csv("attack_test.csv", index=False)

print("Attack test file created successfully!")