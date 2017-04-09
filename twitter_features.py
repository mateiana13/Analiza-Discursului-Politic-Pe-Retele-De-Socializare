import twitter_preprocessing
import string
import re
import mongoDB_for_tweets
from nltk import word_tokenize, sent_tokenize


punctuation = list(string.punctuation)


def lexicalDiversityPerTweet(processedTweets):			#preprocessedTweets
	diversity_score = []
	# for prop in my_text_data:
	for prop in processedTweets:
		word_count = len(word_tokenize(prop))
		vocab_size = len(set(word_tokenize(prop)))
		diversity_score.append(vocab_size / word_count)
	return diversity_score
# print(lexicalDiversityPerTweet(processedTweets))



def wordQuantityPerTweet(processedTweets):
	word_quantity = []
	# for prop in listaText:
	for prop in processedTweets:
		word_quantity.append(len(word_tokenize(prop)))
	return word_quantity
# print(wordQuantityPerTweet(processedTweets))


def verbQuantityPerTweet(tweetsPOSTAGGED):
	verb_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfVerbs = 0
		for i in item:
			if i[1] == "VB" or i[1] == "VBD" or i[1] == "VBG" or i[1] == "VBN" or i[1] == "VBP" or i[1] == "VBZ":
				nbrOfVerbs = nbrOfVerbs +1
		verb_quantity.append(nbrOfVerbs)
	return verb_quantity
# print(verbQuantityPerTweet(tweetsPOSTAGGED))



def pronounQuantityPerTweet(tweetsPOSTAGGED):
	pronoun_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfPronouns = 0
		for i in item:
			if i[1] == "PRP" or i[1] == "PRP$" or i[1] == "WP" or i[1] == "WP$":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(pronounQuantityPerTweet(tweetsPOSTAGGED))


def firstPersSingularPronounQuantityPerTweet(tweetsPOSTAGGED):
	pronoun_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfPronouns = 0
		for i in item:
			if i[0] == "i" or i[0] == "me" or i[0] == "mine" or i[0] == "my":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(firstPersSingularPronounQuantityPerTweet(tweetsPOSTAGGED))



def firstPersPluralPronounQuantityPerTweet(tweetsPOSTAGGED):
	pronoun_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfPronouns = 0
		for i in item:
			if i[0] == "we" or i[0] == "us" or i[0] == "our" or i[0] == "ours":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(firstPersPluralPronounQuantityPerTweet(tweetsPOSTAGGED))



def secondPersPronounQuantityPerTweet(tweetsPOSTAGGED):
	pronoun_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfPronouns = 0
		for i in item:
			if i[0] == "you" or i[0] == "your" or i[0] == "yours":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(secondPersPronounQuantityPerTweet(tweetsPOSTAGGED))



def thirdPersSingularPronounQuantityPerTweet(tweetsPOSTAGGED):
	pronoun_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfPronouns = 0
		for i in item:
			if i[0] == "he" or i[0] == "him" or i[0] == "his" or i[0] == "she" or i[0] == "her" or i[0] =="hers" or i[0] == "it" or i[0] == "its":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(thirdPersSingularPronounQuantityPerTweet(tweetsPOSTAGGED))



def thirdPersPluralPronounQuantityPerTweet(tweetsPOSTAGGED):
	pronoun_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfPronouns = 0
		for i in item:
			if i[0] == "they" or i[0] == "them" or i[0] == "their" or i[0] == "theirs":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(thirdPersPluralPronounQuantityPerTweet(tweetsPOSTAGGED))



def adverbQuantityPerTweet(tweetsPOSTAGGED):					#intra la modifiers
	adverb_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfAdverbs = 0
		for i in item:
			if i[1] == "RB" or i[1] == "RBR" or i[1] == "RBS":
				nbrOfAdverbs = nbrOfAdverbs +1
		adverb_quantity.append(nbrOfAdverbs)
	return adverb_quantity
# print(adverbQuantityPerTweet(tweetsPOSTAGGED))



def adjectiveQuantityPerTweet(tweetsPOSTAGGED):				#intra la modifiers
	adjective_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfAdjectives = 0
		for i in item:
			if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS":
				nbrOfAdjectives = nbrOfAdjectives +1
		adjective_quantity.append(nbrOfAdjectives)
	return adjective_quantity
# print(adjectiveQuantityPerTweet(tweetsPOSTAGGED))



def exclusiveTermsQuantityPerTweet(tweetsPOSTAGGED):				#but, except, without, exclude
	exclusive_terms_quantity = []
	for item in tweetsPOSTAGGED:
		nbrOfExclusiveTerms = 0
		for i in item:
			if i[0].lower() == "but" or i[0].lower() == "except" or i[0].lower() == "without" or i[0].lower() == "exclude":
				nbrOfExclusiveTerms = nbrOfExclusiveTerms +1
		exclusive_terms_quantity.append(nbrOfExclusiveTerms)
	return exclusive_terms_quantity
# print(exclusiveTermsQuantityPerTweet(tweetsPOSTAGGED))



def nbrOfCharactersPerTweet(processedTweets):
	character_count = []
	for prop in processedTweets:
		# print(prop)
		words = word_tokenize(prop)
		suma = 0
		for w in words:
			if w not in punctuation:
				suma = suma + len(w)
		character_count.append(suma)
	return character_count
# print(nbrOfCharactersPerTweet(processedTweets))



def averageWordLenPerTweet(processedTweets):					#raportul dintre lungimea tweet-ului(in caractere) si nr de cuvinte continute de tweet
	average_length = []
	for tweet in processedTweets:
		suma = 0
		words = word_tokenize(tweet)
		for word in words:
			suma = suma + len(word)
		average_length.append(suma/len(words))				
	return average_length
# print(averageWordLenPerTweet(processedTweets))

