import psycopg2

class Database():
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                host = self.host,
                port = self.port,
                dbname = self.dbname,
                user = self.user,
                password = self.password
            )
            print("Successfully connected to", self.host, "on port", self.port, "to database", self.dbname, "using user", self.user)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Connection closed to", self.host)
    
    def create_table(self):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(100)
                );
            """)
            self.conn.commit()
            print("Table 'users' is ready")

    def insert_user(self, username, email):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id;",
                (username, email)
            )
            user_id = cur.fetchone()[0]
            self.conn.commit()
            print(f"Inserted user {username} with id {user_id}")
            return user_id
        
    def get_users(self):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, username, email FROM users;")
            return cur.fetchall()
