# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from final_arch1 import run
from final import run_nt
from analyze import validate
from PandasModel import PandasModel
import os
import shutil
import pandas as pd
from dateandtime import get_date_time_after


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 728)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerBox = QtWidgets.QGroupBox(self.centralwidget)
        self.headerBox.setGeometry(QtCore.QRect(10, 0, 1001, 101))
        self.headerBox.setStyleSheet("background-color: rgb(49, 99, 238);\n"
"color: rgb(255, 255, 255);")
        self.headerBox.setTitle("")
        self.headerBox.setObjectName("headerBox")
        self.headerLabel = QtWidgets.QLabel(self.headerBox)
        self.headerLabel.setGeometry(QtCore.QRect(10, 20, 71, 61))
        self.headerLabel.setText("")
        self.headerLabel.setPixmap(QtGui.QPixmap(":/newPrefix/logohere.png"))
        self.headerLabel.setScaledContents(True)
        self.headerLabel.setObjectName("headerLabel")
        self.h1Label = QtWidgets.QLabel(self.headerBox)
        self.h1Label.setGeometry(QtCore.QRect(270, 10, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.h1Label.setFont(font)
        self.h1Label.setObjectName("h1Label")
        self.h2Label = QtWidgets.QLabel(self.headerBox)
        self.h2Label.setGeometry(QtCore.QRect(290, 50, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.h2Label.setFont(font)
        self.h2Label.setObjectName("h2Label")
        self.functionTab = QtWidgets.QTabWidget(self.centralwidget)
        self.functionTab.setGeometry(QtCore.QRect(10, 110, 1001, 571))
        self.functionTab.setStyleSheet("background-color: rgb(248, 249, 249);")
        self.functionTab.setTabPosition(QtWidgets.QTabWidget.North)
        self.functionTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.functionTab.setElideMode(QtCore.Qt.ElideNone)
        self.functionTab.setTabsClosable(False)
        self.functionTab.setObjectName("functionTab")
        self.trainTab = QtWidgets.QWidget()
        self.trainTab.setObjectName("trainTab")
        self.importBox = QtWidgets.QGroupBox(self.trainTab)
        self.importBox.setGeometry(QtCore.QRect(10, 10, 971, 71))
        self.importBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.importBox.setObjectName("importBox")

        self.pathLabel = QtWidgets.QLabel(self.importBox)
        self.pathLabel.setGeometry(QtCore.QRect(150, 20, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.pathLabel.setFont(font)
        self.pathLabel.setStyleSheet("color: rgb(121, 121, 121);")
        self.pathLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.pathLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pathLabel.setObjectName("pathLabel")
        self.browseBtn = QtWidgets.QPushButton(self.importBox)
        self.browseBtn.setGeometry(QtCore.QRect(600, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.browseBtn.setFont(font)
        self.browseBtn.setStyleSheet("background-color: rgb(80, 198, 179);\n"
"color: rgb(255, 255, 255);")
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.trainBrowseFile)
        self.importBtn = QtWidgets.QPushButton(self.importBox)
        self.importBtn.setGeometry(QtCore.QRect(700, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.importBtn.setFont(font)
        self.importBtn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.importBtn.setObjectName("importBtn")
        self.importBtn.clicked.connect(self.importFile)

        self.trainBox = QtWidgets.QGroupBox(self.trainTab)
        self.trainBox.setGeometry(QtCore.QRect(10, 90, 971, 171))
        self.trainBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.trainBox.setObjectName("trainBox")
        self.cancelBtn = QtWidgets.QPushButton(self.trainBox)
        self.cancelBtn.setGeometry(QtCore.QRect(410, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cancelBtn.setObjectName("cancelBtn")
        self.trainBtn = QtWidgets.QPushButton(self.trainBox)
        self.trainBtn.setGeometry(QtCore.QRect(490, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.trainBtn.setFont(font)
        self.trainBtn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.trainBtn.setObjectName("trainBtn")
        self.trainBtn.clicked.connect(self.trainButton)


        self.paraBox = QtWidgets.QGroupBox(self.trainBox)
        self.paraBox.setGeometry(QtCore.QRect(160, 20, 321, 101))
        self.paraBox.setAlignment(QtCore.Qt.AlignCenter)
        self.paraBox.setFlat(False)
        self.paraBox.setCheckable(False)
        self.paraBox.setObjectName("paraBox")
        self.consEdit = QtWidgets.QLineEdit(self.paraBox)
        self.consEdit.setGeometry(QtCore.QRect(30, 30, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.consEdit.setFont(font)
        self.consEdit.setObjectName("consEdit")
        self.epsEdit = QtWidgets.QLineEdit(self.paraBox)
        self.epsEdit.setGeometry(QtCore.QRect(170, 30, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.epsEdit.setFont(font)
        self.epsEdit.setObjectName("epsEdit")
        self.pEdit = QtWidgets.QLineEdit(self.paraBox)
        self.pEdit.setGeometry(QtCore.QRect(30, 60, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.pEdit.setFont(font)
        self.pEdit.setObjectName("pEdit")
        self.gamEdit = QtWidgets.QLineEdit(self.paraBox)
        self.gamEdit.setGeometry(QtCore.QRect(170, 60, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.gamEdit.setFont(font)
        self.gamEdit.setObjectName("gamEdit")
        self.kernelBox = QtWidgets.QGroupBox(self.trainBox)
        self.kernelBox.setGeometry(QtCore.QRect(490, 20, 331, 101))
        self.kernelBox.setAlignment(QtCore.Qt.AlignCenter)
        self.kernelBox.setObjectName("kernelBox")
        self.btnRbf = QtWidgets.QRadioButton(self.trainBox)
        self.btnRbf.setGeometry(QtCore.QRect(690, 50, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.btnRbf.setFont(font)
        self.btnRbf.setObjectName("btnRbf")
        self.btnPoly = QtWidgets.QRadioButton(self.trainBox)
        self.btnPoly.setGeometry(QtCore.QRect(550, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.btnPoly.setFont(font)
        self.btnPoly.setObjectName("btnPoly")
        self.btnSigmoid = QtWidgets.QRadioButton(self.trainBox)
        self.btnSigmoid.setGeometry(QtCore.QRect(690, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.btnSigmoid.setFont(font)
        self.btnSigmoid.setObjectName("btnSigmoid")
        self.btnLinear = QtWidgets.QRadioButton(self.trainBox)
        self.btnLinear.setGeometry(QtCore.QRect(550, 50, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.btnLinear.setFont(font)
        self.btnLinear.setObjectName("btnLinear")
        self.resultBox = QtWidgets.QGroupBox(self.trainTab)
        self.resultBox.setGeometry(QtCore.QRect(10, 270, 971, 271))
        self.resultBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resultBox.setObjectName("resultBox")
        self.trainresultTable = QtWidgets.QTableWidget(self.resultBox)
        self.trainresultTable.setGeometry(QtCore.QRect(120, 20, 741, 241))
        self.trainresultTable.setRowCount(48911)
        self.trainresultTable.setColumnCount(10)
        self.trainresultTable.setObjectName("trainresultTable")
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.trainresultTable.setHorizontalHeaderItem(9, item)


        self.functionTab.addTab(self.trainTab, "")
        self.validateTab = QtWidgets.QWidget()
        self.validateTab.setObjectName("validateTab")
        self.validationBox = QtWidgets.QGroupBox(self.validateTab)
        self.validationBox.setGeometry(QtCore.QRect(10, 80, 461, 451))
        self.validationBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.validationBox.setObjectName("validationBox")
        self.valDataTable = QtWidgets.QTableWidget(self.validationBox)
        self.valDataTable.setGeometry(QtCore.QRect(20, 20, 421, 421))
        self.valDataTable.setRowCount(48911)
        self.valDataTable.setColumnCount(10)
        self.valDataTable.setObjectName("valDataTable")
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.valDataTable.setHorizontalHeaderItem(9, item)
        self.valresultBox = QtWidgets.QGroupBox(self.validateTab)
        self.valresultBox.setGeometry(QtCore.QRect(500, 80, 481, 411))
        self.valresultBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valresultBox.setObjectName("valresultBox")
        self.valResulTable = QtWidgets.QTableWidget(self.valresultBox)
        self.valResulTable.setGeometry(QtCore.QRect(20, 20, 441, 381))

        self.valResulTable.setRowCount(48911)
        self.valResulTable.setColumnCount(10)

        self.valResulTable.setObjectName("valResulTable")
        self.valResulTable.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.valResulTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.valResulTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.valResulTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.valResulTable.setHorizontalHeaderItem(3, item)

        self.valimportBox = QtWidgets.QGroupBox(self.validateTab)
        self.valimportBox.setGeometry(QtCore.QRect(10, 10, 461, 61))
        self.valimportBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valimportBox.setObjectName("valimportBox")
        self.valimpLabel = QtWidgets.QLabel(self.valimportBox)
        self.valimpLabel.setGeometry(QtCore.QRect(20, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.valimpLabel.setFont(font)
        self.valimpLabel.setStyleSheet("color: rgb(121, 121, 121);")
        self.valimpLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.valimpLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valimpLabel.setObjectName("valimpLabel")
        self.browseBtn_2 = QtWidgets.QPushButton(self.valimportBox)
        self.browseBtn_2.setGeometry(QtCore.QRect(290, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.browseBtn_2.setFont(font)
        self.browseBtn_2.setStyleSheet("background-color: rgb(80, 198, 179);\n"
"color: rgb(255, 255, 255);")
        self.browseBtn_2.setObjectName("browseBtn_2")
        self.browseBtn_2.clicked.connect(self.validateBrowseFile)



        self.importBtn_2 = QtWidgets.QPushButton(self.valimportBox)
        self.importBtn_2.setGeometry(QtCore.QRect(370, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.importBtn_2.setFont(font)
        self.importBtn_2.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.importBtn_2.setObjectName("importBtn_2")
        self.importBtn_2.clicked.connect(self.importFileValidate)

        self.predictBtn = QtWidgets.QPushButton(self.validateTab)
        self.predictBtn.setGeometry(QtCore.QRect(790, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.predictBtn.setFont(font)
        self.predictBtn.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.predictBtn.setObjectName("predictBtn")
        self.predictBtn.clicked.connect(self.predict)

        self.visualizeBtn = QtWidgets.QPushButton(self.validateTab)
        self.visualizeBtn.setGeometry(QtCore.QRect(890, 500, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.visualizeBtn.setFont(font)
        self.visualizeBtn.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.visualizeBtn.setObjectName("visualizeBtn")

        self.rmseLine = QtWidgets.QLineEdit(self.validateTab)
        self.rmseLine.setGeometry(QtCore.QRect(500, 500, 181, 31))
        self.rmseLine.setFrame(True)
        self.rmseLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rmseLine.setReadOnly(False)
        self.rmseLine.setPlaceholderText("")
        self.rmseLine.setObjectName("rmseLine")
        self.mapeLine = QtWidgets.QLineEdit(self.validateTab)
        self.mapeLine.setGeometry(QtCore.QRect(690, 500, 181, 31))
        self.mapeLine.setObjectName("mapeLine")
        self.functionTab.addTab(self.validateTab, "")
        self.forecastTab = QtWidgets.QWidget()
        self.forecastTab.setObjectName("forecastTab")
        self.forecastBox = QtWidgets.QGroupBox(self.forecastTab)
        self.forecastBox.setGeometry(QtCore.QRect(10, 60, 461, 471))
        self.forecastBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.forecastBox.setObjectName("forecastBox")
        self.foreDataTable = QtWidgets.QTableWidget(self.forecastBox)
        self.foreDataTable.setGeometry(QtCore.QRect(20, 30, 421, 431))
        self.foreDataTable.setRowCount(48911)
        self.foreDataTable.setColumnCount(10)
        self.foreDataTable.setObjectName("foreDataTable")
        item = QtWidgets.QTableWidgetItem()

        self.foreDataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreDataTable.setHorizontalHeaderItem(9, item)


        self.foreresultBox = QtWidgets.QGroupBox(self.forecastTab)
        self.foreresultBox.setGeometry(QtCore.QRect(500, 60, 471, 471))
        self.foreresultBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.foreresultBox.setObjectName("foreresultBox")
        self.foreResultTable = QtWidgets.QTableWidget(self.foreresultBox)
        self.foreResultTable.setGeometry(QtCore.QRect(120, 30, 231, 421))
        self.foreResultTable.setRowCount(144)
        self.foreResultTable.setObjectName("foreResultTable")
        self.foreResultTable.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.foreResultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.foreResultTable.setHorizontalHeaderItem(1, item)

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.forecastBtn = QtWidgets.QPushButton(self.forecastTab)
        self.forecastBtn.setGeometry(QtCore.QRect(780, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.forecastBtn.setFont(font)
        self.forecastBtn.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.forecastBtn.setObjectName("forecastBtn")
        self.forecastBtn.clicked.connect(self.predict_predict)

        self.functionTab.addTab(self.forecastTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionSave_File_As = QtWidgets.QAction(MainWindow)
        self.actionSave_File_As.setObjectName("actionSave_File_As")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionSave_File_As)
        self.menuFile.addAction(self.actionQuit)
        self.menuSystem.addAction(self.actionAbout)
        self.menuSystem.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(MainWindow)
        self.functionTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SVRM Forecasting System"))
        self.h1Label.setText(_translate("MainWindow", "Water Level Forecasting System"))
        self.h2Label.setText(_translate("MainWindow", "Using Support Vector Regression Machine"))
        self.importBox.setTitle(_translate("MainWindow", "Import"))
        self.pathLabel.setText(_translate("MainWindow", "File Path"))
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.importBtn.setText(_translate("MainWindow", "Import"))
        self.trainBox.setTitle(_translate("MainWindow", "Train"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.trainBtn.setText(_translate("MainWindow", "Train"))
        self.paraBox.setTitle(_translate("MainWindow", "Input Parameters"))
        self.consEdit.setPlaceholderText(_translate("MainWindow", "C"))
        self.epsEdit.setPlaceholderText(_translate("MainWindow", "ε"))
        self.pEdit.setPlaceholderText(_translate("MainWindow", "P"))
        self.gamEdit.setPlaceholderText(_translate("MainWindow", " γ"))
        self.kernelBox.setTitle(_translate("MainWindow", "Select Kernel"))
        self.btnRbf.setText(_translate("MainWindow", "RBF"))
        self.btnPoly.setText(_translate("MainWindow", "Polynomial"))
        self.btnSigmoid.setText(_translate("MainWindow", "Sigmoid"))
        self.btnLinear.setText(_translate("MainWindow", "Linear"))
        self.resultBox.setTitle(_translate("MainWindow", "Results"))

        item = self.trainresultTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "WATERLEVEL"))
        item = self.trainresultTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RF_DIGKILAAN"))
        item = self.trainresultTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RF_ROGONGON"))
        item = self.trainresultTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Day"))
        item = self.trainresultTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        item = self.trainresultTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Month"))
        item = self.trainresultTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Year"))
        item = self.trainresultTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "i - 1"))
        item = self.trainresultTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "i - 2"))
        item = self.trainresultTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "i - 3"))
        self.functionTab.setTabText(self.functionTab.indexOf(self.trainTab), _translate("MainWindow", "Train"))
        self.validationBox.setTitle(_translate("MainWindow", "Validation Data"))
        item = self.valDataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "WATERLEVEL"))
        item = self.valDataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RF_DIGKILAAN"))
        item = self.valDataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Day"))
        item = self.valDataTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time"))
        item = self.valDataTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Month"))
        item = self.valDataTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Year"))
        item = self.valDataTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "RF_ROGONGON"))
        item = self.valDataTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "i - 1"))
        item = self.valDataTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "i - 2"))
        item = self.valDataTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "i - 3"))
        self.valresultBox.setTitle(_translate("MainWindow", "Results"))

        item = self.valResulTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "WATERLEVEL (Actual)"))
        item = self.valResulTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "WATERLEVEL (Predicted)"))
        item = self.valResulTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RMSE"))
        item = self.valResulTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MAPE"))
        self.valimportBox.setTitle(_translate("MainWindow", "Import"))
        self.valimpLabel.setText(_translate("MainWindow", "File Path"))
        self.browseBtn_2.setText(_translate("MainWindow", "Browse"))
        self.importBtn_2.setText(_translate("MainWindow", "Import"))
        self.predictBtn.setText(_translate("MainWindow", "Predict"))
        self.visualizeBtn.setText(_translate("MainWindow", "View Graph"))
        self.rmseLine.setText(_translate("MainWindow", "Average RMSE ="))
        self.mapeLine.setText(_translate("MainWindow", "Average MAPE = "))
        self.functionTab.setTabText(self.functionTab.indexOf(self.validateTab), _translate("MainWindow", "Validate"))
        self.forecastBox.setTitle(_translate("MainWindow", "Forecasting Data"))


        item = self.foreDataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "WATERLEVEL"))
        item = self.foreDataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RF_DIGKILAAN"))
        item = self.foreDataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RF_ROGONGON"))
        item = self.foreDataTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Day"))
        item = self.foreDataTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        item = self.foreDataTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Month"))
        item = self.foreDataTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Year"))
        item = self.foreDataTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "i - 1"))
        item = self.foreDataTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "i - 2"))
        item = self.foreDataTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "i - 3"))

        self.foreresultBox.setTitle(_translate("MainWindow", "Results"))
        item = self.foreResultTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATETIME"))
        item = self.foreResultTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "WATERLEVEL (Forecasted)"))
        self.forecastBtn.setText(_translate("MainWindow", "Forecast"))

        self.functionTab.setTabText(self.functionTab.indexOf(self.forecastTab), _translate("MainWindow", "Forecast"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSystem.setTitle(_translate("MainWindow", "System"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionSave_File_As.setText(_translate("MainWindow", "Save File As..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

        df = pd.read_csv('D:/Aug/waterlevel_forecastingsystem/Trained/merged_imputation_f.csv')
        for i in range(0,df.shape[1]):
            for j in range(0, df.shape[0]):
                 self.foreDataTable.setItem(j,i, QtWidgets.QTableWidgetItem(str(df.iloc[j][i])))




    def trainBrowseFile(self):
        options = QtWidgets.QFileDialog.Options()
        file = QtWidgets.QFileDialog.getOpenFileName(None, 'Import Data', '', 'All Files (*)::CSV Files (*.csv)', options=options)
        self.pathLabel.setText(str(file[0]))



        if file:
            return file

    def trainButton(self):

        file = "D:/Aug/waterlevel_forecastingsystem/NT/merged_imputation_f_nt.csv"
        print(file)
        print(self.consEdit.text())
        print(self.epsEdit.text())
        print(self.pEdit.text())
        print(self.gamEdit.text())

        cons = int(self.consEdit.text())
        eps = int(self.epsEdit.text())
        p = int(self.pEdit.text())
        gam = int(self.gamEdit.text())

        button_ = ""

        buttons = [self.btnRbf,self.btnPoly,self.btnSigmoid,self.btnLinear]
        for button in buttons:
            if button.isChecked():
                print(button.text())
                button_ = button.text()
                if button_ == "Polynomial":
                    button_ = "Poly"
        print(button_)


        df = run_nt(file, button_, cons, eps, p, gam)

        print(df)
        df.to_csv("D:/Aug/waterlevel_forecastingsystem/Trained/merged_imputation_f.csv",  index=False)
        print(df.iloc[0][1])


        for i in range(0,df.shape[1]):
            for j in range(0, df.shape[0]):
                 self.trainresultTable.setItem(j,i, QtWidgets.QTableWidgetItem(str(df.iloc[j][i])))



    def validateBrowseFile(self):
        options = QtWidgets.QFileDialog.Options()
        file = QtWidgets.QFileDialog.getOpenFileName(None, 'Import Data', '', 'All Files (*)::CSV Files (*.csv)', options=options)
        if file:
            self.valimpLabel.setText(str(file[0]))




    def importFile(self):

        file_new = self.pathLabel.text()
        status = shutil.copyfile(str(file_new), "D:/Aug/waterlevel_forecastingsystem/NT/merged_imputation_f_nt.csv")
        print(str(status) + '-' + "Success")

    def importFileValidate(self):

        file_new = self.valimpLabel.text()
        status = shutil.copyfile(str(file_new),"D:/Aug/waterlevel_forecastingsystem/Trained/merged_imputation_f.csv")
        print(str(status) + '-' + "Success")

        file = open("D:/Aug/waterlevel_forecastingsystem/Trained/merged_imputation_f.csv")



        df = pd.read_csv(file)



        for i in range(0,df.shape[1]):
            for j in range(0, df.shape[0]):
                 self.valDataTable.setItem(j,i, QtWidgets.QTableWidgetItem(str(df.iloc[j][i])))


    def predict(self):
        file = "D:/Aug/waterlevel_forecastingsystem/Trained/merged_imputation_f.csv"
        cons = int(self.consEdit.text())
        eps = int(self.epsEdit.text())
        p = int(self.pEdit.text())
        gam = int(self.gamEdit.text())

        button_ = ""

        buttons = [self.btnRbf,self.btnPoly,self.btnSigmoid,self.btnLinear]
        for button in buttons:
            if button.isChecked():
                print(button.text())
                button_ = button.text()
                if button_ == "Polynomial":
                    button_ = "Poly"
        print(button_)

        df = pd.read_csv(file)
        val = validate(df, button_, cons, eps, p, gam)
        print(val)
 

        self.valResulTable.setRowCount(val.shape[0])
        self.valResulTable.setColumnCount(val.shape[1])

        for i in range(0,val.shape[1]):
            for j in range(0, val.shape[0]):
                 self.valResulTable.setItem(j,i, QtWidgets.QTableWidgetItem(str(val.iloc[j][i])))


    def predict_predict(self):
        file = "D:/Aug/waterlevel_forecastingsystem/Trained/merged_imputation_f.csv"

        cons = int(self.consEdit.text())
        eps = int(self.epsEdit.text())
        p = int(self.pEdit.text())
        gam = int(self.gamEdit.text())

        button_ = ""

        buttons = [self.btnRbf,self.btnPoly,self.btnSigmoid,self.btnLinear]
        for button in buttons:
            if button.isChecked():
                print(button.text())
                button_ = button.text()
                if button_ == "Polynomial":
                    button_ = "Poly"
        print(button_)

        df = pd.read_csv(file)
        val = validate(df, button_, cons, eps, p, gam)
        print(val)

        dates = get_date_time_after()

        val.drop(['RMSE','MAPE','WATERLVEL'], axis=1, inplace=True)
        val['Predicted'] = df['Predicted'].iloc[:len(dates)]
        val['DATETIME'] = dates
        val[['DATETIME','Predicted']]


        for i in range(0,val.shape[1]):
            for j in range(0, val.shape[0]):
                 self.foreResultTable.setItem(j,i, QtWidgets.QTableWidgetItem(str(val.iloc[j][i])))

import qtresources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
