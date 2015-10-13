import pymongo
from dbco import*
import time 

articlesday = db.qdoc.find({'timestamp': {'$gte':time.time()-24*60*60}}).count()

print(articlesday)