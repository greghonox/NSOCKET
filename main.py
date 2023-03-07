from src.nsocket import NSocket


if __name__ == '__main__':
    socket = NSocket()
    socket.create()
    socket.run()