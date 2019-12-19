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
def add_or_update_user(username):
    """add or update a user and their tweets, or else give error"""
    try:
        twitter_user=TWITTER.get_user(username)
        db_user=(User.query.get(twitter_user.id) or
        User(id=twitter.id, name=username))
        DB.session.add(db_user)
        tweets = twitter_user.timeline(count=200, exclude_replies=True,
        include_rts=False, tweet_mode='extended',
        since_id=db_user.newest_tweet_id)
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        for tweet in tweets:
            # calculate embedding on the full tweet
            embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300],
            embedding=embedding)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)

    except Exception as e:
        print('Error processing {}: {}'.format(username,e))
        raise # -*- coding: utf-8 -*-



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
