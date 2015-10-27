import pymongo 
#read the pymongo tutorial 
from dbco import*
import time

def graphBuilder(start, end): 
	nodes = []
	iden = list(db.qdoc.find({'timestamp': {'$gte':int(startTime)-int(endTime)}}))  			#insert appropriate functon from pymongo
	title = list(db.qdoc.find({'timestamp': {'$gte':int(startTime)-int(endTime)}}))  			#insert appropriate functon from pymongo
	source = list(db.qdoc.find({'timestamp': {'$gte':int(startTime)-int(endTime)}}).source) 	#insert appropriate functon from pymongo
	keywords = list(db.qdoc.find({'timestamp': {'$gte':int(startTime)-int(endTime)}}).keywords)  			#insert appropriate functon from pymongo
	#asuuming keywords are in a list, in the list of keywords 
	ind = min(iden, title, source, keywords)
	for x in len(range(ind)):
		temp = (iden[x],title[x],source[x],keywords[x])
		nodes.append(temp)

#need a double for loop and if statement for the list of keywords from (list of tuples abcd) "nodes", in order to get ID numbers for articles w/ >3 keyword matches 
	edges = [] 
	bank = []
	bbank = []
	pmatch = []
	pairs = []
	for tup in nodes:
		bank.append(tup[3])
	for tup in bank:
		for key in tup:
			bbank.append(key)
	for key in bbank:
		num = bbank.count(key)
		if num > 2: 
			pmatch.append(key)
	for p in pmatch:
		for tup in nodes:
			if p in tup[3] :
				pairs.append(tup[0]) 
	for i in len(range(pairs)): 
		edges.append((pairs[i],pairs[i+1]))
	return edges 

	'''bank = []
	for tup in nodes: 
		bank.append(tup[3])
	for alist in bank: 
		for key in len(range(alist)):
			bank1 = bank[:]
			bank1.remove(alist) 
			if alist[key] in bank1[] 
				alist2 = alist1[:]
				alist2.remove()'''
#return nodes and edges (articles and connections)