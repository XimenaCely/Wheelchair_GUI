# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'neck_control_uiLAahWz.ui'
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
import icons_rc

class Ui_neck_window(object):
    def setupUi(self, neck_window):
        if not neck_window.objectName():
            neck_window.setObjectName(u"neck_window")
        neck_window.resize(700, 411)
        neck_window.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(neck_window)
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
        self.start_wizard_btn.setGeometry(QRect(220, 130, 161, 141))
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
        self.neck_pillow_guide = QLabel(self.page)
        self.neck_pillow_guide.setObjectName(u"neck_pillow_guide")
        self.neck_pillow_guide.setGeometry(QRect(350, 20, 301, 211))
        self.neck_pillow_guide.setPixmap(QPixmap(u":/icons/neck.png"))
        self.neck_pillow_guide.setScaledContents(True)
        self.up_right = QLabel(self.page)
        self.up_right.setObjectName(u"up_right")
        self.up_right.setGeometry(QRect(460, 180, 31, 31))
        self.up_right.setPixmap(QPixmap(u":/icons/spiral.png"))
        self.up_right.setScaledContents(True)
        self.up_left = QLabel(self.page)
        self.up_left.setObjectName(u"up_left")
        self.up_left.setGeometry(QRect(510, 180, 31, 31))
        self.up_left.setPixmap(QPixmap(u":/icons/spiral.png"))
        self.up_left.setScaledContents(True)
        self.left_label = QLabel(self.page)
        self.left_label.setObjectName(u"left_label")
        self.left_label.setGeometry(QRect(430, 110, 31, 31))
        self.left_label.setPixmap(QPixmap(u":/icons/spiral.png"))
        self.left_label.setScaledContents(True)
        self.right_label = QLabel(self.page)
        self.right_label.setObjectName(u"right_label")
        self.right_label.setGeometry(QRect(550, 110, 31, 31))
        self.right_label.setPixmap(QPixmap(u":/icons/spiral.png"))
        self.right_label.setScaledContents(True)
        self.back_label = QLabel(self.page)
        self.back_label.setObjectName(u"back_label")
        self.back_label.setGeometry(QRect(490, 60, 31, 31))
        self.back_label.setPixmap(QPixmap(u":/icons/spiral.png"))
        self.back_label.setScaledContents(True)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stop_btn = QPushButton(self.page_2)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setGeometry(QRect(90, 30, 281, 161))
        font5 = QFont()
        font5.setFamily(u"Lucida Sans")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.stop_btn.setFont(font5)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-stop-sign-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon3)
        self.stop_btn.setIconSize(QSize(128, 128))
        self.velocimeter = QScrollBar(self.page_2)
        self.velocimeter.setObjectName(u"velocimeter")
        self.velocimeter.setGeometry(QRect(460, 0, 71, 251))
        self.velocimeter.setOrientation(Qt.Vertical)
        self.prev = QPushButton(self.page_2)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(0, 230, 71, 61))
        icon4 = QIcon()
        icon4.addFile(u":/icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon4)
        self.prev.setIconSize(QSize(64, 64))
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 270, 301, 31))
        self.label_3.setFont(font4)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon5)
        self.info_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.info_btn, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip_2 = QFrame(self.footer_frame)
        self.size_grip_2.setObjectName(u"size_grip_2")
        self.size_grip_2.setMinimumSize(QSize(10, 10))
        self.size_grip_2.setMaximumSize(QSize(10, 10))
        self.size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.size_grip_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip_2)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        neck_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(neck_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(neck_window)
    # setupUi

    def retranslateUi(self, neck_window):
        neck_window.setWindowTitle(QCoreApplication.translate("neck_window", u"MainWindow", None))
        self.return_btn.setText(QCoreApplication.translate("neck_window", u"Main Menu", None))
        self.label.setText("")
        self.main_title.setText(QCoreApplication.translate("neck_window", u"<html><head/><body><p><span style=\" color:#ffffff;\">Smart wheelchair</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("neck_window", u"<html><head/><body><p align=\"center\">Welcome to neck control!</p><p align=\"center\">You can turn on the system click on the button</p></body></html>", None))
        self.start_wizard_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("neck_window", u"<html><head/><body><p align=\"justify\">Please move your neck in the direction you want to operate the wheelchair.</p><p align=\"justify\">The image is showing the place you can make pressure in the pillow.</p><p align=\"justify\">You also have a scroll bar to change the velocity of the wheelchair in the next page. </p><p align=\"justify\">You have an emergency button to stop the system.</p><p align=\"justify\">To come back and start the controller next page have a return button for that.</p><p align=\"justify\">Let's go to operate the wheelchair!</p></body></html>", None))
        self.nxt.setText("")
        self.neck_pillow_guide.setText("")
        self.up_right.setText("")
        self.up_left.setText("")
        self.left_label.setText("")
        self.right_label.setText("")
        self.back_label.setText("")
        self.stop_btn.setText(QCoreApplication.translate("neck_window", u"Emergency button", None))
        self.prev.setText("")
        self.label_3.setText(QCoreApplication.translate("neck_window", u"Change the velocity of the wheelchair", None))
        self.label_4.setText(QCoreApplication.translate("neck_window", u"<html><head/><body><p><span style=\" color:#ffffff;\">Version 1.0 Copyright AXGC</span></p></body></html>", None))
        self.info_btn.setText("")
    # retranslateUi

