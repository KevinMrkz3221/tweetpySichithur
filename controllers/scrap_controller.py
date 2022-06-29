import server
import mysql.connector

class Scrap_controller:
    def __init__(self) -> None:
        self.cnn = mysql.connector.connect(
                    host="sichiturdataset.cm7pj2kzc5wz.us-east-1.rds.amazonaws.com",
                    user="dbasichitur",
                    password="my5qld4t4b4s3",
                    database="sichiturdb"
                )

    def insert(self, inserted_rows):
        sql = '''INSERT INTO SCRAP_HISTORY (platform, inserted_rows)
                 VALUES ('TWITTER',{})'''.format(inserted_rows)

        cur = self.cnn.cursor()
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()

        return n