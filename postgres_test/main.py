import os
from dotenv import load_dotenv
from database import Database

load_dotenv()

def main():
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    # initialize db
    db = Database(db_host, db_port, db_name, db_user, db_password)

    db.connect()
    db.create_table()
    db.insert_user("Axel", "axel@admin.com")
    db.insert_user("Foo", "foo@admin.com")

    users = db.get_users()

    for user in users:
        print(user)

    db.close()

if __name__ == "__main__":
    main()

