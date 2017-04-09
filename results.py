import twitter_preprocessing
import twitter_features_matrix
import classifiers
import grafice
import numpy


#date de lucru
def getMatrixHC():
	tweetsListHC = twitter_preprocessing.getTweets('HillaryClinton')
	processedTweetsHC = twitter_preprocessing.finalProcess(tweetsListHC)
	tweetsPOSTAGGED_HC = twitter_preprocessing.POSTAGTwitterData(processedTweetsHC)
	tweetsHC = twitter_features_matrix.twitterFeaturesMatrix(processedTweetsHC,tweetsPOSTAGGED_HC).transpose()
	return tweetsHC

def getMatrixDT():
	tweetsListDT = twitter_preprocessing.getTweets('realDonaldTrump')
	processedTweetsDT = twitter_preprocessing.finalProcess(tweetsListDT)
	tweetsPOSTAGGED_DT = twitter_preprocessing.POSTAGTwitterData(processedTweetsDT)
	tweetsDT = twitter_features_matrix.twitterFeaturesMatrix(processedTweetsDT,tweetsPOSTAGGED_DT).transpose()
	return tweetsDT

def getMatrixBS():
	tweetsListBS = twitter_preprocessing.getTweets('SenSanders')
	processedTweetsBS = twitter_preprocessing.finalProcess(tweetsListBS)
	tweetsPOSTAGGED_BS = twitter_preprocessing.POSTAGTwitterData(processedTweetsBS)
	tweetsBS = twitter_features_matrix.twitterFeaturesMatrix(processedTweetsBS, tweetsPOSTAGGED_BS).transpose()
	return tweetsBS

gbc = classifiers.loadGBC()


def getPredictionForHC():
	resultsGBC_HC = gbc.predict(getMatrixHC())
	return resultsGBC_HC

def getPredictionForBS():
	resultsGBC_BS = gbc.predict(getMatrixBS())
	return resultsGBC_BS

def getPredictionForDT():
	resultsGBC_DT = gbc.predict(getMatrixDT())
	return resultsGBC_DT


def countTrueFalse(res_politician):
	true=0
	false=0
	for res in res_politician:
		if res == 1:
			true = true + 1
		else:
			false = false + 1
	res=[true,false]
	return res


def procentaj(resultateCandidat):
	total=resultateCandidat[0]+resultateCandidat[1]
	procentTrue=(resultateCandidat[0]/total)*100
	procentFalse=(resultateCandidat[1]/total)*100
	return procentTrue,procentFalse,total

def countedResultsForHC():
	resultsGBC_HC = getPredictionForHC()
	countedResHC = countTrueFalse(resultsGBC_HC)
	return countedResHC

def countedResultsForBS():
	resultsGBC_BS = getPredictionForBS()
	countedResBS = countTrueFalse(resultsGBC_BS)
	return countedResBS

def countedResultsForDT():
	resultsGBC_DT = getPredictionForDT()
	countedResDT = countTrueFalse(resultsGBC_DT)
	return countedResDT




def printStatisticsHC():
	countedResHC = countedResultsForHC()
	sep1 = ' '
	# res1 ="Hillary Clinton\n \t\t% TRUE: ",round(procentaj(countedResHC)[0],2)," \n\t\t% FALSE: ",round(procentaj(countedResHC)[1],2),"\n\t\tNbrOfTrue: ",countedResHC[0], "\n\t\tNbrOfFalse: ", countedResHC[1],"\n\t\tTotal: ",procentaj(countedResHC)[2],"\n"
	s1 = "Hillary Clinton\n \t\t% TRUE: "
	s2 = " \n\t\t% FALSE: "
	s3 = " \n\t\tNbrOfTrue: "
	s4 = " \n\t\tNbrOfFalse: "
	s5 = " \n\t\tTotal: "
	seq1=(str(s1),str(round(procentaj(countedResHC)[0],2)))
	raspuns1=sep1.join(seq1)
	seq2=(str(s2),str(round(procentaj(countedResHC)[1],2)))
	raspuns2=sep1.join(seq2)
	seq3=(str(s3),str(countedResHC[0]))
	raspuns3=sep1.join(seq3)
	seq4=(str(s4),str(countedResHC[1]))
	raspuns4=sep1.join(seq4)
	seq5=(str(s5),str(procentaj(countedResHC)[2]))
	raspuns5=sep1.join(seq5)
	raspfinal = sep1.join([raspuns1,raspuns2,raspuns3,raspuns4,raspuns5])
	return raspfinal

def printStatisticsBS():
	countedResBS = countedResultsForBS()
	sep1 = ' '
	s1 = "\nBernie Sanders\n \t\t% TRUE:"
	s2 = " \n\t\t% FALSE: "
	s3 = " \n\t\tNbrOfTrue: "
	s4 = " \n\t\tNbrOfFalse: "
	s5 = " \n\t\tTotal: "
	seq1=(str(s1),str(round(procentaj(countedResBS)[0],2)))
	raspuns1=sep1.join(seq1)
	seq2=(str(s2),str(round(procentaj(countedResBS)[1],2)))
	raspuns2=sep1.join(seq2)
	seq3=(str(s3),str(countedResBS[0]))
	raspuns3=sep1.join(seq3)
	seq4=(str(s4),str(countedResBS[1]))
	raspuns4=sep1.join(seq4)
	seq5=(str(s5),str(procentaj(countedResBS)[2]))
	raspuns5=sep1.join(seq5)
	raspfinal = sep1.join([raspuns1,raspuns2,raspuns3,raspuns4,raspuns5])
	return raspfinal

def printStatisticsDT():
	countedResDT = countedResultsForDT()
	sep1 = ' '
	s1 = "\nDonald Trump\n \t\t% TRUE:"
	s2 = " \n\t\t% FALSE: "
	s3 = " \n\t\tNbrOfTrue: "
	s4 = " \n\t\tNbrOfFalse: "
	s5 = " \n\t\tTotal: "
	seq1=(str(s1),str(round(procentaj(countedResDT)[0],2)))
	raspuns1=sep1.join(seq1)
	seq2=(str(s2),str(round(procentaj(countedResDT)[1],2)))
	raspuns2=sep1.join(seq2)
	seq3=(str(s3),str(countedResDT[0]))
	raspuns3=sep1.join(seq3)
	seq4=(str(s4),str(countedResDT[1]))
	raspuns4=sep1.join(seq4)
	seq5=(str(s5),str(procentaj(countedResDT)[2]))
	raspuns5=sep1.join(seq5)
	raspfinal = sep1.join([raspuns1,raspuns2,raspuns3,raspuns4,raspuns5])
	return raspfinal


