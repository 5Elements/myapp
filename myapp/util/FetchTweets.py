import tweepy



consumer_key = 'DpvH6jajTiXTlACU5GYh4E9Qn'
consumer_secret = 'v85H9ERJMS2qowxwXnOcMWZ5STa3Iv2xbdTSUIrZP2vIne7WLr'
access_token = '831880428197908484-hvgmFD3Ti2gU8uNnL76Ph2SL0X0jYC2'
access_token_secret = 'gp0gvD8CmdOVPP5QtAxNqT5xBon37kubiWwsvPQGR6eMa'

class FetchData():

    def getTwitterData(self, tag):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            api = tweepy.API(auth)

            public_tweets = api.search( q = tag, count=100,language = 'en' )

            return public_tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


