# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(400, 300)
        self.lcdNumber = QtWidgets.QLCDNumber(test)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 40, 271, 111))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(test)
        self.pushButton.setGeometry(QtCore.QRect(40, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(test)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(test)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 250, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "Test"))
        self.pushButton.setText(_translate("test", "开始"))
        self.pushButton_2.setText(_translate("test", "停止"))
        self.pushButton_3.setText(_translate("test", "暂停/恢复"))
