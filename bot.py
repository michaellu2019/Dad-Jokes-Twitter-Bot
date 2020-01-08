import tweepy as tp
import time
import os

# credentials
consumer_key = '[INSERT FROM THE APP UNDER YOUR TWITTER DEVELOPER ACCOUNT]'
consumer_secret = '[INSERT FROM THE APP UNDER YOUR TWITTER DEVELOPER ACCOUNT]'
access_token = '[INSERT FROM THE APP UNDER YOUR TWITTER DEVELOPER ACCOUNT]'
access_secret = '[INSERT FROM THE APP UNDER YOUR TWITTER DEVELOPER ACCOUNT]'

# pull jokes from text file and store them in array
jokes = []
f = open('dad_jokes.txt', 'r')

for line in f:
	jokes.append(line[:-1])

print('jokes retrieved...')
	
# post jokes to twitter
# login to twitter
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

for joke in jokes:
	try:
		text = 'Bot says: ' + joke + ' Hahahahahahahaha... Ha...'
		api.update_status(text)
		print('posted joke: ', text)
		time.sleep(60)
	except Exception as ex:
		print('exception occured: ', ex)
