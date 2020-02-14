# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.labelClient = QtWidgets.QLabel(Dialog)
        self.labelClient.setGeometry(QtCore.QRect(240, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelClient.setFont(font)
        self.labelClient.setAlignment(QtCore.Qt.AlignCenter)
        self.labelClient.setObjectName("labelClient")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 320, 361, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelDebugWindow = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDebugWindow.setFont(font)
        self.labelDebugWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDebugWindow.setObjectName("labelDebugWindow")
        self.verticalLayout_2.addWidget(self.labelDebugWindow)
        self.textBrowserDebugWindow = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowserDebugWindow.setObjectName("textBrowserDebugWindow")
        self.verticalLayout_2.addWidget(self.textBrowserDebugWindow)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 50, 321, 241))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelImgReceived = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelImgReceived.setFont(font)
        self.labelImgReceived.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelImgReceived.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImgReceived.setObjectName("labelImgReceived")
        self.verticalLayout_4.addWidget(self.labelImgReceived)
        self.labelImg = QtWidgets.QLabel(Dialog)
        self.labelImg.setGeometry(QtCore.QRect(120, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelImg.setFont(font)
        self.labelImg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImg.setObjectName("labelImg")
        self.pushButtonConnect = QtWidgets.QPushButton(Dialog)
        self.pushButtonConnect.setGeometry(QtCore.QRect(480, 380, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonConnect.setFont(font)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.textEditReceived = QtWidgets.QTextEdit(Dialog)
        self.textEditReceived.setGeometry(QtCore.QRect(360, 50, 231, 241))
        self.textEditReceived.setObjectName("textEditReceived")
        self.labelText = QtWidgets.QLabel(Dialog)
        self.labelText.setGeometry(QtCore.QRect(430, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelText.setFont(font)
        self.labelText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelText.setObjectName("labelText")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelClient.setText(_translate("Dialog", "Client"))
        self.labelDebugWindow.setText(_translate("Dialog", "Debug Window"))
        self.labelImgReceived.setText(_translate("Dialog", "Image to received"))
        self.labelImg.setText(_translate("Dialog", "Image received"))
        self.pushButtonConnect.setText(_translate("Dialog", "connect"))
        self.labelText.setText(_translate("Dialog", "Text Received"))
