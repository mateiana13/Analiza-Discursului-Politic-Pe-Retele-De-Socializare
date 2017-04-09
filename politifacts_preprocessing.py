from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pymongo import MongoClient
from nltk import pos_tag
import nltk
import mongoDB_for_politifacts
import string
import re
import random
from nltk.stem.snowball import SnowballStemmer




my_stop_words_list = ['in', 'on','what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 
'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 
'very', '\s', '\t', 'can', 'will', 'just', 'don', 'should', 'now', '\d', '\ll', '\m', 'o', '\re', '\ve', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 
'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', '!', '"', '#', '$', '%', '&', "'", '(', ')', 
'*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'rt', 'via']


#datele cu care lucrez
trueSt = mongoDB_for_politifacts.getTrueStatements()[:550]
falseSt = mongoDB_for_politifacts.getFalseStatements()[:550]


punctuation = list(string.punctuation)


def corpus():
	corpus = []
	for i in trueSt:
		corpus.append((i['Text'], i['ValoareDeAdevar']))
	for i in falseSt:
		corpus.append((i['Text'], i['ValoareDeAdevar']))
	return corpus
# print(corpus())


my_corpus = []
def shuffleCorpus():
	my_corpus = corpus()
	random.shuffle(my_corpus)
	return my_corpus


shuffledData = shuffleCorpus()
# print(shuffledData)


def makeNewData():					#scoate ghilimele din text
	train = []
	for i in shuffledData:
		textnou=i[0].replace('"',"")
		train.append((textnou.lower(),i[1]))
	return train
# print(makeNewData())


def textCorpus():
	text = []
	for item in makeNewData():
		text.append(item[0])
	return text
# print(textCorpus())



def mergeStatementsData():							#ia toate cele 1100 de declaratii(si false si true)
	return makeNewData()
# print(mergeStatementsData())


exclude = set(string.punctuation)

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

stemmer = SnowballStemmer("porter")


def removePunctuationFromText(listaMesaje):
	celula = []
	for mesaj in listaMesaje:
		ValoareDeAdevar = mesaj[1]
		mesaj = test_set(mesaj[0])
		words = word_tokenize(mesaj)						#separ fraza in cuvinte(fiind vorba de mesaje scurte nu ma intereseaza si separarea pe propozitii)
		cuvinte = []
		# recomposedString = []
		for word in words:
			if word.lower() not in my_stop_words_list:
				if word.isalpha():							#scot toate numerele din text(nu ia si "six", "ten", etc.)
					cuvinte.append(stemmer.stem(word))	
		celula.append(' '.join(c for c in cuvinte))
	return celula

# print(removePunctuationFromText(makeNewData()))


def cleaningTextData(listaMesaje):
	celula = []
	for mesaj in listaMesaje:
		ValoareDeAdevar = mesaj[1]
		mesaj = test_set(mesaj[0])							#scot punctuatia din fraze
		words = word_tokenize(mesaj)						#separ fraza in cuvinte(fiind vorba de mesaje scurte nu ma intereseaza si separarea pe propozitii)
		cuvinte = []
		for word in words:
			if word.lower() not in my_stop_words_list:
				if word.isalpha():							#scot toate numerele din text(nu ia si "six", "ten", etc.)
					cuvinte.append(stemmer.stem(word))		#stemming pe cuvinte(o metoda de reducere a dimensionalitatii...necesara???)
		celula.append((pos_tag(cuvinte), ValoareDeAdevar))	#partile de vorbire
	return celula
# print(cleaningTextData(makeNewData()))
