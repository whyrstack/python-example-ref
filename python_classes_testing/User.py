class User:
    def __init__(self, username):
        self.username = username
        self.logged_in = False

    def login(self):
        self.logged_in = True

    def logout(self):
        self.logged_in = False