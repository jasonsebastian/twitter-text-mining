import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# Basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    with open("CREDENTIALS.json") as c:
        creds = json.load(c)

    # Credentials to access Twitter API
    ACCESS_TOKEN = creds["access_token"]
    ACCESS_TOKEN_SECRET = creds["access_token_secret"]
    CONSUMER_KEY = creds["consumer_key"]
    CONSUMER_SECRET = creds["consumer_secret"]

    # Handle Twitter authentification and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    # Filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
