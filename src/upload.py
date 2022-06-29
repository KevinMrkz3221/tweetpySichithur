from inspect import Attribute
import controllers


def insert():
    querys = controllers.Hashtags_controller().get_hashtags()
    count = 0
    for query in querys:
        data = controllers.Tweepy_controller().get_list(query)
        if(data.meta['result_count'] != 0):
            for tweet in data.data:
                try:
                    controllers.Tweets_controller().insert_tweet(tweet.text, query, tweet.created_at)
                    count = count + 1
                except:
                    print('Error on query {} Number {} '.format(query, count))
    
    return count

def main():
    
    number_tweets = insert()

    controllers.Scrap_controller().insert(number_tweets)