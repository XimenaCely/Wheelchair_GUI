"""
Copyright [2023] [Aura Ximena Gonzalez Cely]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
import os
import sys, traceback
from PySide2 import *
from PySide2 import QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5 import *
from qt_material import *
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve
import icons
import psutil
import PySide2extn
from PySide2 import QtCore
import qdarkstyle
import platform
import datetime
import shutil
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, QSize, Qt
from queue import Queue
#UDP Communication
import socket 
import threading
from multiprocessing import Process, Queue
import serial
import time

from ui_manual_control_ui import  Ui_manual_window

#Variables
activeWidget=1
#Variables for UDP communication
#Variables for UDP communication
msgFromClient       = "0"		#Security command to the wheelchair
bytesToSend         = str.encode(msgFromClient)
serverAddressPortWheelchair   = ("192.168.137.20", 1234)
serverAddressPortNeck   = ("192.168.137.23", 1234)
serverAddressPortHead   = ("192.168.137.141", 2390)
bufferSize          = 1024

class manual_window(QtWidgets.QMainWindow):
	def __init__(self):
		
		#Wheelchair commands
		global arduino
		arduino = serial.Serial(port='COM10', baudrate=115200, timeout=.1)	
		
		#WiFi connection
		self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)			
		#Application init
		super(manual_window,self).__init__()
		QMainWindow.__init__(self)			
		uic.loadUi("manual_control_ui.ui",self)
		#Json Style
		#f= open('style.json','r')
		#json_style= json.load(f)
		#Style configuration
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.shadow= QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.centralwidget.setGraphicsEffect(self.shadow)
		self.setWindowTitle("Wheelchair manual control")#title_app
		self.centralwidget.setGraphicsEffect(self.shadow)
		self.setWindowIcon(QtGui.QIcon("E:\CADEIRA DE RODAS\Desktop_app\icons\wheelchair.png"))#image_app
		QSizeGrip(self.size_grip_2) #Change_size_window		
		#movement
		def moveWindow(e):
			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos()+e.globalPos() - self.clickPosition)
					self.clickPosition= e.globalPos()
					e.accept()
		self.header_frame.mouseMoveEvent=moveWindow				
		self.return_btn.clicked.connect(lambda: self.come_back_mainmenu())
		self.start_wizard_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
		self.nxt.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
		self.prev.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
		#self.validateWizard()
		
		self.return_btn.clicked.connect(lambda: self.close())
		#Style clicked menu button 		
		for w in self.main_frame.findChildren(QPushButton):
			w.clicked.connect(self.applyButtonStyle)
		#Turn on system
		self.start_wizard_btn.clicked.connect(lambda: self.psutil_thread())
		self.start_wizard_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\power-on.png"))
		self.stop_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-stop-sign-96.png"))
		self.up_btn.clicked.connect(self.up_control)
		self.right_btn.clicked.connect(self.right_control)
		self.diag_upr_btn.clicked.connect(self.diag_upr_control)
		self.diag_upl_btn.clicked.connect(self.diag_upl_control)
		self.left_btn.clicked.connect(self.left_control)
		self.diag_downr_btn.clicked.connect(self.diagdownr_control)
		self.diag_downl_btn.clicked.connect(self.diagdownl_control)
		self.down_btn.clicked.connect(self.down_control)
		self.stop_btn.clicked.connect(self.stop_control)
		#Manual button images
		self.diag_downl_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\diagonal-arrw_right2.png"))
		self.diag_downr_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\diagonal-arrow_left1.png"))
		self.diag_upl_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\diagonal-arrow_right1.png"))
		self.diag_upr_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\diagonal-arrow.png"))
		self.down_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\down.png"))
		self.left_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\left.png"))
		self.right_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\right.png"))
		self.up_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\upbtn.png"))
		
		
		#self.psutil_thread()		
		self.show()
	
	def up_control(self):
		print("Action control: up")
		print("up","1")
		self.send_comm("1")
	
	def right_control(self):
		print("Action control: right")
		print("right","2")
		self.send_comm("2")
	
	def diag_upr_control(self):
		print("Action control: up diag right")
		print("up diag right","5")
		self.send_comm("5")
		
	def diag_upl_control(self):
		print("Action control: up diag left")
		print("up diag left","6")
		self.send_comm("6")
	
	def left_control(self):
		print("Action control: left")
		print("left","3")
		self.send_comm("3")
		
	def diagdownr_control(self):
		print("Action control: diagdownr_control")
		print("diagdownr_control","7")
		self.send_comm("7")
		
	def diagdownl_control(self):
		print("Action control: diagdownl_control")
		print("diagdownl_control","8")
		self.send_comm("8")
		
	def down_control(self):
		print("Action control: back")
		print("back","4")
		self.send_comm("4")
		
	def stop_control(self):
		print("stop","0")
		self.send_comm("0")
	
	def send_comm(self,comm):
		print("Send data wheelchair")
		arduino.write(str.encode(comm))
		time.sleep(1)
		print("Sent")
		#t1 = threading.Thread(name="talkWheelchair",target=self.talkToClient, args=(comm,))
		#t1.start()
	
	def talkToClient(self,msg):
		bytesToSend = str.encode(msg)
		self.UDPClientSocket.sendto(bytesToSend, serverAddressPortWheelchair)
		print("msg: ",msg)
		time.sleep(0.1)
			
	def startWizard(self):
		global activeWidget
		self.pages.expandMenu()
		self.welcome.collapseMenu()		
		#currentPerc= (activeWidget/2)*100
		
	def stopWizard(self):
		self.pages.collapseMenu()
		self.welcome.expandMenu()
			
	def come_back_mainmenu(self):
		#self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()
		arduino.close()			
		"""
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		"""
		from main import MainWindow
		window=MainWindow()		
			
	#Thread functions
	def psutil_thread(self):
		print("Test")
		#t1 = threading.Thread(name="wifi_communication",target=self.wifi_communication, args=())
		#t1.start()
		#t2 = threading.Thread(name="blue_communication",target=self.blue_communication, args=())
		#t2.start()
		
	def wifi_communication(self): 
		while True:	
			self.UDPClientSocket.sendto(bytesToSend, serverAddressPortWheelchair)
			msgFromServer = self.UDPClientSocket.recvfrom(bufferSize) 
			wheelchair_data=msgFromServer[0].decode("utf-8")
			print("wheelchair: ",wheelchair_data)
	
	def blue_communication(self):
		while True:
			serial_data = arduino.readline()
			#print("Serial data: ",serial_data)
			#arduino.write(x)
			#time.sleep(0.05)
			
	def applyButtonStyle(self):
		for w in self.main_frame.findChildren(QPushButton):
			if w.objectName() != self.sender().objectName():
				w.setStyleSheet("border-bottom: none;")
		self.sender().setStyleSheet("border-bottom: 2px solid")
		return
	
	def mousePressEvent(self,event):
		self.clickPosition= event.globalPos()
