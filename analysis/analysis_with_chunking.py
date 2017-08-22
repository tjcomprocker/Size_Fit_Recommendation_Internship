import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import csv
import itertools
import operator

def avg(list):
	sum = 0
	for elm in list:
		sum += elm
	return (str(sum/(len(list)*1.0)))

name = "mencasualshoes_sales_data"
size_column_name = 'uk_india_size'

import pickle
from random import randint

file = open(name+"_analysis.txt","w")
file2 = open(name+"_edgelist.txt","w")

#df = pd.read_csv(name+".csv",sep="	")

users = set()
brands = {}
product_id = set()
G=nx.Graph()
bs = set()
sizes = set()
count = 0

chunksize = 10 ** 6
for df in pd.read_csv(name+".csv" , sep="	" , chunksize=chunksize):

	print (df.shape)

	for index,rows in df.iterrows():
		if str(rows['brand']).lower() == 'null' or str(rows[size_column_name]).lower() == 'null':
			continue
		product_id.add(rows['product_id'])
		users.add(rows['account_id'])
		count = count + 1
		if (str(rows['brand']).lower()).replace(" ","_") in brands.keys():
			brands[(str(rows['brand']).lower()).replace(" ","_")].add(str(rows[size_column_name]).lower())
			sizes.add(str(rows[size_column_name]).lower())
		else:
			brands[(str(rows['brand']).lower()).replace(" ","_")] = set()
			brands[(str(rows['brand']).lower()).replace(" ","_")].add(str(rows[size_column_name]).lower())
			sizes.add(str(rows[size_column_name]).lower())
		
		bs.add((str(rows['brand']).lower()).replace(" ","_")+";"+str(rows[size_column_name]).lower())
		if not (G.has_edge(rows['account_id'],str((str(rows['brand']).lower()).replace(" ","_")+";"+str(rows[size_column_name]).lower()))):
			G.add_edge(rows['account_id'],(str(rows['brand']).lower()).replace(" ","_")+";"+str(rows[size_column_name]).lower())

pickle.dump(G, open(name[:-5]+'_bi.pickle', 'w'))

print ("Rows Iterated: - "+str(count))
print ("Graph Created")

file.write(str(count)+"\n")
file.write(str(len(users))+"\n")
file.write(str(len(product_id))+"\n")
file.write(str(len(bs))+"\n")
file.write(str(len(brands))+"\n")
file.write(str(len(sizes))+"\n")
file.write(str(G.number_of_edges())+"\n")

l = list(G.degree(list(users)).values())

file.write(str(min(l))+"\n")
file.write(str(max(l))+"\n")
file.write(str(avg(l))+"\n")

l = list(G.degree(list(bs)).values())

file.write(str(min(l))+"\n")
file.write(str(max(l))+"\n")
file.write(str(avg(l))+"\n")

G2=nx.Graph()
bs = list(bs)

for pair in itertools.combinations(bs,2):
		temp = len(set(G.neighbors(pair[0])).intersection(G.neighbors(pair[1])))
		if temp > 0:
			if temp <= 10 and randint(1,100)>25:
				G2.add_edge(pair[0],pair[1],weight=temp)
			else:
				G2.add_edge(pair[0],pair[1],weight=temp)
			file2.write(str(bs.index(pair[0]))+" "+str(bs.index(pair[1]))+" "+str(temp)+"\n")

file2.close()
pickle.dump(G2, open(name[:-5]+'_pro.pickle', 'w'))
pickle.dump(bs, open(name[:-5]+'_bs.pickle', 'w'))

# l = list(G2.edges_iter(data='weight'))

# max_w = -1
# sum_w = 0
# for items in l:
# 	if items[2] > max_w:
# 		max_w = items[2]
# 	sum_w = sum_w + items[2]

# file.write(str(max_w)+"\n")
# file.write(str(sum_w/(len(l)*1.0))+"\n")

# file.write(str(G2.number_of_edges())+"\n")

# l = list(G2.degree().values())

# file.write(str(min(l))+"\n")
# file.write(str(max(l))+"\n")
# file.write(str(avg(l))+"\n")

# clustering_coeff_nodes = nx.clustering(G2)
# l = clustering_coeff_nodes.values()

# file.write(str(min(l))+"\n")
# file.write(str(max(l))+"\n")
# file.write(str(avg(l))+"\n")

# centrality = nx.eigenvector_centrality(G2)
# sorted_x = sorted(centrality.items(), key=operator.itemgetter(1),reverse=True)
# max_w = -1
# min_w = 100
# sum_w = 0
# for items in sorted_x:
# 	if items[1] > max_w:
# 		max_w = items[1]
# 	if items[1] < min_w:
# 		min_w = items[1]
# 	sum_w = sum_w + items[1]

# file.write(str(min_w)+"\n")
# file.write(str(max_w)+"\n")
# file.write(str(sum_w/(len(l)*1.0))+"\n")

# file.close()

