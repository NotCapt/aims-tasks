# Applying imputation on house price datset

import pandas as pd
import numpy as np

dict1 = {
    'city' : ['Noida', 'Delhi', 'Pune', 'Ghaziabad', 'Mumbai', 'Gurgaon'],
    'Price' : [12e6, 1e7, 9e6, 5e6, 15e6, np.nan],
    'Bedrooms' : [2, 2, 3, 3, 2, 2]
}

df = pd.DataFrame(dict1)
#print(df)

# replacing gurgaon's price with the mean of other values
df.Price[5] = df.Price.mean()
#print(df.Price[5])

print(df)