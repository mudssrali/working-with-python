import pandas as pd

# Creating data frame
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)

# Perform data merging and joining
data1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value': [1, 2, 3]})
data2 = pd.DataFrame({'Key': ['B', 'C', 'D'], 'Value': [4, 5, 6]})

merged_data = pd.merge(data1, data2, on='Key', how='inner')

print(merged_data)