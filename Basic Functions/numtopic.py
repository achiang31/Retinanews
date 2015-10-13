import pymongo
from dbco import*
import time 

numtopic = db.qdoc.find({'topic': 293}).count()

print(numtopic)

mkeyword = db.qdoc.find({'topic': 293})
print mkeyword[0].keys()
print(mkeyword)
