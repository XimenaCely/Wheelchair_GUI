"""
Copyright [2023] [Aura Ximena Gonzalez Cely]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import sys, traceback
from PySide2 import *
from PySide2 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5 import *
from qt_material import *
from PyQt5.QtCore import QPropertyAnimation, QPoint
import icon
import psutil
import PySide2extn
from PySide2 import QtCore
import qdarkstyle
import platform
import datetime
import shutil
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal
#Serial communication
import serial
import time
#UDP Communication
import socket 
import threading
#Another windows
from neck_control import neck_window
from head_control import head_window
from manual_control import *
from posture_monitoring import *


# Convert UI to PyQt5 py file
os.system("pyuic5 -o ui_Desktop_app.py Desktop_app.ui")

# Import the generated UI
from ui_Desktop_app import *


#Global Variables
progress_val = 0
velocity_wheelchair = 0
distance_wheelchair = 0
battery_wheelchair = 0
battery_PC = 0
blueflag=0
wififlag=0

#Variables for UDP communication
msgFromClient       = "0"		#Security command to the wheelchair
bytesToSend         = str.encode(msgFromClient)
serverAddressPortWheelchair   = ("192.168.137.20", 1234)
serverAddressPortNeck   = ("192.168.137.23", 1234)
serverAddressPortHead   = ("192.168.137.141", 2390)
bufferSize          = 1024

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
	
		#WiFi connection
		self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	
		self.UDPClientSocketneck = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	
		#Init application
		super().__init__()
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)		
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.shadow= QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.ui.centralwidget.setGraphicsEffect(self.shadow)
		self.setWindowTitle("Smart Wheelchair")
		self.setWindowIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\wheelchair.png"))#image_app
		QSizeGrip(self.ui.size_grip) #Change_size_window
		self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
		self.ui.minimize_window_button.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\minus.svg"))
		self.ui.close_window_button.clicked.connect(lambda: self.close())
		self.ui.close_window_button.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\close.svg"))
		self.ui.restore_window_button.clicked.connect(lambda:self.restore_or_maximize_window())
		self.ui.restore_window_button.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\maximize-2.svg"))
		#navigate into the scrolled menu
		self.ui.home_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
		self.ui.home_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\home.svg"))
		self.ui.system_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_page))
		self.ui.system_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\monitor.svg"))
		self.ui.battery_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery_page))
		self.ui.battery_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-battery-unknown-50"))
		self.ui.sensors_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensors_page))
		self.ui.sensors_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-proximity-sensor-30.png"))
		self.ui.networks_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.networks_page))
		self.ui.networks_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-signal-16.png"))
		self.ui.settings_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))
		self.ui.settings_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\settings.svg"))
		self.ui.exit_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.exit_page))
		self.ui.exit_page_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\log-out.svg"))		
		#movement
		def moveWindow(e):
			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos()+e.globalPos() - self.clickPosition)
					self.clickPosition= e.globalPos()
					e.accept()
		self.ui.header_frame.mouseMoveEvent=moveWindow			
		self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
		self.ui.info_btn.clicked.connect(lambda: self.slideRightMenu())
		self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\menu.svg"))		
		#Style clicked menu button 		
		for w in self.ui.menu_frame.findChildren(QPushButton):
			w.clicked.connect(self.applyButtonStyle)			
		#Menu options
		self.progressBarValueVelocimeter(velocity_wheelchair)
		self.progressBarValueDistance(distance_wheelchair)
		self.progressBarValueBatteryWheelchair(battery_wheelchair)
		#System info
		self.system_info()	
		#Threads functions
		self.psutil_thread()
		self.ui.close_window_button.clicked.connect(lambda: self.close_system())
		#Open windows controllers and posture monitoring
		self.ui.neck_ctrl_btn.clicked.connect(self.connect_neck_ctrl_win)
		self.ui.neck_ctrl_btn.clicked.connect(lambda: self.close())
		self.ui.head_ctrl_btn.clicked.connect(self.connect_head_ctrl_win)	
		self.ui.head_ctrl_btn.clicked.connect(lambda: self.close())
		self.ui.manual_ctrl_btn.clicked.connect(self.connect_manual_ctrl_win)
		self.ui.manual_ctrl_btn.clicked.connect(lambda: self.close())
		self.ui.posture_monitoring_btn.clicked.connect(self.connect_posture_monitor_win)
		self.ui.posture_monitoring_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\posture2.png"))	
		self.ui.posture_monitoring_btn.clicked.connect(lambda: self.close())
		self.ui.bluetooth_btn.clicked.connect(lambda: self.bluetooth_thread())
		self.ui.wifi_btn.clicked.connect(lambda: self.wifi_thread())				
		self.show()
	
	def psutil_thread(self):	
		t1 = threading.Thread(name="time_hour",target=self.time_hour, args=())
		t1.start()
		t2 = threading.Thread(name="Communication",target=self.communication, args=())
		t2.start()
		t3 = threading.Thread(name="battery",target=self.battery, args=())
		t3.start()
		
	def bluetooth_thread(self):	
		t4 = threading.Thread(name="bt_connection",target=self.bluetooth_connection, args=())
		t4.start()
				
	def wifi_thread(self):
		t5 = threading.Thread(name="wifi_reconnect",target=self.wifi_reconnect, args=())
		t5.start()
		
	def close_system(self):	
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()	
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()				
		sys.exit(0)
		event.accept()
		sys.exit(app.exec_())	
	
	def wifi_reconnect(self):
		self.wififlag=1
		self.communication()
			
	def bluetooth_connection(self):
		#Bluetooth connection
		global arduino
		arduino = serial.Serial(port='COM12', baudrate=115200, timeout=.1)	
		while True:
			serial_data = arduino.readline()
			print("Serial data: ",serial_data)
			#arduino.write(x)
			#time.sleep(0.05)
			
	def communication(self):	
		while True:	
			self.UDPClientSocket.sendto(bytesToSend, serverAddressPortWheelchair)
			msgFromServer = self.UDPClientSocket.recvfrom(bufferSize) 
			wheelchair_data=msgFromServer[0].decode("utf-8")			
			print("wheelchair: ",wheelchair_data)		
					
	def connect_posture_monitor_win(self):
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()	
		"""
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		"""
		self.posture_monitor=posture_window()
	
	def connect_manual_ctrl_win(self):
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()
		"""
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		"""
		self.manual_ctrl=manual_window()
	
	def connect_head_ctrl_win(self):
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()	
		"""
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		"""
		self.head_ctrl= head_window()
		
	def connect_neck_ctrl_win(self):
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()
		"""
		if(arduino.is_open == True):
			arduino.close()
		"""
		self.ui_neck= neck_window()
		
	def battery(self):
		while True:
			batt=psutil.sensors_battery()			
			if not hasattr(psutil,"sensors battery"):
				self.ui.battery_status.setText("Platform not supported")			
			if batt is None:
				self.ui.battery_status.setText("No battery installed")
			if batt.power_plugged:
				self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
				battery_PC=(int(round(batt.percent,2)))
				self.ui.battery_time_left.setText("N/A")
				if batt.percent < 100:
					self.ui.battery_status.setText("Charging")
				else:
					self.ui.battery_status.setText("Fully charged")
				self.ui.battery_plugged.setText("yes")
			else:
				self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
				battery_PC=(int(round(batt.percent,2)))
				self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
				if batt.percent < 100:
					self.ui.battery_status.setText("Discharging")
				else:
					self.ui.battery_status.setText("Fully Charged")
				self.ui.battery_plugged.setText("No")
			self.progressBarValueBatteryPC(int(round(batt.percent,2)))
			self.ui.battery_percentagePC.setText(str(round(batt.percent,2))+"%")	
			sleep(1)
			
	def time_hour(self):	
		while True:
			time=datetime.datetime.now().strftime("%I:%M:%S %p")
			self.ui.system_date.setText(str(time))
			date=datetime.datetime.now().strftime("%Y-%m-%d")
			self.ui.system_time.setText(str(date))
			sleep(1)
	
	def system_info(self):		
		self.ui.system_machine.setText(platform.machine())
		self.ui.system_version.setText(platform.version())
		self.ui.system_platform.setText(platform.platform())
		self.ui.system_system.setText(platform.system())
		self.ui.system_processor.setText(platform.processor())
	
	def progressBarValueVelocimeter(self,value):
		styleSheet= """
		QFrame{
			border-radius: 290 px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 128, 0), stop:{STOP_2} rgba(170, 170, 255, 255));

		}
		"""		
		progress= (100-value)/100
		stop_1= str(progress-0.001)
		stop_2= str(progress)
		
		newStylesheet= styleSheet.replace("{STOP_1}",stop_1).replace("{STOP_2}",stop_2)
		self.ui.circularProgress.setStyleSheet(newStylesheet)
			
	def progressBarValueDistance(self,value):
		styleSheet= """
		QFrame{
			border-radius: 290 px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_3} rgba(255, 0, 128, 0), stop:{STOP_4} rgba(170, 170, 255, 255));

		}
		"""
		progress= (100-value)/100
		stop_3= str(progress-0.001)
		stop_4= str(progress)
		
		newStylesheet= styleSheet.replace("{STOP_3}",stop_3).replace("{STOP_4}",stop_4)
		self.ui.circularProgress_2.setStyleSheet(newStylesheet)
		
	def progressBarValueBatteryWheelchair(self,value):
		styleSheet= """
		QFrame{
			border-radius: 70 px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_5} rgba(255, 0, 128, 0), stop:{STOP_6} rgba(170, 170, 255, 255));

		}
		"""
		progress= (100-value)/100
		stop_5= str(progress-0.001)
		stop_6= str(progress)
		
		newStylesheet= styleSheet.replace("{STOP_5}",stop_5).replace("{STOP_6}",stop_5)
		self.ui.circularProgress_3.setStyleSheet(newStylesheet)
	
	def progressBarValueBatteryPC(self,value):
		styleSheet= """
		QFrame{
			border-radius: 70 px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_7} rgba(255, 0, 128, 0), stop:{STOP_8} rgba(170, 170, 255, 255));

		}
		"""
		progress= (100-value)/100
		stop_7= str(progress-0.001)
		stop_8= str(progress)
		
		newStylesheet= styleSheet.replace("{STOP_7}",stop_7).replace("{STOP_8}",stop_8)
		self.ui.circularProgress_4.setStyleSheet(newStylesheet)
	
	def secs2hours(self,secs):
		mm,ss= divmod(secs,60)
		hh,mm= divmod(mm,60)
		return ("%d:%02d:%02d (H:M:S)" % (hh,mm,ss))
			
	def applyButtonStyle(self):
		for w in self.ui.menu_frame.findChildren(QPushButton):
			if w.objectName() != self.sender().objectName():
				w.setStyleSheet("border-bottom: none;")
		self.sender().setStyleSheet("border-bottom: 2px solid")
		return
		
	def slideRightMenu(self):
		width= self.ui.right_frame.width()
		if width==0:
			newWidth=150
		else:
			newWidth=0
		self.animation= QPropertyAnimation(self.ui.right_frame,b"minimumWidth")
		self.animation.setDuration(250)
		self.animation.setStartValue(width)
		self.animation.setEndValue(newWidth)
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
		self.animation.start()
	
	def slideLeftMenu(self):
		width= self.ui.left_menu_cont_frame.width()
		if width==42:
			newWidth=200
		else:
			newWidth=20
		self.animation= QPropertyAnimation(self.ui.left_menu_cont_frame,b"minimumWidth")
		self.animation.setDuration(250)
		self.animation.setStartValue(width)
		self.animation.setEndValue(newWidth)
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
		self.animation.start()
		
	def restore_or_maximize_window(self): #change icon maximize or minimize window
		if self.isMaximized():
			self.showNormal()
			self.ui.restore_window_button.setIcon(QtGui.QIcon(u"E:\CADEIRA DE RODAS\Desktop_app\icons\maximize-2.svg"))
		else:
			self.showMaximized()
			self.ui.restore_window_button.setIcon(QtGui.QIcon(u"E:\CADEIRA DE RODAS\Desktop_app\icons\minimize-2.svg"))
		
	def mousePressEvent(self,event):
		self.clickPosition= event.globalPos()
	"""
	def closeEvent(self, event):
		sys.exit(0)
		event.accept()
	"""

if __name__ == '__main__':
	try:		
		app=QtWidgets.QApplication(sys.argv)
		widget=QtWidgets.QMainWindow()		
		window = MainWindow()
	except KeyboardInterrupt:
		pass
	finally:
		sys.exit(app.exec_())
