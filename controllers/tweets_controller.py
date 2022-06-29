import server
import mysql.connector

class Tweets_controller:
    def __init__(self) -> None:
        self.cnn = mysql.connector.connect(
                    host="sichiturdataset.cm7pj2kzc5wz.us-east-1.rds.amazonaws.com",
                    user="dbasichitur",
                    password="my5qld4t4b4s3",
                    database="sichiturdb"
                )

    def insert_tweet(self, caption, hashtag, created_at):
        sql = '''INSERT INTO twitter_posts (caption, hashtag, tweet_date)
                 VALUES ('{}','{}', '{}')'''.format(caption, hashtag, created_at)

        cur = self.cnn.cursor()
        cur.execute(sql)
        self.cnn.commit()
        n = cur.rowcount
        cur.close()

        return n