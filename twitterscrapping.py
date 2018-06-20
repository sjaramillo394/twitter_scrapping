from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

ckey = "GQhK1WoZXODVtB1iykKKV6BQk"
csecret = "F1AeIYzwzTET1QOep2vUL6V0W6pKWanYMctKcUIb2r8XhalpDz"
atoken = "345550799-K0PzeUU79yXtetcNeMVziyFmrFubDAUn6UQ2JuFq"
asecret = "VlAjOKpD0QL3pSCPijvFpSsnn9Wo0SdXp7WtA5J85jngE"

class listener(StreamListener):

    def on_data(self, data):
        with open('twitter_duque.json', 'a') as f:
            f.write(data)
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Ivan Duque"])
