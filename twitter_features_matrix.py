import twitter_features
import twitter_preprocessing
import twitter_features
import numpy
from sklearn.preprocessing import normalize


def twitterFeaturesMatrix(processedTweets, tweetsPOSTAGGED):
	matrice = numpy.array([
		twitter_features.lexicalDiversityPerTweet(processedTweets),
	    twitter_features.wordQuantityPerTweet(processedTweets),
	    twitter_features.verbQuantityPerTweet(tweetsPOSTAGGED),
	    twitter_features.pronounQuantityPerTweet(tweetsPOSTAGGED),
	    twitter_features.adverbQuantityPerTweet(tweetsPOSTAGGED),
	    twitter_features.adjectiveQuantityPerTweet(tweetsPOSTAGGED),
	    twitter_features.exclusiveTermsQuantityPerTweet(tweetsPOSTAGGED),
	    twitter_features.nbrOfCharactersPerTweet(processedTweets),
	    twitter_features.averageWordLenPerTweet(processedTweets)
		])
	matrice_normalizata = normalize(matrice, norm = 'l1', axis=1)
	return matrice_normalizata


