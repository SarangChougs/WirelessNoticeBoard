# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.labelServer = QtWidgets.QLabel(Dialog)
        self.labelServer.setGeometry(QtCore.QRect(240, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelServer.setFont(font)
        self.labelServer.setObjectName("labelServer")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 120, 251, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelText = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelText.sizePolicy().hasHeightForWidth())
        self.labelText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelText.setFont(font)
        self.labelText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelText.setObjectName("labelText")
        self.verticalLayout.addWidget(self.labelText)
        self.lineEditTextToSend = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTextToSend.sizePolicy().hasHeightForWidth())
        self.lineEditTextToSend.setSizePolicy(sizePolicy)
        self.lineEditTextToSend.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEditTextToSend.setObjectName("lineEditTextToSend")
        self.verticalLayout.addWidget(self.lineEditTextToSend)
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(440, 350, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonStart = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.verticalLayout_3.addWidget(self.pushButtonStart)
        self.pushButtonSend = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.verticalLayout_3.addWidget(self.pushButtonSend)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 50, 321, 241))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelImgToSend = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelImgToSend.setFont(font)
        self.labelImgToSend.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelImgToSend.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImgToSend.setObjectName("labelImgToSend")
        self.verticalLayout_4.addWidget(self.labelImgToSend)
        self.pushButtonSelectImg = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSelectImg.setFont(font)
        self.pushButtonSelectImg.setObjectName("pushButtonSelectImg")
        self.verticalLayout_4.addWidget(self.pushButtonSelectImg)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelServer.setText(_translate("Dialog", "Server"))
        self.labelText.setText(_translate("Dialog", "Text to send"))
        self.labelDebugWindow.setText(_translate("Dialog", "Debug Window"))
        self.pushButtonStart.setText(_translate("Dialog", "Start"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
        self.labelImgToSend.setText(_translate("Dialog", "Image to send"))
        self.pushButtonSelectImg.setText(_translate("Dialog", "Select Image"))
