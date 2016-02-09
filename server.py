import flask
import pymongo
import random
import bson

app = flask.Flask(__name__)
mongodb_server = pymongo.MongoClient('mongodb://143.215.138.132:27017/')
db = mongodb_server.big_data


@app.route('/hi/<string:name>')
def say_hello(name):
    return 'Hello' + name

@app.route('/')
def index():
    # display 10 random sources
    sources = db.qdoc.distinct('source')
    subset = random.sample(sources, 10)
    return flask.render_template('sources.html', sources = subset)

@app.route('/articles/<string:source>')
def list_articles(source):
    # return articles that match the source
    articles = db.qdoc.find({'source' : source},
        projection = {'_id' : 1, 'title' : 1}, limit = 10)
    return flask.render_template('article_list.html', source = source,
        articles = articles)

@app.route('/article/<string:_id>')
def get_article(_id):
    object_id = bson.objectid.ObjectId(_id)
    article = db.qdoc.find_one({'_id' : object_id})
    # return the article that has the given id
    article['_id'] = str(article['_id'])
    return flask.render_template ('article.html', article = article)

@app.route('/chartdata')
def sources_chart_data():
    # use the mongodb aggregation framework to return the top 20 sources
    # with the most articles.
    group = {'$group' : {'_id' : '$source', 'total' : {'$sum' : 1}}}
    sort = {'$sort' : {'total' : -1}}
    limit = {'$limit' : 20}
    data = db.qdoc.aggregate([group, sort, limit])
    return flask.jsonify(data = list(data))


@app.route('/chart')
def chart():
    return flask.render_template('chart.html')

if __name__ == "__main__":
    app.debug = True
    app.run()


