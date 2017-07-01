#!/usr/bin/env python3
"""
module contains a twitter bot that tweets onces a day
"""
import tweepy
from get_rank_1 import get_rank_1
import time, random, schedule
from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

def tweet():
    """
    tweets
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    while True:
         try:
             tweet = get_rank_1() + ' /r/#programming top post!'
             break
         except:
             time.sleep(random.randint(1, 10))
             pass
    try:
        api.update_status(status=tweet)
    except Exception as e:
        api.update_status(status=
                          "Oops, something went wrong. Someone tell my owner!!! Error:{}".
                          format(e))

if __name__ == "__main__":
    schedule.every().day.at("15:32").do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(1)
