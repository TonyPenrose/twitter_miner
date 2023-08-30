import tweepy
import os
from tweepy import OAuthHandler
import json

consumer_key = os.environ.get('API_KEY_TWITTER')
consumer_secret = os.environ.get('API_SECRET_TWITTER')
access_token = os.environ.get('ACCESS_TOKEN_TWITTER')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET_TWITTER')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    # A list of all our followers
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    # A list of all our tweets
    process_or_store(tweet._json)


