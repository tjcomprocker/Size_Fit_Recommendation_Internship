import pickle

file1 = "sales/womenjean_sales_bs.pickle"
file2 = "returns/womenjean_returns_bs.pickle"

bs = list(pickle.load( open( file1, "rb" ) ))
bs2 = list(pickle.load( open( file2, "rb" ) ))

sales_clusters = []
temp = []
temp2 = []

split_str = "	"

with open("tp","r") as f:
	content = f.readlines()
	for lines in content:
		temp = map(int,(lines.split(split_str))[:-1])
		temp2 = []
		for items in temp:
			temp2.append(bs[items])
		sales_clusters.append(temp2)

returns_clusters = []

with open("tp 2","r") as f:
	content = f.readlines()
	for lines in content:
		temp = map(int,(lines.split(split_str))[:-1])
		temp2 = []
		for items in temp:
			temp2.append(bs2[items])
		returns_clusters.append(temp2)

i = 0
j = 0
result = []
for x in sales_clusters[:len(sales_clusters)/2]:
	for y in returns_clusters[:len(returns_clusters)/2]:
		result.append((len(set(x).intersection(y)),i,j))
		j = j + 1
	i = i + 1
	j = 0

result = sorted(result, key=lambda x: x[0], reverse=True)

print result[0:5]

for i in range(1,4):
	file3 = open(str(i)+"_1.txt","w")
	file4 = open(str(i)+"_2.txt","w")
	temp = sorted(sales_clusters[result[i-1][1]])
	temp2 = sorted(returns_clusters[result[i-1][2]])
	for nodes in temp:
		file3.write(str(nodes)+"\n")
	for nodes in temp2:
		file4.write(str(nodes)+"\n")

file3.close()
file4.close()

i = 0
j = 0
result = []
for x in sales_clusters[(len(sales_clusters)/2)+1:]:
	for y in returns_clusters[(len(returns_clusters)/2)+1:]:
		result.append((len(set(x).intersection(y)),i,j))
		j = j + 1
	i = i + 1
	j = 0

result = sorted(result, key=lambda x: x[0], reverse=True)

print result[0:5]

for i in range(4,7):
	file3 = open(str(i)+"_1.txt","w")
	file4 = open(str(i)+"_2.txt","w")
	temp = sorted(sales_clusters[result[i-4][1]])
	temp2 = sorted(returns_clusters[result[i-4][2]])
	for nodes in temp:
		file3.write(str(nodes)+"\n")
	for nodes in temp2:
		file4.write(str(nodes)+"\n")
file3.close()
file4.close()
