import tweepy

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAFcaVAEAAAAAqJhk9TI%2BB4%2FxMWGW4vT%2FkJWhpCg%3DjVD4g7oSNNbIvapvZZbdCzLvrsulmuv7hehSjThvf9QoVB5rzu')
api = tweepy.API('AAAAAAAAAAAAAAAAAAAAAFcaVAEAAAAAqJhk9TI%2BB4%2FxMWGW4vT%2FkJWhpCg%3DjVD4g7oSNNbIvapvZZbdCzLvrsulmuv7hehSjThvf9QoVB5rzu', wait_on_rate_limit=True)