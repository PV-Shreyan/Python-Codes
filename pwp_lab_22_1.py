# Write a code snippet to check the data types of each column in a DataFrame.

import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Age': [20, 25, 30],
    'Score': [88.5, 92.3, 79.8],
    'Passed': [True, False, True]
})

print(df.dtypes)
