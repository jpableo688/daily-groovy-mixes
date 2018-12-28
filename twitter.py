import tweepy
import datetime

CONSUMER_KEY = ''
CONSUER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth =  tweepy.OAuthHandler(CONSUMER_KEY, CONSUER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
user = api.get_user('USER-NAME-HERE')

def tweet(string):
    api.update_status(string)

def template_tweet(url):
    time = datetime.datetime.now()
    time = time.strftime("%x")
    return_tweet = "here's a groovy mix for " + str(time) + ' ' + str(url)
    return return_tweet
