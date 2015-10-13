import json, pymongo
from dbco import*

def getArticlesWithKeywords(key):
    print(1)
    article = db.qdoc.find({'keywords': key}) 
    print(2)
    article = list(article)
    print(len(article))
    keywordList = []
    print(4)
    for a in article:
        print(5)
        return
        if key == a:
            print(6) 
            keywordList.extend(a['keywords'])
            print(7)
    	    print(article[0]['title'].encode('utf-8', 'ignore'))
            print(8)
        else: 
    	   print("last") 


getArticlesWithKeywords('greece')




"""
    Get articles who share at least one keyword with one of the keywords
        provided in the params.
        Params:
            keywords (list<str>):
                list of keywords to match
"""
    