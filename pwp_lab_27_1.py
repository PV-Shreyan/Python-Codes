# Visualize the data with a box plot and pandas:

import pandas as pd
import seaborn as sns

# initialise data of lists
data = {'Name': ['Mohe', 'Karnal', 'Yrik', 'Jack'],
        'Age': [30, 21, 29, 28]}

df = pd.DataFrame(data)
sns.boxplot(data['Age'])
