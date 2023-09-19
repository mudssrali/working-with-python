import pandas as pd
import numpy as np

# Create a Pandas Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Create a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}
df = pd.DataFrame(data)
print(df)

# Perform operations on DataFrame columns
df['Age'] += 1
print(df)

# Filter rows based on conditions
filtered_df = df[df['Age'] > 30]
print(filtered_df)