import politifacts_preprocessing
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize




lista = politifacts_preprocessing.makeNewData()



def lexicalDiversity(lista):					#raportul dintre nr de cuvinte din propozitie si nr de cuvinte unice din propozitie

	my_text_data = politifacts_preprocessing.removePunctuationFromText(lista)
	diversity_score = []
	for prop in my_text_data:
		word_count = len(word_tokenize(prop))
		vocab_size = len(set(word_tokenize(prop)))
		diversity_score.append(vocab_size / word_count)
	return diversity_score
# print(lexicalDiversity(lista))


def characterCountPerPhrase(lista):
	my_text_data = politifacts_preprocessing.removePunctuationFromText(lista)
	character_count = []
	for prop in my_text_data:
		lungimeProp = 0
		for word in word_tokenize(prop):
			lungimeProp = lungimeProp + len(word)
		character_count.append(lungimeProp)
	return character_count
# print(characterCountPerPhrase(lista))



def wordQuantity(lista):
	word_quantity = []
	for prop in lista:
		word_quantity.append(len(word_tokenize(prop[0])))
	return word_quantity
# print(wordQuantity(lista))



def averageWordLengthPerPhrase(lista):			#raportul dintre lungimea frazei(in caractere) si nr de cuvinte continute de fraza
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	average_length = []
	for prop in listaText:
		suma = 0
		for word in prop[0]:
			suma = suma + len(word[0])
		average_length.append(suma/len(prop[0]))
	return average_length
# print(averageWordLengthPerPhrase(lista))



def verbQuantity(lista):
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	verb_quantity = []
	for item in listaText:
		nbrOfVerbs = 0
		for i in item[0]:
			if i[1] == "VB" or i[1] == "VBD" or i[1] == "VBG" or i[1] == "VBN" or i[1] == "VBP" or i[1] == "VBZ":
				nbrOfVerbs = nbrOfVerbs +1
		verb_quantity.append(nbrOfVerbs)
	return verb_quantity
# print(verbQuantity(lista))


def pronounQuantity(lista):
	# listaText = cleaningTextData(makenewdata(trueOrFalseST))
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	pronoun_quantity = []
	for item in listaText:
		nbrOfPronouns = 0
		for i in item[0]:
			if i[1] == "PRP" or i[1] == "PRP$" or i[1] == "WP" or i[1] == "WP$":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(pronounQuantity(lista))


def firstPersonSingularPronounsQuantity(lista):
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	pronoun_quantity = []
	for item in listaText:
		nbrOfPronouns = 0
		for i in item[0]:
			if i[0] == "i" or i[0] == "me" or i[0] == "my" or i[0] == "mine":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity

# print(firstPersonSingularPronounsQuantity(lista))


def firstPersonPluralPronounsQuantity(lista):
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	pronoun_quantity = []
	for item in listaText:
		nbrOfPronouns = 0
		for i in item[0]:
			if i[0] == "we" or i[0] == "us" or i[0] == "our" or i[0] == "ours":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(firstPersonPluralPronounsQuantity(lista))


def secondPersonPronounQuantity(lista):
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	pronoun_quantity = []
	for item in listaText:
		nbrOfPronouns = 0
		for i in item[0]:
			if i[0] == "you" or i[0] == "your" or i[0] == "yours":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(len(secondPersonPronounQuantity(lista)))


def thirdPersonSingularPronounQuantity(lista):
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	pronoun_quantity = []
	for item in listaText:
		nbrOfPronouns = 0
		for i in item[0]:
			if i[0] == "he" or i[0] == "him" or i[0] == "his" or i[0] == "she" or i[0] == "her" or i[0] == "hers" or i[0] == "it" or i[0] == "its":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(len(thirdPersonSingularPronounQuantity(lista)))


def thirdPersonPluralPronounQuantity(lista):
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	pronoun_quantity = []
	for item in listaText:
		nbrOfPronouns = 0
		for i in item[0]:
			if i[0] == "they" or i[0] == "their" or i[0] == "theirs" or i[0] == "them":
				nbrOfPronouns = nbrOfPronouns +1
		pronoun_quantity.append(nbrOfPronouns)
	return pronoun_quantity
# print(len(thirdPersonPluralPronounQuantity(lista)))


def adverbQuantity(lista):					#intra la modifiers
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	adverb_quantity = []
	for item in listaText:
		nbrOfAdverbs = 0
		for i in item[0]:
			if i[1] == "RB" or i[1] == "RBR" or i[1] == "RBS":
				nbrOfAdverbs = nbrOfAdverbs +1
		adverb_quantity.append(nbrOfAdverbs)
	return adverb_quantity
# print(len(adverbQuantity(lista)))


def adjectiveQuantity(lista):				#intra la modifiers
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	adjective_quantity = []
	for item in listaText:
		nbrOfAdjectives = 0
		for i in item[0]:
			if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS":
				nbrOfAdjectives = nbrOfAdjectives +1
		adjective_quantity.append(nbrOfAdjectives)
	return adjective_quantity
# print(len(adjectiveQuantity(lista)))


def exclusiveTermsQuantity(lista):				#but, except, without, exclude
	listaText = politifacts_preprocessing.cleaningTextData(lista)
	exclusive_terms_quantity = []
	for item in listaText:
		nbrOfExclusiveTerms = 0
		for i in item[0]:
			if i[0].lower() == "but" or i[0].lower() == "except" or i[0].lower() == "without" or i[0].lower() == "exclude":
				nbrOfExclusiveTerms = nbrOfExclusiveTerms +1
		exclusive_terms_quantity.append(nbrOfExclusiveTerms)
	return exclusive_terms_quantity
# print(exclusiveTermsQuantity(lista))


def getValoareAdevar(lista):
	valoareAdevar = []
	for prop in lista:
		if prop[1] == "True": 				#codific valoarea "True" prin 1 si "False" prin 0
			valoareAdevar.append(1)
		else:
			valoareAdevar.append(0)
	return valoareAdevar
# print(getValoareAdevar(lista))


