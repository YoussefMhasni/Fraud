import tweepy
from kafka import KafkaProducer
import logging

"""API ACCESS KEYS"""
consumerKey = "cux9gE2ReaD91ZWhJqHNi28X4"
consumerSecret = "NbmQNFbs5ZJqwsPmGTyzYRBwY7VPcgsywKSXwx8DTp34XVjNZw"
accessToken = "3908641701-ABuYXILKal8YKs9Eg0U4FaYsLKwbcQfIVoo3nbi"
accessTokenSecret = "wWCqwpI61LbXn8cGZfd147Lx7hR0YI1Yy1YJ3ZGiqhcqk"

producer = KafkaProducer(bootstrap_servers='localhost:9092')
term = 'morocco'
topic_name = 'testing'


def twitterAuth():
    # create the authentication object
    authenticate = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret,access_token=accessToken,access_token_secret=accessTokenSecret)
    # set the access token and the access token secret
    # create the API object
    api = tweepy.API(authenticate, wait_on_rate_limit=True)    
    return api


class TweetListener(tweepy.Stream):

    def on_data(self, raw_data):
        producer.send(topic_name, value=raw_data)
        return True
    def start_streaming_tweets(self, search_term):
        self.filter(track=search_term)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    twitter_stream = TweetListener(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    twitter_stream.start_streaming_tweets(search_term=term)