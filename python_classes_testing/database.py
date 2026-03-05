class Database():
    def __init__(self, host):
        self.host = host

    def connect(self):
        print("connecting to", self.host)

    def disconnect(self):
        print("disconnecting from", self.host)

    def query(self, sql_query):
        print("running sql query", sql_query, "on", self.host)