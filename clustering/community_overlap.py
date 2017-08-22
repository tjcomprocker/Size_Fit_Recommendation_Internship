import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score
import sys

def purity_score(clusters, classes):
	"""
	Calculate the purity score for the given cluster assignments and ground truth classes
	
	:param clusters: the cluster assignments array
	:type clusters: numpy.array
	
	:param classes: the ground truth classes
	:type classes: numpy.array
	
	:returns: the purity score
	:rtype: float
	"""
	
	A = np.c_[(clusters,classes)]

	n_accurate = 0.

	for j in np.unique(A[:,0]):
		z = A[A[:,0] == j, 1]
		x = np.argmax(np.bincount(z))
		n_accurate += len(z[z == x])

	return n_accurate / A.shape[0]

file1 = str(sys.argv[1])+"/2/results_1/tp"
file2 = str(sys.argv[1])+"/4/results_1/tp"
file3 = str(sys.argv[1])+"/6/results_1/tp"
file4 = open(str(sys.argv[1])+"/"+str(sys.argv[1])+"_nmi.txt",'w')

number_of_clusters1 = 0
number_of_clusters2 = 0
number_of_clusters3 = 0

cluster_output = []

with open(file1,"r") as f:
	content = f.readlines()
	for lines in content:
		cluster_output.append(map(int,(lines.split("	"))[:-1]))

possible_clusters = range(1,len(cluster_output)+1)
possible_clusters2 = range(1,len(cluster_output)+1)
number_of_clusters1 = len(cluster_output)

votes = [0]*(len(cluster_output)+1)

nodes = -1

for ls in cluster_output:
	if nodes < max(ls):
		nodes = max(ls)

ground_truth = [0]*(nodes+1)

temp = 1
for cluster in cluster_output:
	for node_in_cluster in cluster:
		ground_truth[node_in_cluster] = temp
	temp = temp + 1


cluster_output = []
with open(file2,"r") as f:
	content = f.readlines()
	for lines in content:
		cluster_output.append(map(int,(lines.split("	"))[:-1]))

number_of_clusters2 = len(cluster_output)

predicted = [0]*(nodes+1)

winning_cluster = -1
winning_votes = -1

for cluster in cluster_output:
	for node_in_cluster in cluster:
		votes[ground_truth[node_in_cluster]] = votes[ground_truth[node_in_cluster]] + 1

	for i in range(1,len(votes)):
		if votes[i] > winning_votes and i in possible_clusters:
			winning_cluster = i
			winning_votes = votes[i]
			possible_clusters.remove(i)

	if winning_cluster == -1 or len(possible_clusters) == 0:
		break

	for node_in_cluster in cluster:
		predicted[node_in_cluster] = winning_cluster

	winning_cluster = -1
	winning_votes = -1
	votes = [0]*len(votes)

print ("Purity: "+str(purity_score(np.array(predicted),np.array(ground_truth))))
print ("NMI: "+str(normalized_mutual_info_score(ground_truth,predicted)))
print ("ARI: "+str(adjusted_rand_score(ground_truth,predicted)))

file4.write (str(purity_score(np.array(predicted),np.array(ground_truth)))+"\n")
file4.write (str(normalized_mutual_info_score(ground_truth,predicted))+"\n")
file4.write (str(adjusted_rand_score(ground_truth,predicted))+"\n")

cluster_output = []
with open(file3,"r") as f:
	content = f.readlines()
	for lines in content:
		cluster_output.append(map(int,(lines.split(" "))[:-1]))

number_of_clusters3 = len(cluster_output)

predicted = [0]*(nodes+1)
votes = [0]*len(votes)

winning_cluster = -1
winning_votes = -1

for cluster in cluster_output:
	for node_in_cluster in cluster:
		votes[ground_truth[node_in_cluster]] = votes[ground_truth[node_in_cluster]] + 1

	for i in range(1,len(votes)):
		if votes[i] > winning_votes and i in possible_clusters2:
			winning_cluster = i
			winning_votes = votes[i]
			possible_clusters2.remove(i)

	if winning_cluster == -1 or len(possible_clusters2) == 0:
		break

	for node_in_cluster in cluster:
		predicted[node_in_cluster] = winning_cluster

	winning_cluster = -1
	winning_votes = -1
	votes = [0]*len(votes)

print ("Purity: "+str(purity_score(np.array(predicted),np.array(ground_truth))))
print ("NMI: "+str(normalized_mutual_info_score(ground_truth,predicted)))
print ("ARI: "+str(adjusted_rand_score(ground_truth,predicted)))

print ("-----------------------------------------------------------\n\n\n")


file4.write (str(purity_score(np.array(predicted),np.array(ground_truth)))+"\n")
file4.write (str(normalized_mutual_info_score(ground_truth,predicted))+"\n")
file4.write (str(adjusted_rand_score(ground_truth,predicted))+"\n")

file4.write (str(number_of_clusters1)+"\n")
file4.write (str(number_of_clusters2)+"\n")
file4.write (str(number_of_clusters3)+"\n")

file4.close()