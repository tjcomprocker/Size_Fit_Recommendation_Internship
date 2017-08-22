import os
import glob

edgelist_files = glob.glob("*_edgelist.txt")

for edgelist_file in edgelist_files:
	os.system("mkdir "+edgelist_file[:-18])
	os.system("mkdir "+edgelist_file[:-18]+"/2")
	os.system("mkdir "+edgelist_file[:-18]+"/4")
	os.system("mkdir "+edgelist_file[:-18]+"/6")
	
	os.system("python select.py -n "+edgelist_file+" -p 2 -f temp -c 1")
	os.system("mv temp/* "+edgelist_file[:-18]+"/2/")
	os.system("rm -r temp")

	os.system("python select.py -n "+edgelist_file+" -p 4 -f temp -c 1")
	os.system("mv temp/* "+edgelist_file[:-18]+"/4/")
	os.system("rm -r temp")

	os.system("python select.py -n "+edgelist_file+" -p 6 -f temp -c 1")
	os.system("mv temp/* "+edgelist_file[:-18]+"/6/")
	os.system("rm -r temp")

	os.system("python community_overlap.py "+edgelist_file[:-18])