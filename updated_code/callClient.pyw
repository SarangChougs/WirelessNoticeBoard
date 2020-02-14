import sys
from PyQt5.QtWidgets import QApplication,QDialog
import socket
from threading import Thread
from socketserver import ThreadingMixIn
from clientWindow import *

tcpClientA = None

'''Class to initialize window '''
class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.textEditReceived = self.ui.textEditReceived
        self.debugmssg = self.ui.textBrowserDebugWindow
        self.show()

'''Class for client thread'''
class ClientThread(Thread):

    def __init__(self,window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        host = '127.0.0.1'
        port = 5052
        global tcpClientA
        tcpClientA = socket.socket()
        self.window.ui.textBrowserDebugWindow.append(f'Trying to connect to {host}, {port}')
        try: 
            tcpClientA.connect((host,port))
            self.window.ui.textBrowserDebugWindow.append(f'Connected to {host}, {port}')
            while True:
                data = tcpClientA.recv(1024)
                self.window.textEditReceived.append('Server>> ' + data.decode('utf-8'))
        except Exception as e:
            self.window.ui.textBrowserDebugWindow.append(str(e))

        tcpClientA.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    clientThread = ClientThread(window)
    clientThread.start()
    window.exec()
    sys.exit(app.exec_())