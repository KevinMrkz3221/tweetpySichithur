from server import api, client
import controllers

class Tweepy_controller:
    def __init__(self) -> None:
        self.api = api
        self.client = client


    def get_list(self, _query):    
        return client.search_recent_tweets(query=_query, tweet_fields=['created_at','context_annotations'], max_results=100)  



