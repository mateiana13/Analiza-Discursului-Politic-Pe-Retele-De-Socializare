from pymongo import MongoClient
import politifacts_webcrawler

#verifies the if there's a connection to the mongo DB
def connectionDB():
	return MongoClient('mongodb://localhost:27017/')

#creates a collection in the mydb database named statementsCollection
def createCollectionOfStatements():
	db = connectionDB()['politifacts']
	collection = db.my_collection
	return collection

def insertStatements():
	col = createCollectionOfStatements()
	statements = politifacts_webcrawler.getAllStatements()
	col.insert(statements)


def getNbOfStatements():
	#print("number of items in collection %s" %(collection.count()))
	return createCollectionOfStatements().count()


def getTrueStatements():
	return createCollectionOfStatements().find({'ValoareDeAdevar':"True"})


def getFalseStatements():
	return createCollectionOfStatements().find({'ValoareDeAdevar':"False"})


def getNbOfTrueStatements():
	return createCollectionOfStatements().find({'ValoareDeAdevar':'True'}).count()


def getNbOfFalseStatements():
	return createCollectionOfStatements().find({'ValoareDeAdevar':'False'}).count()

def getTrueStatements():
	return createCollectionOfStatements().find({'ValoareDeAdevar':'True'},{'_id':0})

def getFalseStatements():
	return createCollectionOfStatements().find({'ValoareDeAdevar':'False'},{'_id':0})

def getTextForTrueStatements():
	cursor = createCollectionOfStatements().find({'ValoareDeAdevar':'True'},{'_id':0,'Sursa':0,'Id':0})
	return cursor


def getTextForFalseStatements():
	cursor = createCollectionOfStatements().find({'ValoareDeAdevar':'False'},{'_id':0, 'Sursa':0,'Id':0})
	return cursor


def getMeSpaces():
	for i in range(0,4):
		print()

