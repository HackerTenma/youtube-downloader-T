# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 214)
        MainWindow.setMinimumSize(QtCore.QSize(571, 214))
        MainWindow.setMaximumSize(QtCore.QSize(571, 214))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 531, 124))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_pegar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_pegar.setObjectName("pushButton_pegar")
        self.gridLayout_3.addWidget(self.pushButton_pegar, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_descargar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_descargar.setEnabled(False)
        self.pushButton_descargar.setObjectName("pushButton_descargar")
        self.horizontalLayout_5.addWidget(self.pushButton_descargar)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.lineEdit_directorio = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_directorio.setObjectName("lineEdit_directorio")
        self.gridLayout_3.addWidget(self.lineEdit_directorio, 2, 0, 1, 1)
        self.pushButton_guardar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_guardar.setObjectName("pushButton_guardar")
        self.gridLayout_3.addWidget(self.pushButton_guardar, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.lineEdit_link = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_link.setObjectName("lineEdit_link")
        self.gridLayout_3.addWidget(self.lineEdit_link, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader T"))
        self.pushButton_pegar.setText(_translate("MainWindow", "Pegar"))
        self.pushButton_descargar.setText(_translate("MainWindow", "Descargar"))
        self.lineEdit_directorio.setPlaceholderText(_translate("MainWindow", "Directorio del video"))
        self.pushButton_guardar.setText(_translate("MainWindow", "Guardar"))
        self.lineEdit_link.setPlaceholderText(_translate("MainWindow", "Link del video"))
