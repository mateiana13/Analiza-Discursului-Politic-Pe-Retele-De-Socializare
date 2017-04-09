#Twitter only allows access to a users most recent 3240 tweets with this method
import tweepy
import json

#Twitter API credentials
CONSUMER_KEY = "Vc6lEOT3qv8MWFVVx707qsOJA"
CONSUMER_SECRET = "6MHHgv6LhQjJ2ayx3kU7AfE7A3B2uow8lfdGoCH3g39res83Ym"

ACCESS_KEY = "1920254432-SZ2oax81M7vWME4ryHM83j1XpaiFecPii5fpdwS"
ACCESS_SECRET = "vrySmQ0iXyUmqlXfORnfUzap4M1g7dNzlDFNmklvPwDJ2"


targets = ["SenSanders", "HillaryClinton", "realDonaldTrump"]

nameDict = {}

def authorize_twitter():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	return auth

def API_response():
	api= tweepy.API(authorize_twitter())
	return api

def get_all_tweets(SCREEN_NAME):
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = API_response().user_timeline(screen_name = SCREEN_NAME,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = API_response().user_timeline(screen_name = SCREEN_NAME,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))

	return alltweets

def chose_info_from_tweets(SCREEN_NAME):
	outtweets = [[tweet.id_str, tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"), tweet.text.encode('unicode-escape')] for tweet in get_all_tweets(SCREEN_NAME)]
	return outtweets	

i = 0	
def get_tweets_in_JSON_format(SCREEN_NAME):
	arrayOfDict=[]
	
	for tweetArray in chose_info_from_tweets(SCREEN_NAME):
		global i
		i=i+1
		tweet={}
		tweet['id_str']=tweetArray[0]
		tweet['created_at']=tweetArray[1]
		tweet['text']=tweetArray[2].decode("utf-8")
		tweet['username']=SCREEN_NAME
		tweet['_id']=i
		arrayOfDict.append(tweet)
	return arrayOfDict	
	
		
def write_JSON(SCREEN_NAME):	
	with open('lista.json.txt' , 'w') as f:
		json.dump(get_tweets_in_JSON_format(SCREEN_NAME), f)


def json_for_list_of_targets():
	for target in targets:
		write_JSON(target)
	


	

	
	