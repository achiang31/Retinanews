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
	for (a,b,c,d) in (iden, title, source, keywords):
		temp = (a,b,c,d)
		nodes.append(temp)

#need a double for loop and if statement for the list of keywords from (list of tuples abcd) "nodes", in order to get ID numbers for articles w/ >3 keyword matches 
	edges = [] 
	for tup in nodes:
		for key in tup: 
			for word in key:
				num = []
				num.append(word) 
			if num == 
			
	edges.append(x,y)


#return nodes and edges (articles and connections)