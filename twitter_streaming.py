import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

with open("CREDENTIALS.json") as c:
    creds = json.load(c)

# Credentials to access Twitter API
ACCESS_TOKEN = creds["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = creds["ACCESS_TOKEN_SECRET"]
CONSUMER_KEY = creds["CONSUMER_KEY"]
CONSUMER_SECRET = creds["CONSUMER_SECRET"]


# Basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Handle Twitter authentification and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    # Filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
