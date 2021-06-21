import tweepy as tweepy
from tweepy_stream import MyStreamListener

# Verifired Twitter Developer account gets these values
consumer_token = "string"
consumer_secret = "string"
consumer_key = "string"
key = "14jbgSlr6HkcE8OpyWSP1slNJ"
secret = "tj20UqQQKAO4b7Wv6WHmIGKj4Yn2kwDZOOUMAUpCve0PA5QPHb"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP1oPwEAAAAAY7aG0NWpRdLVhpeOsjgjRxa5e5I%3D4d7r41ETKv9FfSzTzHXQHNiyMQuJN1JlzTRbVtFGU9Lx99kzjY"

auth = tweepy.OAuthHandler(bearer_token, secret)

# auth.request_token = bearer_token


auth.set_access_token(key, secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
print(myStream)
myStream.filter()


