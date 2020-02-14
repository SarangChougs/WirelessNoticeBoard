import sys,time
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread
from socketserver import ThreadingMixIn
from serverWindow import *

conn = None # global server object

'''Class for initializing window. This class inherits Qdialog, as we have created a Dialog using QtDesigner'''
class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.TextToSend = self.ui.lineEditTextToSend
        self.DebugWindow = self.ui.textBrowserDebugWindow
        self.ui.pushButtonSelectImg.clicked.connect(self.selectImg)
        self.ui.pushButtonSend.clicked.connect(self.send)
        self.ui.pushButtonStart.clicked.connect(self.startServer)
        self.show()

    def selectImg(self):
        self.printDebugMssg('selectImg Pressed')

    def send(self):
        global conn
        self.printDebugMssg('sendButton Pressed')
        text = self.ui.lineEditTextToSend.text()
        conn.send(text.encode('utf-8'))
        self.printDebugMssg(text)
        self.ui.lineEditTextToSend.setText('')

    def startServer(self):
        self.printDebugMssg('startServerButton Pressed')

    def printDebugMssg(self,mssg):
        self.DebugWindow.append(mssg)

'''Class for server thread''' 
class ServerThread(Thread):

    def __init__(self,window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = '127.0.0.1'
        TCP_PORT = 5052
        tcpServer = socket.socket()
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP,TCP_PORT))
        tcpServer.listen(4)
        self.window.ui.textBrowserDebugWindow.append(f'Server listening at : {TCP_IP}, {TCP_PORT}')
        threads = []

        while True:
            global conn 
            (conn,(ip,port)) = tcpServer.accept()
            newthread = ClientThread(ip,port,window)
            self.window.ui.textBrowserDebugWindow.append(f'Client connected : {ip},{port}')
            newthread.start()
            threads.append(newthread)

        for t in threads:
            t.join()

'''Class for client thread'''
class ClientThread(Thread):

    def __init__(self,ip,port,window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            global conn
            data = conn.recv(1024)
            window.ui.textBrowserDebugWindow.append('Client: ' + data.decode('utf-8'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    serverThread = ServerThread(window)
    serverThread.start()
    window.exec()
    sys.exit(app.exec_())