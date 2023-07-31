# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'neck_control_uiUgHgQQ.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(699, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.open_close_side_bar_btn = QPushButton(self.header_left_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setFamily(u"Lucida Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.open_close_side_bar_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        self.main_body_frame.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame_2 = QFrame(self.main_body_frame)
        self.left_menu_cont_frame_2.setObjectName(u"left_menu_cont_frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu_cont_frame_2.sizePolicy().hasHeightForWidth())
        self.left_menu_cont_frame_2.setSizePolicy(sizePolicy)
        self.left_menu_cont_frame_2.setMinimumSize(QSize(42, 0))
        self.left_menu_cont_frame_2.setMaximumSize(QSize(42, 16777215))
        self.left_menu_cont_frame_2.setStyleSheet(u"background-color: rgb(0, 67, 98);")
        self.left_menu_cont_frame_2.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.left_menu_cont_frame_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.menu_frame_2 = QFrame(self.left_menu_cont_frame_2)
        self.menu_frame_2.setObjectName(u"menu_frame_2")
        self.menu_frame_2.setMinimumSize(QSize(100, 0))
        self.menu_frame_2.setStyleSheet(u"background-color: rgb(0, 67, 98);")
        self.menu_frame_2.setFrameShape(QFrame.StyledPanel)
        self.menu_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.menu_frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.menu_frame_2)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setFamily(u"Lucida Sans")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_16.setFont(font3)
        self.label_16.setMargin(5)

        self.gridLayout_7.addWidget(self.label_16, 10, 1, 1, 1, Qt.AlignLeft)

        self.battery_page_btn_2 = QPushButton(self.menu_frame_2)
        self.battery_page_btn_2.setObjectName(u"battery_page_btn_2")
        icon4 = QIcon()
        icon4.addFile(u":/icons/battery_charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_page_btn_2.setIcon(icon4)
        self.battery_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.battery_page_btn_2, 2, 0, 1, 1, Qt.AlignLeft)

        self.settings_page_btn_2 = QPushButton(self.menu_frame_2)
        self.settings_page_btn_2.setObjectName(u"settings_page_btn_2")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_page_btn_2.setIcon(icon5)
        self.settings_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.settings_page_btn_2, 9, 0, 1, 1, Qt.AlignLeft)

        self.exit_page_btn_2 = QPushButton(self.menu_frame_2)
        self.exit_page_btn_2.setObjectName(u"exit_page_btn_2")
        icon6 = QIcon()
        icon6.addFile(u":/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_page_btn_2.setIcon(icon6)
        self.exit_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.exit_page_btn_2, 10, 0, 1, 1, Qt.AlignLeft)

        self.label_28 = QLabel(self.menu_frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setMargin(5)

        self.gridLayout_7.addWidget(self.label_28, 9, 1, 1, 1, Qt.AlignLeft)

        self.networks_page_btn_2 = QPushButton(self.menu_frame_2)
        self.networks_page_btn_2.setObjectName(u"networks_page_btn_2")
        icon7 = QIcon()
        icon7.addFile(u":/icons/rss.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_page_btn_2.setIcon(icon7)
        self.networks_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.networks_page_btn_2, 5, 0, 1, 1, Qt.AlignLeft)

        self.label_29 = QLabel(self.menu_frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setMargin(5)

        self.gridLayout_7.addWidget(self.label_29, 5, 1, 1, 1, Qt.AlignLeft)

        self.label_30 = QLabel(self.menu_frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)
        self.label_30.setMargin(5)

        self.gridLayout_7.addWidget(self.label_30, 2, 1, 1, 1, Qt.AlignLeft)

        self.system_page_btn_2 = QPushButton(self.menu_frame_2)
        self.system_page_btn_2.setObjectName(u"system_page_btn_2")
        icon8 = QIcon()
        icon8.addFile(u":/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_page_btn_2.setIcon(icon8)
        self.system_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.system_page_btn_2, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_34 = QLabel(self.menu_frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setMargin(5)

        self.gridLayout_7.addWidget(self.label_34, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_35 = QLabel(self.menu_frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setMargin(5)

        self.gridLayout_7.addWidget(self.label_35, 4, 1, 1, 1, Qt.AlignLeft)

        self.home_page_btn_2 = QPushButton(self.menu_frame_2)
        self.home_page_btn_2.setObjectName(u"home_page_btn_2")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-proximity-sensor-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_page_btn_2.setIcon(icon9)
        self.home_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.home_page_btn_2, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_40 = QLabel(self.menu_frame_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)
        self.label_40.setMargin(5)

        self.gridLayout_7.addWidget(self.label_40, 1, 1, 1, 1, Qt.AlignLeft)

        self.sensors_page_btn_2 = QPushButton(self.menu_frame_2)
        self.sensors_page_btn_2.setObjectName(u"sensors_page_btn_2")
        icon10 = QIcon()
        icon10.addFile(u":/icons/speedometer-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_page_btn_2.setIcon(icon10)
        self.sensors_page_btn_2.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.sensors_page_btn_2, 4, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_15.addWidget(self.menu_frame_2, 0, Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.left_menu_cont_frame_2)

        self.main_body_contents_2 = QFrame(self.main_body_frame)
        self.main_body_contents_2.setObjectName(u"main_body_contents_2")
        self.main_body_contents_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.main_body_contents_2.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_body_contents_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_14.addWidget(self.main_body_contents_2)

        self.right_frame_2 = QFrame(self.main_body_frame)
        self.right_frame_2.setObjectName(u"right_frame_2")
        self.right_frame_2.setMaximumSize(QSize(0, 16777215))
        self.right_frame_2.setStyleSheet(u"background-color: rgb(0, 67, 98);")
        self.right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.right_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.right_frame_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.contact_info_frame_2 = QFrame(self.right_frame_2)
        self.contact_info_frame_2.setObjectName(u"contact_info_frame_2")
        self.contact_info_frame_2.setFrameShape(QFrame.StyledPanel)
        self.contact_info_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.contact_info_frame_2)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.contact_info_frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_69 = QLabel(self.frame_10)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_69)

        self.label_70 = QLabel(self.frame_10)
        self.label_70.setObjectName(u"label_70")
        font4 = QFont()
        font4.setFamily(u"Lucida Sans")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_70.setFont(font4)

        self.verticalLayout_12.addWidget(self.label_70)

        self.instagram_btn_2 = QPushButton(self.frame_10)
        self.instagram_btn_2.setObjectName(u"instagram_btn_2")
        self.instagram_btn_2.setMinimumSize(QSize(50, 50))
        self.instagram_btn_2.setFont(font)
        icon11 = QIcon()
        icon11.addFile(u":/icons/instagram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.instagram_btn_2.setIcon(icon11)
        self.instagram_btn_2.setIconSize(QSize(32, 32))

        self.verticalLayout_12.addWidget(self.instagram_btn_2)

        self.email_btn_2 = QPushButton(self.frame_10)
        self.email_btn_2.setObjectName(u"email_btn_2")
        self.email_btn_2.setMinimumSize(QSize(40, 40))
        self.email_btn_2.setFont(font)
        icon12 = QIcon()
        icon12.addFile(u":/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.email_btn_2.setIcon(icon12)
        self.email_btn_2.setIconSize(QSize(32, 32))

        self.verticalLayout_12.addWidget(self.email_btn_2)


        self.gridLayout_12.addWidget(self.frame_10, 2, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.contact_info_frame_2)


        self.horizontalLayout_14.addWidget(self.right_frame_2)


        self.verticalLayout.addWidget(self.main_body_frame)

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
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.info_btn = QPushButton(self.footer_right_frame)
        self.info_btn.setObjectName(u"info_btn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon13)
        self.info_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.info_btn, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.main_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Smart wheelchair</span></p></body></html>", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Exit</span></p></body></html>", None))
        self.battery_page_btn_2.setText("")
        self.settings_page_btn_2.setText("")
        self.exit_page_btn_2.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Settings</span></p></body></html>", None))
        self.networks_page_btn_2.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Networks</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Battery</span></p></body></html>", None))
        self.system_page_btn_2.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Home</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Sensors</span></p></body></html>", None))
        self.home_page_btn_2.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">System</span></p></body></html>", None))
        self.sensors_page_btn_2.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">About</span></p></body></html>", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">App designed and</span></p><p><span style=\" color:#ffffff;\">Developed by </span></p><p><span style=\" color:#ffffff;\">Ximena Cely</span></p></body></html>", None))
        self.instagram_btn_2.setText("")
        self.email_btn_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Version 1.0 Copyright AXGC</span></p></body></html>", None))
        self.info_btn.setText("")
    # retranslateUi

