import pandas as pd
import random
import csv
import itertools
import operator
import pickle

name = "menpolotshirt_returns_data"
size_column_name = 'size'

import pickle
from random import randint

df = pd.read_csv(name+".csv",sep="	",usecols=range(0,27))

print ("Reading CSV Completed")

print (df.shape)

brands = {}
bs = set()
sizes = set()

for index,rows in df.iterrows():
    if str(rows['brand']).lower() == 'null' or str(rows[size_column_name]).lower() == 'null':
        continue

    if (str(rows['brand']).lower()).replace(" ","_") in brands.keys():
        brands[(str(rows['brand']).lower()).replace(" ","_")].add(str(rows[size_column_name]).lower())
        sizes.add(str(rows[size_column_name]).lower())
    else:
        brands[(str(rows['brand']).lower()).replace(" ","_")] = set()
        brands[(str(rows['brand']).lower()).replace(" ","_")].add(str(rows[size_column_name]).lower())
        sizes.add(str(rows[size_column_name]).lower())
    
    bs.add((str(rows['brand']).lower()).replace(" ","_")+";"+str(rows[size_column_name]).lower())

pickle.dump(bs, open(name[:-5]+'_bs.pickle', 'w'))