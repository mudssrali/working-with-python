import pandas as pd

# Read data from a CSV file
data = pd.read_csv("data.csv")

# Display the first few rows of the DataFrame
print(data.head())

# Perform data aggregation
grouped_data = data.groupby("student_status").sum()
print(grouped_data)

# Filter rows based on conditions
filtered_data = data[data["std_gender"] == "FEMALE"]
print(filtered_data)