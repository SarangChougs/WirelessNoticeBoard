import threading from Thread

conn = None

class ClientThread(Thread):
    def __init__(self,ip,port):
        Thread.__init(self)

    def run(self):
        While True:
            global conn
            data = conn.recv(1024)
            window.textEditMssg.append('Client :' + data.decode('utf-8'))

