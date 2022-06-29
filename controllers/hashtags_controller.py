import server

class Hashtags_controller:
    def __init__(self) -> None:
        self.cnn = server.mydb


    def get_hashtags(self)->list:
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM HASHTAGS_MAIN")
        dbhashtags = cur.fetchall()
        cur.close()
        self.cnn.close()

        querys = [hashtag[0][1:] for hashtag in dbhashtags]       
        return querys

    





