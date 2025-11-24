# Draw the violin plot with Pandas.

import pandas as pd
import seaborn as sns

# initialise data of lists
data = {'Name': ['Mohe', 'Karnal', 'Yrik', 'Jack'],
        'Age': [30, 21, 29, 28]}

df = pd.DataFrame(data)
sns.violinplot(data['Age'])
