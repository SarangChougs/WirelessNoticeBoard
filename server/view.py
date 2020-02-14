# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgToSend = QtWidgets.QLabel(self.centralwidget)
        self.imgToSend.setGeometry(QtCore.QRect(9, 9, 231, 161))
        self.imgToSend.setObjectName("imgToSend")
        self.setImgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.setImgBtn.setGeometry(QtCore.QRect(9, 189, 75, 23))
        self.setImgBtn.setObjectName("setImgBtn")
        self.textToSend = QtWidgets.QLineEdit(self.centralwidget)
        self.textToSend.setGeometry(QtCore.QRect(30, 250, 281, 20))
        self.textToSend.setObjectName("textToSend")
        self.sndBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sndBtn.setGeometry(QtCore.QRect(544, 390, 81, 31))
        self.sndBtn.setObjectName("sndBtn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(360, 20, 291, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.startServer = QtWidgets.QPushButton(self.centralwidget)
        self.startServer.setGeometry(QtCore.QRect(70, 360, 91, 31))
        self.startServer.setObjectName("startServer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setImgBtn.clicked.connect(self.SelectImage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SelectImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "" , "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imgToSend.width(), self.imgToSend.height(), QtCore.Qt.KeepAspectRatio)
            self.imgToSend.setPixmap(pixmap)
            self.imgToSend.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imgToSend.setText(_translate("MainWindow", "Image"))
        self.setImgBtn.setText(_translate("MainWindow", "select image"))
        self.sndBtn.setText(_translate("MainWindow", "Send"))
        self.startServer.setText(_translate("MainWindow", "Start Server"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
