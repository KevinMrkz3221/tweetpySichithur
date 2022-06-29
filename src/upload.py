from inspect import Attribute
import controllers
import models

def insert():
    querys = controllers.Hashtags_controller().get_hashtags()
    count = 0
    for query in querys:
        data = controllers.Tweepy_controller().get_list(query)
        if(data.meta['result_count'] != 0):
            for tweet in data.data:
                try:
                    my_tweet = models.Tweet(tweet.text, query, tweet.created_at)
                    controllers.Tweets_controller().insert_tweet(my_tweet.caption, my_tweet.hashtag, my_tweet.created_at)
                    count = count + 1
                except:
                    print('Error on query {} Number {} '.format(query, count))
    
    return count

def main():
    
    number_tweets = insert()

    controllers.Scrap_controller().insert(len(number_tweets))