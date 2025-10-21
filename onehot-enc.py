# applying one hot encoding on a color dataset
import pandas as pd
import numpy as np

dict1 = {
    'Color' : ['Red', 'Green', 'Blue']
}

df = pd.DataFrame(dict1)
#print(df)

#creating new columsn with dummy values
for i in df['Color']:
    df[i] = 0
#print(df)

#fitting the columns with actual values
for i in df.index:
    column = df.loc[i, 'Color']
    df.loc[i, column] = 1

print(df)