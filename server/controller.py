'''This file connects the model and view of the app.
It also controls them both.
This also contains the main funciton which is the starting point of the application
'''

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from view import Ui_MainWindow
from model import Model
from threading import ServerThread
import sys

class Controller(Ui_MainWindow):

    '''Constructor'''
    def __init__(self):
        super().__init__() #initialising the super class
        self.model = Model('127.0.0.1',5000)
        self.threadpool = QThreadPool() #initialising a seperate thread for starting server in the background

    '''SetUp the UI of the super class, 
    add here the code that relates to 
    the way UI works'''
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.startServer.clicked.connect(self.BtnStartClicked)
        self.sndBtn.clicked.connect(self.BtnSendClicked)    
        # self.setImgBtn.clicked.connect(self.SelectImage)    

    def BtnStartClicked(self):
        self.serverTh = ServerThread(self.model.s) # object of the serverThread class
        self.model.startServer()
        self.threadpool.start(self.serverTh) #starting the thread
        print("Start Button Clicked")
        print(self.model.serverStatus)
        self.startServer.setDisabled(True)

    def BtnSendClicked(self):
        self.serverTh.sendMssg(self.textToSend.text())
        print("Send Button Clicked")
        

'''The main entry point of the application'''
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  #reference to QMainWindow qt widget
    ui = Controller()  #object of the controller class
    ui.setupUi(MainWindow) #setupUI method ot the UI class
    MainWindow.show()  #starting the main window
    sys.exit(app.exec_()) #closing the window when user ends it
    ui.model.s.close()
main()