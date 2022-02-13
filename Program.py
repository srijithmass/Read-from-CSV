'''
Program to read contents from a csv file
Developed by: SRIJITH R
RegisterNumber: 21004191
'''

import pandas as pd
df=pd.read_csv('data.csv')
print(df.head(10))
print(df.tail(5))
print("Number of rows:",len(df.axes[0]))
print("Number of columns:",len(df.axes[1]))