from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

ckey = "xxxxxxxxxx"
csecret = "xxxxxxx"
atoken = "xxxxxxxx"
asecret = "xxxxxx"

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
