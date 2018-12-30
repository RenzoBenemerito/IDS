# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
import io
import requests
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn import metrics
from keras.models import Sequential, load_model

import threading
from threading import Thread
import asyncio

from PyQt5 import QtCore, QtGui, QtWidgets
from Settings import Ui_Dialog
from BlockAll import Ui_DialogBlock
from About import Ui_AboutIDS

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import predict
from scapy.all import *
import interface

counter = 0
counter1 = 0
interface = interface.getInterface()
class Ui_MainWindow(object):



    def SettingsWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi (self.window)
        self.window.show()


    def BlockAll(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_DialogBlock()
        self.ui.setupUi (self.window)
        self.window.show()


    def AboutWindows(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutIDS()
        self.ui.setupUi (self.window)
        self.window.show()


    def exitSystem(self):
        sys.exit(app.exec_())


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 740)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #212121;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 731, 81))
        self.frame.setStyleSheet("background-color: #424242;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setStyleSheet("color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.AboutWindows)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setStyleSheet("color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.SettingsWindow)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_4.setStyleSheet("color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.BlockAll)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_5.setStyleSheet("color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(self.exitSystem)


        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 140, 731, 561))
        self.frame_2.setStyleSheet("background-color: #424242;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setGeometry(QtCore.QRect(20, 60, 691, 481))
        self.scrollArea.setStyleSheet("background-color: #FFFFFF")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 691, 481))
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(138)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 51, 28))
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/img/on.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: Roboto;\n"
"font-size: 40;\n"
"color: white;\n"
"font-style: strong;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(550, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: Roboto;\n"
"font-size: 20;\n"
"color: white;\n"
"font-style: strong;\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(780, 140, 321, 561))
        self.frame_3.setStyleSheet("background-color: #424242;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("font: Roboto;\n"
"font-size: 40;\n"
"color: white;\n"
"font-style: strong;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(10, 50, 231, 20))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("color: white\n"
"")
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 80, 301, 461))
        self.scrollArea_2.setStyleSheet("background-color: #263238")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 299, 459))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 301, 461))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(780, 10, 131, 121))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(910, 50, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: Roboto;\n"
"font-size: 40;\n"
"color: white;\n"
"font-style: strong;\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 10, 141, 41))
        self.pushButton_6.setStyleSheet("\n"
"background-color: rgb(69, 208, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6.clicked.connect(self.test)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def capture(self):
        capture =  sniff(iface=interface,  prn = self.extract)
        wrpcap('scapy.pcap', capture)

    packets = []
    

    def extract(self,packet):
        packets = []
        global counter
        global counter1
        if len(self.packets) == 30:
            packets = []
        while len(packets) != 30:
            packet = [0, 'icmp', 'eco_i', 'SF', 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 4, 2, 0.5, 0.75, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 'nmap.']
            packets.append(packet)
        p = predict.prediction()
        df = pd.DataFrame(packets)
        values = df.values.tolist()
        df = p.addCol(df)
        df['outcome'] = ""
        df = p.encode(df)
        x,y = p.to_xy(df, 'outcome')
        aattack = p.predictOut(x)
        
        for v in values:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(counter,0, QTableWidgetItem(str(v[0])))
            self.tableWidget.setItem(counter,1 , QTableWidgetItem(v[1]))
            self.tableWidget.setItem(counter,2 , QTableWidgetItem(v[2]))
            self.tableWidget.setItem(counter,3 , QTableWidgetItem(v[3]))
            self.tableWidget.setItem(counter,4 , QTableWidgetItem(str(v[4])))
            counter += 1

        for at in aattack:
            rowPosition = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition)
            self.tableWidget_2.setItem(counter1,0, QTableWidgetItem(at))
            counter1 += 1


        return packets

    def test(self):
        c= Thread(target = self.capture)
        c.daemon = True
        c.start()
   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "  About"))
        self.pushButton_3.setText(_translate("MainWindow", "Settings"))
        self.pushButton_4.setText(_translate("MainWindow", "Block"))
        self.pushButton_5.setText(_translate("MainWindow", "Exit"))
        self.pushButton_6.setText(_translate("MainWindow", "START SERVICE"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DURATION"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PROTOCOL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SERVICE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "FLAG"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SRC BYTE"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Packets"))
        self.label_3.setText(_translate("MainWindow", "AI Mode"))
        self.label.setText(_translate("MainWindow", "Attacks"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ATTACK"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/img/logo.png\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "I D S"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

