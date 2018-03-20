# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\python-skeleton\python_skeleton\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.layout = QtWidgets.QVBoxLayout(self.widget)
        self.layout.setObjectName("layout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setPixmap(QtGui.QPixmap(":/static/img/img.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layout.addWidget(self.label)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HelloWorld"))

from . import main_rc
