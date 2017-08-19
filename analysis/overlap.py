import networkx as nx
import random
import csv
import itertools
import operator
import pickle


def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

name_sales = "sales/menpolotshirt_sales_pro.pickle"
name_returns = "returns/menpolotshirt_returns_pro.pickle"
file = open("overlap.txt","w")

G_sales=nx.read_gpickle(name_sales)
G_returns=nx.read_gpickle(name_returns)

l1 = G_sales.degree()
l2 = G_returns.degree()

sorted_l1 = list(sorted(l1.items(), key=operator.itemgetter(1)))
sorted_l1 = [x[0] for x in sorted_l1]
sorted_l2 = list(sorted(l2.items(), key=operator.itemgetter(1)))
sorted_l2 = [x[0] for x in sorted_l2]

sorted_l1 = chunkIt(sorted_l1,3)
sorted_l2 = chunkIt(sorted_l2,3)

file.write(str(float(len(set(sorted_l1[0]).intersection(set(sorted_l2[0]))))/(min(len(sorted_l1[0]),len(sorted_l2[0]))))+"\n")
file.write(str(float(len(set(sorted_l1[1]).intersection(set(sorted_l2[1]))))/(min(len(sorted_l1[1]),len(sorted_l2[1]))))+"\n")
file.write(str(float(len(set(sorted_l1[2]).intersection(set(sorted_l2[2]))))/(min(len(sorted_l1[2]),len(sorted_l2[2]))))+"\n")


clustering_coeff_nodes = nx.clustering(G_sales)
l1 = clustering_coeff_nodes
clustering_coeff_nodes = nx.clustering(G_returns)
l2 = clustering_coeff_nodes

sorted_l1 = list(sorted(l1.items(), key=operator.itemgetter(1)))
sorted_l1 = [x[0] for x in sorted_l1]
sorted_l2 = list(sorted(l2.items(), key=operator.itemgetter(1)))
sorted_l2 = [x[0] for x in sorted_l2]

sorted_l1 = chunkIt(sorted_l1,3)
sorted_l2 = chunkIt(sorted_l2,3)

file.write(str(float(len(set(sorted_l1[0]).intersection(set(sorted_l2[0]))))/(min(len(sorted_l1[0]),len(sorted_l2[0]))))+"\n")
file.write(str(float(len(set(sorted_l1[1]).intersection(set(sorted_l2[1]))))/(min(len(sorted_l1[1]),len(sorted_l2[1]))))+"\n")
file.write(str(float(len(set(sorted_l1[2]).intersection(set(sorted_l2[2]))))/(min(len(sorted_l1[2]),len(sorted_l2[2]))))+"\n")

centrality = nx.eigenvector_centrality(G_sales)
sorted_l1 = sorted(centrality.items(), key=operator.itemgetter(1))
centrality = nx.eigenvector_centrality(G_returns)
sorted_l2 = sorted(centrality.items(), key=operator.itemgetter(1))

sorted_l1 = [x[0] for x in sorted_l1]
sorted_l2 = [x[0] for x in sorted_l2]

sorted_l1 = chunkIt(sorted_l1,3)
sorted_l2 = chunkIt(sorted_l2,3)

file.write(str(float(len(set(sorted_l1[0]).intersection(set(sorted_l2[0]))))/(min(len(sorted_l1[0]),len(sorted_l2[0]))))+"\n")
file.write(str(float(len(set(sorted_l1[1]).intersection(set(sorted_l2[1]))))/(min(len(sorted_l1[1]),len(sorted_l2[1]))))+"\n")
file.write(str(float(len(set(sorted_l1[2]).intersection(set(sorted_l2[2]))))/(min(len(sorted_l1[2]),len(sorted_l2[2]))))+"\n")

file.close()