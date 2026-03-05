from User import User
from server import Server
from database import Database

# user
user1 = User("Axel")
print(user1.username, "logged in?", user1.logged_in)
user1.login()
print(user1.username, "logged in?", user1.logged_in)
user1.logout()
print(user1.username, "logged in?", user1.logged_in)

# socket, server
my_server = Server("prod-server")
my_server.info()

# database
db = Database("prod-db")

db.connect()
db.query("INSERT SOMETHING RANDOM")
db.disconnect()
