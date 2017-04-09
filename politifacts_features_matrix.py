import politifacts_features
import politifacts_preprocessing
from sklearn.preprocessing import normalize
import numpy


myList = politifacts_preprocessing.makeNewData()

def featuresMatrix(myList):
	w = numpy.array([								#pune features pe linii
	    politifacts_features.lexicalDiversity(myList),
	    politifacts_features.wordQuantity(myList),
	    politifacts_features.verbQuantity(myList),
	    politifacts_features.pronounQuantity(myList),
	    politifacts_features.adverbQuantity(myList),
	    politifacts_features.adjectiveQuantity(myList),
	    politifacts_features.exclusiveTermsQuantity(myList),
	    politifacts_features.characterCountPerPhrase(myList),
	    politifacts_features.averageWordLengthPerPhrase(myList)])				
	w_normalized = normalize(w, norm='l1', axis=1)
	return w_normalized						#returneaza matricea cu valorile normalizate pentru liniile care reprezinta features

# print(featuresMatrix(myList).transpose())

