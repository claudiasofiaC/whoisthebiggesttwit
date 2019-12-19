#retrieve tweets, embedding, save into db

import basilica
import tweepy
from decouple import config
from .models import DB, Tweet, User

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                  config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config('BASILICA_KEY'))

# to do: add functions later
# had to pip install tweepy in terminal

# flask shell
# from TWITOFF.twitter import *
#twitter_user = TWITTER.get_user('elonmusk')
#tweets = twitter_user.timeline(count=200, exclude_replies=True,
                                #include_rts=False, mode='extended')
#tweets[1].text

#tweet_text = tweets[0].text
#embedding=BASILICA.embed_sentence(tweet_text,
                                  #model='twitter')
