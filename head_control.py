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
import logging
import threading
import json
#Serial communication
import serial
import time
#UDP Communication
import socket 
import threading
from multiprocessing import Process, Queue
#Fuzzy logic controller
import numpy as np
#import skfuzzy as fuzz
#from skfuzzy import control as ctrl
#Filtering stages
from scipy.signal import butter, lfilter, freqz
from scipy import signal
import scipy.signal
import pandas as pd
#Fuzzy logic controller
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

from ui_head_control_ui import  Ui_head_window

#Variables for UDP communication
msgFromClient       = "Welcome Smart wheelchair communication system"
bytesToSend         = str.encode(msgFromClient)
serverAddressPortWheelchair   = ("192.168.137.23", 1234)
serverAddressPortNeck   = ("192.168.137.20", 1234)
serverAddressPortHead   = ("192.168.137.141", 2390)
bufferSize          = 1024
#Variables
activeWidget=1
global arduino
maxsamples = 21
# Configuration Butterworth low pass filter
fs = 1000  # Sampling frequency
fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
order = 5
#Update lists
PD1n=[]
PD2n=[]
PD1w=[]
PD2w=[]
PD3w=[]
PD4w=[]
PD5w=[]
PD6w=[]
PD7w=[]
PD8w=[]
PD9w=[]
PD10w=[]
PD11w=[]
PD12w=[]
PD13w=[]
PD14w=[]
PD15w=[]
PD16w=[]
PD17w=[]
PD18w=[]
PD19w=[]
PD20w=[]
PD21w=[]
PD22w=[]
PD23w=[]
PD24w=[]
meanPDs=[]
datasetPDs=[]
meanCAR=[]
meanbutter=[]
df_butter = pd.DataFrame()

