from ClientUI import Ui_MainWindow
from PyQt5 import QtWidgets
from model import Model
import sys

class controller(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.model = Model('127.0.0.1',5000)
        self.model.startClient()
       
    def setupUi(self,mainWindow):
        super().setupUi(mainWindow)
        self.connToServerBtn.clicked.connect(self.BtnConnectClicked)
        self.receivedText.setText(self.model.recvMssg())
        self.receivedText.repaint()

    '''Defining the functions for signals'''
    def BtnConnectClicked(self):
        self.debugWindow.append("Connect Button Clicked")
        self.model.connectToServer()
        if self.model.connectionStatus:
            self.debugWindow.append(f"Connected to server>>(\'{self.model.ip}\',{self.model.port})")
            self.connToServerBtn.setDisabled(True)
        else:
            self.debugWindow.append('Server not Started')
        
        
'''Starting the Application loop'''
app = QtWidgets.QApplication([])
ui = controller()
mainwindow = QtWidgets.QMainWindow()
ui.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())