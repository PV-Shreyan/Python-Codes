# Write a code snippet that demonstrates how to fill missing values with the mean of a column.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, np.nan]
})

df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
