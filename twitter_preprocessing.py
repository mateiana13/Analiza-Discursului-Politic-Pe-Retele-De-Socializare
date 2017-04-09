import mongoDB_for_tweets
import re
import string
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk import pos_tag


my_stop_words_list = ['in', 'on','what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 
'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 
'very', '\s', '\t', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 
'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', '!', '"', '#', '$', '%', '&', "'", '(', ')', 
'*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'rt', 'via']




def getTweets(username):
	collection = mongoDB_for_tweets.getTweetsFromUser(username)
	tweets = []
	for c in collection:
		tweets.append(' '.join(re.sub("(#\w+)|(http)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(u\d+)|(RT)|(n\d+)|(U000+)"," ",str(c['text'])).split()))
	return tweets


stemmer = SnowballStemmer("porter")
punctuation = list(string.punctuation)
exclude = set(string.punctuation)

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

def POSTAGTwitterData(tweetsList):
	celula = []
	for mesaj in tweetsList:
		mesaj = test_set(mesaj)
		words = word_tokenize(mesaj)
		cuvinte = []
		for word in words:
			if word.lower() not in my_stop_words_list:
				if word.isalpha():
					cuvinte.append(stemmer.stem(word))
		celula.append(pos_tag(cuvinte))
	return celula

def removePunctuationFromText(tweetsList):
	mesaje = []
	for tweet in tweetsList:
		tweet = test_set(tweet)
		words = word_tokenize(tweet.lower())						#separ fraza in cuvinte(fiind vorba de mesaje scurte nu ma intereseaza si separarea pe propozitii)
		cuvinte = []
		for word in words:
			if word.lower() not in my_stop_words_list:
				if word.isalpha():
					cuvinte.append(stemmer.stem(word))
		mesaje.append(' '.join(c for c in cuvinte))
	return mesaje

def finalProcess(tweetsList):
	new=[]
	y=removePunctuationFromText(tweetsList)
	for i in y:
		if len(i)!=0:
			new.append(i)
	return new
