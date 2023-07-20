# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'posture_monitoring_uiChhTXn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_posture_window(object):
    def setupUi(self, posture_window):
        if not posture_window.objectName():
            posture_window.setObjectName(u"posture_window")
        posture_window.resize(700, 411)
        posture_window.setStyleSheet(u"*{\n"
"	background-color: rgb(66, 66, 66);\n"
"	border: none;\n"
"	background: none;\n"
"	color: #fff;\n"
"}\n"
"QPushButton, QLineEdit, QCheckBox{\n"
"	background-color:rgba(10,16,27,150);\n"
"	padding: 7px;\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(posture_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(699, 411))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(0, 67, 98);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.return_btn = QPushButton(self.header_left_frame)
        self.return_btn.setObjectName(u"return_btn")
        font = QFont()
        font.setFamily(u"Lucida Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.return_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.return_btn.setIcon(icon)
        self.return_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.return_btn)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u":/icons/wheelchair.png"))

        self.horizontalLayout_3.addWidget(self.label)

        self.main_title = QLabel(self.header_center_frame)
        self.main_title.setObjectName(u"main_title")
        font2 = QFont()
        font2.setFamily(u"Lucida Sans")
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.main_title.setFont(font2)

        self.horizontalLayout_3.addWidget(self.main_title)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.header_right_frame)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(300, 325))
        self.main_frame.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pages = QFrame(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pages.setMinimumSize(QSize(0, 0))
        self.pages.setMaximumSize(QSize(16777215, 16777215))
        self.pages.setFrameShape(QFrame.StyledPanel)
        self.pages.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.pages)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(20, 0, 661, 311))
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 661, 311))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 621, 91))
        font3 = QFont()
        font3.setFamily(u"Lucida Sans")
        font3.setPointSize(14)
        self.label_2.setFont(font3)
        self.start_wizard_btn = QPushButton(self.page_3)
        self.start_wizard_btn.setObjectName(u"start_wizard_btn")
        self.start_wizard_btn.setEnabled(True)
        self.start_wizard_btn.setGeometry(QRect(210, 130, 181, 141))
        self.start_wizard_btn.setMinimumSize(QSize(100, 0))
        self.start_wizard_btn.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/power-on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_wizard_btn.setIcon(icon1)
        self.start_wizard_btn.setIconSize(QSize(128, 128))
        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 331, 281))
        font4 = QFont()
        font4.setFamily(u"Lucida Sans")
        font4.setPointSize(12)
        self.label_5.setFont(font4)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"\n"
"background-color: rgb(66, 66, 66);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.footer_left_frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setStyleSheet(u"background-color: rgb(66,66, 66);")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_right_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.info_btn = QPushButton(self.footer_right_frame)
        self.info_btn.setObjectName(u"info_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon2)
        self.info_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.info_btn, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip_2 = QFrame(self.footer_frame)
        self.size_grip_2.setObjectName(u"size_grip_2")
        self.size_grip_2.setMinimumSize(QSize(10, 10))
        self.size_grip_2.setMaximumSize(QSize(10, 10))
        self.size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.size_grip_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip_2, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        posture_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(posture_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(posture_window)
    # setupUi

    def retranslateUi(self, posture_window):
        posture_window.setWindowTitle(QCoreApplication.translate("posture_window", u"MainWindow", None))
        self.return_btn.setText(QCoreApplication.translate("posture_window", u"Main Menu", None))
        self.label.setText("")
        self.main_title.setText(QCoreApplication.translate("posture_window", u"<html><head/><body><p><span style=\" color:#ffffff;\">Smart wheelchair</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("posture_window", u"<html><head/><body><p align=\"center\">Welcome to monitoring your system!</p><p align=\"center\">You can turn on the system clicking on the button</p></body></html>", None))
        self.start_wizard_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("posture_window", u"<html><head/><body><p align=\"justify\">Please click on the buttons in the direction you want to operate the system. </p><p align=\"justify\">You also have a velocity bar to change the speed of the wheelchair.</p><p align=\"justify\">You have an emergency button to stop the system.</p><p align=\"justify\">To come back and start the controller next page have a return button for that.</p><p align=\"justify\">Let's go to operate the wheelchair!</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("posture_window", u"<html><head/><body><p><span style=\" color:#ffffff;\">Version 1.0 Copyright AXGC</span></p></body></html>", None))
        self.info_btn.setText("")
    # retranslateUi

