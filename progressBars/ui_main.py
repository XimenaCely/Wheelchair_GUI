# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBcLupO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 266)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBarContainer = QFrame(self.centralwidget)
        self.progressBarContainer.setObjectName(u"progressBarContainer")
        self.progressBarContainer.setFrameShape(QFrame.StyledPanel)
        self.progressBarContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.progressBarContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = roundProgressBar(self.progressBarContainer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 200))
        self.progressBar.setMaximumSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.progressBarContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