class head_window(QtWidgets.QMainWindow):
	def __init__(self):
		#Wheelchair connection
		global arduino
		global heads
		#arduino = serial.Serial(port='COM10', baudrate=115200, timeout=.1)	
		heads = serial.Serial(port='COM9', baudrate=115200, timeout=.1)	
		#WiFi connection
		self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)			
		#self.UDPClientSockethead = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)			
		#Application init
		super(head_window,self).__init__()
		QMainWindow.__init__(self)			
		uic.loadUi("head_control_ui.ui",self)
		#Json Style
		f= open('style.json','r')
		json_style= json.load(f)
		#Style configuration
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.shadow= QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.centralwidget.setGraphicsEffect(self.shadow)
		self.setWindowTitle("Wheelchair neck control")#title_app
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
		self.return_btn.clicked.connect(lambda: self.close())
		self.info_btn.clicked.connect(lambda: self.slideRightMenu())
		#Style clicked menu button 		
		for w in self.main_frame.findChildren(QPushButton):
			w.clicked.connect(self.applyButtonStyle)
		#Turn on system
		self.start_wizard_btn.clicked.connect(lambda: self.psutil_thread())
		self.start_wizard_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\power-on.png"))
		self.stop_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-stop-sign-96.png"))
		#self.pixmap = QPixmap(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\neck_pillow.png")
		#self.neck_pillow_guide.setPixmap(self.pixmap)
		
				
		self.show()
			
	def startWizard(self):
		global activeWidget
		self.pages.expandMenu()
		self.welcome.collapseMenu()		
		#currentPerc= (activeWidget/2)*100
		
	def stopWizard(self):
		self.pages.collapseMenu()
		self.welcome.expandMenu()
	
		
	def come_back_mainmenu(self):
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()	
		#self.UDPClientSockethead.shutdown(socket.SHUT_RDWR)
		#self.UDPClientSockethead.close()
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		from main import MainWindow
		window=MainWindow()		
			
	#Thread functions
	def psutil_thread(self):
		t1 = threading.Thread(name="fuzzy",target=self.fuzzy, args=())		#Send info to the fuzzy controller	with wifi comm
		t1.start()
		#t1 = threading.Thread(name="wifi_communication",target=self.wifi_communication, args=())
		#t1.start()
		#t2 = threading.Thread(name="blue_communication",target=self.blue_communication, args=())
		#t2.start()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Fuzzy logic control
	def fuzzy(self):
		#Lists
		hd=[]
		hd1=[]
		cp=[]
		cp1=[]
		data_send=[]
		# functions
		headtailf = ctrl.Antecedent(np.linspace(-100, 70, 100), 'headtail')
		fluttf = ctrl.Antecedent(np.linspace(-60, 100, 100), 'flutt')
		dir = ctrl.Consequent(np.linspace(0, 5.01, 100), 'dir')#Fuzzify and defuzz inputs and output

		# Membership functions pitch
		headtailf['forw'] = fuzz.trimf(headtailf.universe, [-40, 0, 20])      #Se colocan decimales para evitar el error en los rangos y que no tome ese valor
		headtailf['left'] = fuzz.trimf(headtailf.universe, [28, 45, 70])
		headtailf['right'] = fuzz.trimf(headtailf.universe, [-30,-10,10])#-20,-10,0
		headtailf['stop'] = fuzz.trimf(headtailf.universe, [5, 17 , 30])
		headtailf['back'] = fuzz.trimf(headtailf.universe, [9, 16,17])
		headtailf['stop2'] = fuzz.trimf(headtailf.universe, [-100, -55, -40])
		#headtailf['back_left'] = fuzz.trimf(headtailf.universe, [-20, -10 , -5])

		# Membership functions flutt
		fluttf['rightf'] = fuzz.trimf(fluttf.universe, [20, 26, 40])
		fluttf['forwf'] = fuzz.trimf(fluttf.universe, [40, 50, 70])
		fluttf['leftf'] = fuzz.trimf(fluttf.universe, [18, 31,40])
		fluttf['stopf'] = fuzz.trimf(fluttf.universe, [5, 22 , 40])
		fluttf['stop2f'] = fuzz.trimf(fluttf.universe, [70, 85 , 100])
		fluttf['backf'] = fuzz.trimf(fluttf.universe, [-13,0,14])
		#fluttf['backf_leftf'] = fuzz.trimf(fluttf.universe, [43,55,60])
		#fluttf['backf_rightf'] = fuzz.trimf(fluttf.universe, [-13,0.01,20.01])
		########## OUTPUT1 ########################
		# Discurse-universe
		#Discurse universe for direction
		dir['forwd'] = fuzz.trimf(dir.universe,[0.9, 1, 1.1])
		dir['rightd'] = fuzz.trimf(dir.universe,[1.9, 2, 2.1])
		dir['leftd'] = fuzz.trimf(dir.universe,[2.9, 3, 3.1])
		dir['stopd'] = fuzz.trimf(dir.universe,[-0.1, 0, 0.1])
		dir['backd'] = fuzz.trimf(dir.universe,[3.9, 4, 4.1])

		#Linguistic rules
		rule1 = ctrl.Rule(headtailf['forw'] & fluttf['forwf'], dir['forwd'])
		rule2 = ctrl.Rule(headtailf['right'] & fluttf['rightf'], dir['rightd'])
		rule3 = ctrl.Rule(headtailf['left'] & fluttf['leftf'], dir['leftd'])
		rule4 = ctrl.Rule(headtailf['back'] & fluttf['backf'], dir['backd'])
		rule5 = ctrl.Rule(headtailf['stop'] & fluttf['stopf'], dir['stopd'])
		rule6 = ctrl.Rule(headtailf['stop2'] & fluttf['stop2f'], dir['stopd'])
		#rule7 = ctrl.Rule(headtailf['back_left'] & fluttf['backf_leftf'], dir['backd_leftd'])
		#rule8 = ctrl.Rule(headtailf['back_right'] & fluttf['backf_rightf'], dir['backd_rightd'])

		tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6])
		tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
		#Send fuzzy output
		t2 = threading.Thread(name="start_comm",target=self.start_comm, args=(tipping,))		
		t2.start()
		
	def sending_data_wheelchair(self,datahead,tipping):
		datawheel=Queue()
		while datahead.empty() is False:
			initialize_time=time.time()
			dataheadthread= datahead.get()
			pitch=dataheadthread[0]
			roll=dataheadthread[1]
			print(pitch,roll)			
			tipping.input['headtail'] = pitch
			tipping.input['flutt'] = roll
			try:
				tipping.compute()
				msg_wheelchair=int(round(tipping.output['dir']))
				msg_wheelchair=str(msg_wheelchair)
				print("msg_wheelchair: ",msg_wheelchair)
				#self.send_comm(msg_wheelchair)
				final_time=time.time()
				execution_time=final_time-initialize_time
				print("Response time: ",execution_time)
			except:
				pass
			
				
	def send_comm(self,comm):
		arduino.write(str.encode(comm))
		
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Process wifi data and filtering
		
	def start_comm(self,tipping): 
		datahead= Queue()
		while True:			
			#clean wheelchair data
			
			headdata = heads.readline()
			headdata =headdata.decode("utf-8")	
			headdata=headdata.rstrip()
			headdata = headdata.strip('\n')
			headdata = headdata.split(" ")
			#print(headdata,type(headdata),len(headdata))
			if (len(headdata)==6):
				newLista=filter(lambda x:not x in ("",None),headdata)	#clean None values			
				headdata_filtered = [float(item) for item in newLista]	
				head_info=[headdata_filtered[3],headdata_filtered[4]]
				datahead.put(head_info)
				print(head_info)
				t6 = threading.Thread(name="sending_data_wheelchair",target=self.sending_data_wheelchair, args=(datahead,tipping,))		#Send info to the fuzzy controller
				t6.start()
			else:
				pass
	
	def listeachPD(self,list1):  
		pitch.append(list1[1][0])  
		yaw.append(list1[1][1])  
		roll.append(list1[1][2])		
		PD1w.append(list1[0][0])  
		PD2w.append(list1[0][1])  
		PD3w.append(list1[0][2])  
		PD4w.append(list1[0][3])  
		PD5w.append(list1[0][4])  
		PD6w.append(list1[0][5])  
		PD7w.append(list1[0][6])  
		PD8w.append(list1[0][7])  
		PD9w.append(list1[0][8])  
		PD10w.append(list1[0][9])  
		PD11w.append(list1[0][10])  
		PD12w.append(list1[0][11])  
		PD13w.append(list1[0][12])  
		PD14w.append(list1[0][13])  
		PD15w.append(list1[0][14])  
		PD16w.append(list1[0][15])  
		PD17w.append(list1[0][16])  
		PD18w.append(list1[0][17])  
		PD19w.append(list1[0][18])  
		PD20w.append(list1[0][19])  
		PD21w.append(list1[0][20])  
		PD22w.append(list1[0][21])  
		PD23w.append(list1[0][22])  
		PD24w.append(list1[0][23])
		return PD1w,PD2w,PD3w,PD4w,PD5w,PD6w,PD7w,PD8w,PD9w,PD10w,PD11w,PD12w,PD13w,PD14w,PD15w,PD16w,PD17w,PD18w,PD19w,PD20w,PD21w,PD22w,PD23w,PD24w,pitch, yaw, roll
	
	def butter_lowpass_filter(self,order,data, w):
		b, a = signal.butter(order, w, 'low')
		output_but = signal.filtfilt(b, a, data)
		return output_but
	
	def CAR_filter(self,dataframe_each_posture):
		wheelchair_filtered2 = []
		wheelchair_filtered2list=[]
		tot=[]
		list_help=[]
		for i in range (dataframe_each_posture.shape[0]): #mean each row of the dataframe
			wheelchair_filtered2.append(dataframe_each_posture.iloc[i].mean()) 
		for i in range (dataframe_each_posture.shape[0]):   #Loop through N columns of the dataframe
			for j in dataframe_each_posture.iloc[i]:          #Loop throug M rows of the dataframe
				list_help.append(j-wheelchair_filtered2[i])
			tot.append(list_help) 
			list_help=[]
		posture_dffilt = pd.DataFrame(tot)  #Dataframe filtered
		return posture_dffilt
		
	def processCARfilter(self,dataframe):
		dfCAR=self.CAR_filter(dataframe)	
		for i in range (dfCAR.shape[1]):
			meanCAR.append(np.mean(dfCAR[i]))
			meanbutter.append(np.mean(dataframe[i]))
		return meanCAR,meanbutter
	
	def clearfilters(self,meandata):
		for i in range (len(meandata)):
			meandata[i].clear()
		
	def filter_wifi_data(self,dataIMUhead):	#Mean filter complete WiFi data: wheelchair-neck
		dataneck= Queue()
		print("First data: ",dataIMUhead)
		PDslists=self.listeachPD(dataIMUhead)		
		for i in PDslists:
			if len(i) == maxsamples:
				i.pop(0)#Update the last values
				#print("Values: ",i)
				dataPDs_butter = self.butter_lowpass_filter(order,i, w)
				#print("Filtered value: ",dataPDs_butter)				
				datasetPDs.append(dataPDs_butter)	
				if (len(datasetPDs)==27):	#convert to columns
					wheelchairPDsarray = np.stack((datasetPDs[0], datasetPDs[1],datasetPDs[2],datasetPDs[3],datasetPDs[4],datasetPDs[5],datasetPDs[6],datasetPDs[7],datasetPDs[8],datasetPDs[9],datasetPDs[10],datasetPDs[11],datasetPDs[12],datasetPDs[13],datasetPDs[14],datasetPDs[15],datasetPDs[16],datasetPDs[17],datasetPDs[18],datasetPDs[19],datasetPDs[20],datasetPDs[21],datasetPDs[22],datasetPDs[23]), axis=1)
					dfwheelchair = pd.DataFrame(wheelchairPDsarray)
					meanswheelchair=self.processCARfilter(dfwheelchair)
					print("means wheelchair: ",meanswheelchair)						
					self.clearfilters(meanswheelchair)
					headPDsarray = np.stack((datasetPDs[24], datasetPDs[25], datasetPDs[26]), axis=1)
					dfhead = pd.DataFrame(headPDsarray)	#Only Butterworth filter
					means=self.processCARfilter(dfhead)
					print("means head: ",meanshead)
					datahead.put(meanshead)
					t5 = threading.Thread(name="head_fuzzy_control",target=self.head_fuzzy_control(datahead), args=())		#Send info to the fuzzy controller
					t5.start()					
					self.clearfilters(meanshead)					
					datasetPDs.clear()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Process bluetooth data and filtering				

	def blue_communication(self):
		datablue=[]
		while True:
			serial_data = arduino.readline()
			serial_data=serial_data.decode("utf-8") 				
			if len(serial_data) > 1:
				serial_data=serial_data.rstrip()
				serial_data = serial_data.split(",")
				if len(serial_data) == 24:
					val= '' in serial_data
					if val == False:
						wheelchair_list = [int(item) for item in serial_data]
					datablue.append(wheelchair_list)
						#print("wheelchair_list: ",wheelchair_list)
						#datawheelblue.put(wheelchair_list)
				if len(serial_data) == 2:
					val= '' in serial_data
					if val == False:
						neck_list = [int(item) for item in serial_data]
					datablue.append(neck_list)
			#t3 = threading.Thread(name="switch_info",target=self.switch_info(datablue), args=())
			#t3.start()
			#arduino.write(x)
			#time.sleep(0.05)
			
	def switch_info(self,data):
		dataneckblue=Queue()
		datawheelblue=Queue()
		dataneckwifi=Queue()
		datawheelwifi=Queue()
		if type(data) is list:
			print("wifi data: ",data)			
			dataneckwifi.put(data[0])
			datawheelwifi.put(data[1])							
		else:
			print("blue data",data)
			"""
			data=data.decode("utf-8") 				
			if len(data) > 1:
				data=data.rstrip()
				data = data.split(",")
				if len(data) == 24:
					val= '' in data
					if val == False:
						wheelchair_list = [int(item) for item in data]
						#print("wheelchair_list: ",wheelchair_list)
						datawheelblue.put(wheelchair_list)
				if len(data) == 2:
					val= '' in data
					if val == False:
						neck_list = [int(item) for item in data]
						#print('neck_list: ',neck_list)
						dataneckblue.put(neck_list)
			"""
						#t6 = threading.Thread(name="design_fuzzy_control",target=self.neck_fuzzy_control(), args=(datawheelblue,dataneckblue,))
						#t6.start()
	
	def slideRightMenu(self):
		width= self.right_frame.width()
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
		
	def applyButtonStyle(self):
		for w in self.main_frame.findChildren(QPushButton):
			if w.objectName() != self.sender().objectName():
				w.setStyleSheet("border-bottom: none;")
		self.sender().setStyleSheet("border-bottom: 2px solid")
		return
	
	def mousePressEvent(self,event):
		self.clickPosition= event.globalPos()
