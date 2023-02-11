import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = {'name':['Xamil','Anan','Janna','Vi','Rayu','Aval','Nuri'],
        'city':['mardin','traabzon','prag','samsun','mayamezkoy','corum','ordu'],
'age':['41','28','33','35','47','40','50'],
'py-score':['50.0','75.1','56.7','99.8','11.2','1.2','90.9']
}
#row_labels refers to a list that contains the labels of the rows, which are numbers ranging from 101 to 107.
row_labels=[101,102,103,104,105,106,107]

df = pd.DataFrame(data=data, index=row_labels)
print(df)
#use .head() to show the first few items and .tail() to show the last few items
#df.head(n=2) first two items
#df.tail(n=2) last two items
cities = df['city']
print(cities)
print()
#cities[102]  city in the row number of 102
#.loc[] gives the information about row number entered
onezerofive = df.loc[105]
print(onezerofive)