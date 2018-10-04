from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Credentials to access Twitter API
access_token = "1046980874552655872-h3j0Fksv7kpydsPJ6B1xC7MhNgD69z"
access_token_secret = "oIbYLz5iNtRmo458QuiHrEpCLKLINdKlfwPT5s1Kf3sCT"
consumer_key = "nvFIpH6VSbn1l8TfV6HjixvLw"
consumer_secret = "66Ac0fbsy0oly1jgYbqFWyMBiHt8ul5CIHKMtIYNDAsPmZF1Qt"


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
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])