from pymongo import MongoClient
import twitter_webcrawler
import pprint
import json
import datetime
import re

def getData():
	targets = ["SenSanders", "HillaryClinton", "realDonaldTrump"]
	lista = []
	for t in targets:
		lista.extend(twitter_webcrawler.get_tweets_in_JSON_format(t))
	return lista

def storeBSON():
	json_data = json.dumps(getData())
	json_data2=json.loads(json_data)
	return json_data2

def connectionDB():
	return MongoClient('mongodb://localhost:27017/')

def createCollectionInDB():
	db = connectionDB()['1tweets']
	collection = db.my_collection
	return collection

def insertDB():
	col = createCollectionInDB()
	col.insert(storeBSON())

def getNbrOfDocuments():
	return createCollectionInDB().count()

def printNbrOfDocumentsFromSpecificUser(username):
	print(creareCollectionInDB().find({'username':username}).count())

def printTextFromDB():
	cursor = createCollectionInDB().find({'_id':{"$gt":6480, "$lt":6500}}, {'created_at':0, 'id_str':0, '_id':0, 'username':0})
	for c in cursor:
		print(c['text'])

def getTextInDocuments():
	cursor = createCollectionInDB().find({'_id':{"$gt":1, "$lt":getNbrOfDocuments()}}, {'created_at':0, 'id_str':0, '_id':0, 'username':0})
	return cursor

def getTweetsFromUser(username):
	cursor = createCollectionInDB().find({'username':username})
	return cursor

# insertDB()

