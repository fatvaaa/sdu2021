# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'haha.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(794, 441)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 50, 221, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 201, 291))
        self.label.setObjectName("label")
        self.btn_big = QtWidgets.QPushButton(Dialog)
        self.btn_big.setGeometry(QtCore.QRect(340, 100, 75, 23))
        self.btn_big.setObjectName("btn_big")
        self.btn_small = QtWidgets.QPushButton(Dialog)
        self.btn_small.setGeometry(QtCore.QRect(340, 240, 75, 23))
        self.btn_small.setObjectName("btn_small")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(500, 50, 221, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 201, 291))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.btn_big.setText(_translate("Dialog", "放大"))
        self.btn_small.setText(_translate("Dialog", "缩小"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
