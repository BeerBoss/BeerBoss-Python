# Imports
import MySQLdb


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = self.connect()

    def __exit__(self):
        self.conn.close()

    def submitData(self, fridgeTemp, barrelTemp, coolerState, heaterState):
        if fridgeTemp is not None and barrelTemp is not None:
            query = self.conn.cursor()
            try:
                query.execute("INSERT INTO sensorData(fridgeTemp, barrelTemp, coolerState, heaterState) VALUES (%s,%s,%s,%s)", (fridgeTemp, barrelTemp, coolerState, heaterState))
                self.conn.commit()
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                self.conn.rollback()

    def connect(self):
        try:
            conn = MySQLdb.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            return conn
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)


