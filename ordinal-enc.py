# Applying ordinal-encoding on a cloth size datset

import pandas as pd
import numpy as np

dict1 = {
    'Size' : ['Small', 'Medium', 'Large', 'XL', 'XXL'],
    'ordinal-enc': []
}

# df = pd.DataFrame(dict1)
# print(df)

ordinalDict = {
    'Small' : 1,
    'Medium' : 2,
    'Large' : 3,
    'XL' : 4, 
    'XXL' : 5
}

for i in dict1['Size']:
    dict1['ordinal-enc'].append(ordinalDict[i])

df = pd.DataFrame(dict1)
print(df)