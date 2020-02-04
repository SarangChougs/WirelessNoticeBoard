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
        self.textToSend = QtWidgets.QTextEdit(self.centralwidget)
        self.textToSend.setGeometry(QtCore.QRect(20, 220, 291, 41))
        self.textToSend.setObjectName("textToSend")
        self.sndBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sndBtn.setGeometry(QtCore.QRect(544, 390, 81, 31))
        self.sndBtn.setObjectName("sndBtn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(360, 20, 291, 351))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sndBtn.clicked.connect(MainWindow.sendbutton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imgToSend.setText(_translate("MainWindow", "Image"))
        self.setImgBtn.setText(_translate("MainWindow", "select image"))
        self.sndBtn.setText(_translate("MainWindow", "sndBtn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
