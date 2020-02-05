from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM


class Server:
    def __init__(self, PORT: int = 5500, HOST: str = 'localhost', BUFSIZ: int = 512):
        self.addresses = {}
        self.clients = {}

        self.PORT = PORT
        self.HOST = HOST
        self.BUFSIZ = BUFSIZ

        self.ADDRESS = (self.HOST, self.PORT)

        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDRESS)

    def accept_incoming_connection(self):
        pass


if __name__ == '__main__':
    server = Server()
    server.SERVER.listen(5)
    print('Waiting for the connection...')
    ACCEPT_THREAD = Thread(target=server.accept_incoming_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.SERVER.close()
