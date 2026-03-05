import socket

class Server:
    def __init__(self, name):
        self.name = name
        self.ip = self.get_local_ip()
        self.status = "stopped"

    def get_local_ip(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    
    def start(self):
        self.status = "running"
        print(self.name, "started at", self.ip)

    def stop(self):
        self.status = "stopped"
        print(self.name, "stopped at", self.ip)

    def info(self):
        print("server name:", self.name)
        print("server ip:", self.ip)
        print("server status:", self.status)
