import pymongo
from dbco import*

number_articles = db.qdoc.find().count()

print(number_articles) 