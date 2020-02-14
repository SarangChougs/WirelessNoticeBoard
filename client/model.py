''''This is the Model of the client side. This contains all the
Backend code of the client side of the application.'''

import socket

class Model():

    '''Constructor'''
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.clientStatus = False
        self.connectionStatus = False

    def startClient(self):
        self.s = socket.socket()
        self.clientStatus = True
        print(self.clientStatus)

    def connectToServer(self):
        try:
            self.s.connect((self.ip,self.port))
            self.connectionStatus = True
            print(">>Connection = " + str(self.connectionStatus))
        except ConnectionRefusedError:
            print("Server Not Started.\nPlease start Server first.")

    def recvMssg(self):
        if self.connectionStatus:
            return self.s.recv(1024).decode()
        else:
            return 'Just Started'

def main():
    # m = Model('127.0.0.1',1236)
    # m.startClient()
    # m.connectToServer()
    print('Main method')

if __name__ == "__main__":
    main()

