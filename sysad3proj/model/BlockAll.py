# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BlockAll.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogBlock(object):

    def setupUi(self, DialogBlock):
        DialogBlock.setObjectName("DialogBlock")
        DialogBlock.resize(400, 136)
        DialogBlock.setStyleSheet("background-color: #212121;")
        self.frame = QtWidgets.QFrame(DialogBlock)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.frame.setStyleSheet("background-color: #424242;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-70, 30, 171, 201))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 251, 61))
        self.label_2.setObjectName("label_2")


        self.BlockAllBut = QtWidgets.QPushButton(self.frame)
        self.BlockAllBut.setGeometry(QtCore.QRect(250, 70, 91, 23))
        self.BlockAllBut.setStyleSheet("background-color: rgb(255, 241, 234);")
        self.BlockAllBut.setObjectName("BlockAllBut")


        self.CancelBut = QtWidgets.QPushButton(self.frame)
        self.CancelBut.setGeometry(QtCore.QRect(130, 70, 75, 23))
        self.CancelBut.setStyleSheet("background-color: rgb(255, 246, 235);")
        self.CancelBut.setObjectName("CancelBut")



        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 91, 81))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/warning.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(75, 75))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(DialogBlock)
        QtCore.QMetaObject.connectSlotsByName(DialogBlock)

    def retranslateUi(self, DialogBlock):
        _translate = QtCore.QCoreApplication.translate
        DialogBlock.setWindowTitle(_translate("DialogBlock", "Block"))
        self.label.setText(_translate("DialogBlock", "<html><head/><body><p><img src=\":/img/warning.png\" height = \"50\"/></p></body></html>"))
        self.label_2.setText(_translate("DialogBlock", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Are you sure you want to </span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">block all interfaces?</span></p></body></html>"))
        self.BlockAllBut.setText(_translate("DialogBlock", "YES, I am sure"))
        self.CancelBut.setText(_translate("DialogBlock", "Cancel"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogBlock = QtWidgets.QDialog()
    ui = Ui_DialogBlock()
    ui.setupUi(DialogBlock)
    DialogBlock.show()
    sys.exit(app.exec_())

