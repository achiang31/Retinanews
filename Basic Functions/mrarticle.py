import pymongo
from dbco import*
mrarticle = db.qdoc.find().sort('timestamp', pymongo.DESCENDING).limit(1)

print(mrarticle[0]['title'].encode('utf-8', 'ignore'))

t = mrarticle.type
print(t)