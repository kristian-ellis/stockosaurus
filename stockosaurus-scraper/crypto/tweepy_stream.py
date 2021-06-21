import tweepy


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

        
    def on_error(self, status_code):
        if status_code == 420:
        #returning False in on_data disconnects the stream
            return False
            