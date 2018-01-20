import json
import time

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


##################################################
# Forked from Joey Phan
##################################################

keywords = 'hello world'
output_file = 'data.txt'


# Load keys from keys.json into variables
filename = 'keys.json'
if filename:
    with open(filename, 'r') as f:
        keys = json.load(f)

consumerKey = keys['consumer_key']
consumerSecret = keys['consumer_key_secret']
accessToken = keys['access_token']
accessSecret = keys['access_token_secret']


# Creating Listener class that will gather data from API
class Listener(StreamListener):
    def on_data(self, str_data):
        try:
            # Data from on_data initially comes in as string. Converts to json
            data_json = json.loads(str_data)

            # Checking if keywords exist in data
            if 'id' in data_json and 'text' in data_json and 'user' in data_json:
                try:
                    saveFile = open(output_file, 'a')
                    saveFile.write(str_data)
                    saveFile.close()

                    # Options of what to print
                    # print str_data
                    print "TWEET: " + data_json['text']

                    return True
                except BaseException, e:
                    print 'failed on_data: ', str(e)
                    time.sleep(5)
            return True

        # Could happen with bad internet... etc other errors
        except BaseException, e:
            print 'failed on_data,', str(e)
            time.sleep(5)

    # Happens when an error occurs - probably through a wrong key
    def on_error(self, status):
        print status
        if status == 420:  # 420 means maxed out on number of requests in a window of time
            return False
        time.sleep(30)


# Setting Authentication Keys for API
auth = OAuthHandler(consumerKey, consumerSecret)
api = tweepy.API(auth)
auth.set_access_token(accessToken, accessSecret)
twitterStream = Stream(auth, Listener())

# Gathering tweets with keywords
twitterStream.filter(track=[keywords])