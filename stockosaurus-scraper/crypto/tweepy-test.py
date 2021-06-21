import tweepy as tweepy
from .tweepystream import MyStreamListener

# Verifired Twitter Developer account gets these values
consumer_token = "string"
consumer_secret = "string"
consumer_key = "string"
key = "14jbgSlr6HkcE8OpyWSP1slNJ"
secret = "tj20UqQQKAO4b7Wv6WHmIGKj4Yn2kwDZOOUMAUpCve0PA5QPHb"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP1oPwEAAAAAY7aG0NWpRdLVhpeOsjgjRxa5e5I%3D4d7r41ETKv9FfSzTzHXQHNiyMQuJN1JlzTRbVtFGU9Lx99kzjY"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

# Example w/o callback (desktop)
# verifier = raw_input('Verifier:')

auth.request_token = bearer_token

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

myStream.filter(track=['python'])
