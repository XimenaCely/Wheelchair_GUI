# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manual_control_uiIsnOSR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
"""
Copyright [2023] [Aura Ximena Gonzalez Cely]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_manual_window(object):
    def setupUi(self, manual_window):
        if not manual_window.objectName():
            manual_window.setObjectName(u"manual_window")
        manual_window.resize(700, 411)
        manual_window.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(manual_window)
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
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 10, 451, 91))
        font3 = QFont()
        font3.setFamily(u"Lucida Sans")
        font3.setPointSize(14)
        self.label_2.setFont(font3)
        self.start_wizard_btn = QPushButton(self.page_3)
        self.start_wizard_btn.setObjectName(u"start_wizard_btn")
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
        self.nxt = QPushButton(self.page)
        self.nxt.setObjectName(u"nxt")
        self.nxt.setGeometry(QRect(590, 230, 71, 61))
        icon2 = QIcon()
        icon2.addFile(u":/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nxt.setIcon(icon2)
        self.nxt.setIconSize(QSize(64, 64))
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(510, 130, 31, 31))
        self.label_6.setPixmap(QPixmap(u":/icons/arrow-down-circle.svg"))
        self.label_6.setScaledContents(True)
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(470, 100, 31, 31))
        self.label_8.setPixmap(QPixmap(u":/icons/arrow-left-circle.svg"))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(550, 100, 31, 31))
        self.label_9.setPixmap(QPixmap(u":/icons/arrow-right-circle.svg"))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(510, 60, 31, 31))
        self.label_10.setPixmap(QPixmap(u":/icons/arrow-up-circle.svg"))
        self.label_10.setScaledContents(True)
        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(550, 60, 31, 31))
        self.label_11.setPixmap(QPixmap(u":/icons/arrow-up-right.svg"))
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(470, 60, 31, 31))
        self.label_12.setPixmap(QPixmap(u":/icons/arrow-up-left.svg"))
        self.label_12.setScaledContents(True)
        self.label_13 = QLabel(self.page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(550, 130, 31, 31))
        self.label_13.setPixmap(QPixmap(u":/icons/arrow-down-right.svg"))
        self.label_13.setScaledContents(True)
        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(470, 130, 31, 31))
        self.label_14.setPixmap(QPixmap(u":/icons/arrow-down-left.svg"))
        self.label_14.setScaledContents(True)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.velocimeter = QScrollBar(self.page_2)
        self.velocimeter.setObjectName(u"velocimeter")
        self.velocimeter.setGeometry(QRect(530, 20, 71, 251))
        self.velocimeter.setOrientation(Qt.Vertical)
        self.prev = QPushButton(self.page_2)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(0, 230, 81, 61))
        icon3 = QIcon()
        icon3.addFile(u":/icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon3)
        self.prev.setIconSize(QSize(64, 64))
        self.buttons = QFrame(self.page_2)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setGeometry(QRect(130, 10, 351, 291))
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.buttons)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stop_btn = QPushButton(self.buttons)
        self.stop_btn.setObjectName(u"stop_btn")
        font5 = QFont()
        font5.setFamily(u"Lucida Sans")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.stop_btn.setFont(font5)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-stop-sign-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon4)
        self.stop_btn.setIconSize(QSize(128, 128))

        self.gridLayout_2.addWidget(self.stop_btn, 1, 1, 1, 1)

        self.up_btn = QPushButton(self.buttons)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setStyleSheet(u"image: url(:/icons/triangle.png);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_btn.setIcon(icon5)
        self.up_btn.setIconSize(QSize(84, 84))

        self.gridLayout_2.addWidget(self.up_btn, 0, 1, 1, 1)

        self.diag_upr_btn = QPushButton(self.buttons)
        self.diag_upr_btn.setObjectName(u"diag_upr_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/diagonal-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.diag_upr_btn.setIcon(icon6)
        self.diag_upr_btn.setIconSize(QSize(74, 74))

        self.gridLayout_2.addWidget(self.diag_upr_btn, 0, 2, 1, 1)

        self.diag_upl_btn = QPushButton(self.buttons)
        self.diag_upl_btn.setObjectName(u"diag_upl_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/diagonal-arrow_right1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.diag_upl_btn.setIcon(icon7)
        self.diag_upl_btn.setIconSize(QSize(74, 74))

        self.gridLayout_2.addWidget(self.diag_upl_btn, 0, 0, 1, 1)

        self.left_btn = QPushButton(self.buttons)
        self.left_btn.setObjectName(u"left_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_btn.setIcon(icon8)
        self.left_btn.setIconSize(QSize(84, 84))

        self.gridLayout_2.addWidget(self.left_btn, 1, 0, 1, 1)

        self.diag_downl_btn = QPushButton(self.buttons)
        self.diag_downl_btn.setObjectName(u"diag_downl_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/diagonal-arrw_right2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.diag_downl_btn.setIcon(icon9)
        self.diag_downl_btn.setIconSize(QSize(74, 74))

        self.gridLayout_2.addWidget(self.diag_downl_btn, 2, 0, 1, 1)

        self.down_btn = QPushButton(self.buttons)
        self.down_btn.setObjectName(u"down_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.down_btn.setIcon(icon10)
        self.down_btn.setIconSize(QSize(84, 84))

        self.gridLayout_2.addWidget(self.down_btn, 2, 1, 1, 1)

        self.diag_downr_btn = QPushButton(self.buttons)
        self.diag_downr_btn.setObjectName(u"diag_downr_btn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/diagonal-arrow_left1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.diag_downr_btn.setIcon(icon11)
        self.diag_downr_btn.setIconSize(QSize(74, 74))

        self.gridLayout_2.addWidget(self.diag_downr_btn, 2, 2, 1, 1)

        self.right_btn = QPushButton(self.buttons)
        self.right_btn.setObjectName(u"right_btn")
        self.right_btn.setIcon(icon8)
        self.right_btn.setIconSize(QSize(84, 84))

        self.gridLayout_2.addWidget(self.right_btn, 1, 2, 1, 1)

        self.stop_btn.raise_()
        self.diag_upr_btn.raise_()
        self.diag_upl_btn.raise_()
        self.diag_downl_btn.raise_()
        self.diag_downr_btn.raise_()
        self.up_btn.raise_()
        self.left_btn.raise_()
        self.down_btn.raise_()
        self.right_btn.raise_()
        self.stackedWidget.addWidget(self.page_2)

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
        icon12 = QIcon()
        icon12.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon12)
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

        manual_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(manual_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(manual_window)
    # setupUi

    def retranslateUi(self, manual_window):
        manual_window.setWindowTitle(QCoreApplication.translate("manual_window", u"MainWindow", None))
        self.return_btn.setText(QCoreApplication.translate("manual_window", u"Main Menu", None))
        self.label.setText("")
        self.main_title.setText(QCoreApplication.translate("manual_window", u"<html><head/><body><p><span style=\" color:#ffffff;\">Smart wheelchair</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("manual_window", u"<html><head/><body><p align=\"center\">Welcome to manual control!</p><p align=\"center\">You can turn on the system click on the button</p></body></html>", None))
        self.start_wizard_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("manual_window", u"<html><head/><body><p align=\"justify\">Please click on the buttons in the direction you want to operate the system. </p><p align=\"justify\">You also have a velocity bar to change the speed of the wheelchair.</p><p align=\"justify\">You have an emergency button to stop the system.</p><p align=\"justify\">To come back and start the controller next page have a return button for that.</p><p align=\"justify\">Let's go to operate the wheelchair!</p></body></html>", None))
        self.nxt.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.prev.setText("")
        self.stop_btn.setText("")
        self.up_btn.setText("")
        self.diag_upr_btn.setText("")
        self.diag_upl_btn.setText("")
        self.left_btn.setText("")
        self.diag_downl_btn.setText("")
        self.down_btn.setText("")
        self.diag_downr_btn.setText("")
        self.right_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("manual_window", u"<html><head/><body><p><span style=\" color:#ffffff;\">Version 1.0 Copyright AXGC</span></p></body></html>", None))
        self.info_btn.setText("")
    # retranslateUi

