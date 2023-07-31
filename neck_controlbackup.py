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
#Classification model libraries
from joblib import Parallel, delayed
import joblib
from sklearn.preprocessing import MinMaxScaler
from statistics import mode

from ui_neck_control_ui import  Ui_neck_window
#Variables for UDP communication
msgFromClient       = "0"
bytesToSend         = str.encode(msgFromClient)
serverAddressPortWheelchair   = ("192.168.137.20", 1234)
serverAddressPortNeck   = ("192.168.137.23", 1234)
serverAddressPortHead   = ("192.168.137.141", 2390)
bufferSize          = 1024
#Variables
activeWidget=1
global arduino
maxsamples = 201
features_quantity = 5
overlap= 10
# Configuration Butterworth low pass filter
fs = 1000  # Sampling frequency
fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
order = 5
#Update lists
PD1n=[]
PD2n=[]
meanPDs=[]
datasetPDs=[]
meanCAR=[]
meanbutter=[]
meandata=[]
meanPDs=[]
df_butter = pd.DataFrame()
features_PDs=[]

class neck_window(QtWidgets.QMainWindow):
	def __init__(self):
		"""
		#Bluetooth connection
		global arduino
		arduino = serial.Serial(port='COM12', baudrate=115200, timeout=.1)	
		"""		
		self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)		#WiFi connection	
		self.UDPClientSocketneck = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)				
		super(neck_window,self).__init__()	#Application init
		QMainWindow.__init__(self)			
		uic.loadUi("neck_control_ui.ui",self)		
		f= open('style.json','r')		#Json Style
		json_style= json.load(f)		
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())	#Style configuration
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.shadow= QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.centralwidget.setGraphicsEffect(self.shadow)
		self.setWindowTitle("Wheelchair neck control")			#title_app
		self.centralwidget.setGraphicsEffect(self.shadow)
		#self.setWindowIcon(QtGui.QIcon("C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\wheelchair.png"))#image_app
		QSizeGrip(self.size_grip_2) #Change_size_window				
		def moveWindow(e):			#movement
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
		for w in self.main_frame.findChildren(QPushButton):		#Style clicked menu button 		
			w.clicked.connect(self.applyButtonStyle)		
		self.start_wizard_btn.clicked.connect(lambda: self.psutil_thread())		#Turn on communication system
		#self.start_wizard_btn.setIcon(QtGui.QIcon(u"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\power-on.png"))
		#self.stop_btn.setIcon(QtGui.QIcon(u"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-stop-sign-96.png"))
		#self.pixmap = QPixmap("C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\neck_pillow.png")
		#self.neck_pillow_guide.setPixmap(self.pixmap)				
		self.show()
			
	def startWizard(self):
		global activeWidget
		self.pages.expandMenu()
		self.welcome.collapseMenu()		
		
	def stopWizard(self):
		self.pages.collapseMenu()
		self.welcome.expandMenu()
	
		
	def come_back_mainmenu(self):
		self.UDPClientSocket.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocket.close()	
		self.UDPClientSocketneck.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocketneck.close()
		"""
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		"""
		from main import MainWindow
		window=MainWindow()		
			
	#Thread functions
	def psutil_thread(self):
		t1 = threading.Thread(name="wifi_communication",target=self.wifi_communication, args=())
		t1.start()
		#t2 = threading.Thread(name="blue_communication",target=self.blue_communication, args=())
		#t2.start()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Seinding wheelchair commands
		
	def sending_data_wheelchair(self,dataneck,tipping):
		if len(dataneck) == 2:			#PD1 and PD2 values
			print("PD1: ",dataneck[0])
			print("PD2: ",dataneck[1])
			PD1val=dataneck[0]
			PD2val=dataneck[1]
			tipping.input['PD1'] = PD1val
			tipping.input['PD2'] = PD2val
			try:
				tipping.compute()
				print("Pass")
				msg_wheelchair=int(round(tipping.output['direction']))
				msg_wheelchair=str(msg_wheelchair)
				print("msg_wheelchair: ",msg_wheelchair)
				datawheel.put(msg_wheelchair)
				self.send_comm(msg_wheelchair)
			except:
				pass
				
	def send_comm(self,comm):
		t1 = threading.Thread(name="talkWheelchair",target=self.talkToClient, args=(serverAddressPortWheelchair,comm,))
		t1.start()

	def talkToClient(self,ip,msg):
		bytesToSend = str.encode(msg)
		self.sockrobo.sendto(bytesToSend, ip)
		print("msg: ",msg)
		time.sleep(0.1)
		logging.info(bytesToSend)	
		
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Process wifi data and filtering process
			
	def wifi_communication(self): 
		datawifiwheelchair=[]
		datawifineck=[]
		while True:			
			#clean neck data
			self.UDPClientSocketneck.sendto(bytesToSend, serverAddressPortNeck)
			msgFromServerneck = self.UDPClientSocketneck.recvfrom(bufferSize) 
			neck_data=msgFromServerneck[0].decode("utf-8")			
			neck_data=neck_data.rstrip()
			neck_data = neck_data.strip('\n')
			neck_data = neck_data.split(",")
			newLista=filter(lambda x:not x in ("",None),neck_data)	#clean None values
			neck_wifi_data = [int(item) for item in newLista]
			if len(neck_wifi_data)==2:
				t4 = threading.Thread(name="filter_wifi_neck_data",target=self.filter_wifi_neck_data(neck_wifi_data), args=())
				t4.start()	
	
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
		print("CAR: ",meanCAR,meanbutter)
		return meanCAR,meanbutter
		meanCAR.clear()
		meanbutter.clear()
	"""
	def windows_generation_overlap(dataframe_filtered):
		W=[]
		featuresbywindow=[]
		featuresbyPDlist=[]
		windows_quantity=int(((dataframe_filtered.shape[0]-samples)/overlap)-1)#-1?
		var=0
		W=[dataframe_filtered.iloc[var:samples-1]]  
		#print("Firsst: ",var,samples-1)
		#print("Shape dataframe: ",dataframe_filtered.shape)
		for i in range(windows_quantity):
		  var += overlap
		  #print(var,(var+samples)-1)
		  W.append(dataframe_filtered.iloc[var:(var+samples)-1])
		#print(len(W))
		for i in range(len(W)): #Window 0 to N window 
		dffeatures=pd.DataFrame(W[i])
		meanlabel = round(np.mean(dffeatures['label']))
		#print("meanlabel: ",meanlabel)
		del(dffeatures['label'])
		#print(dffeatures)
		for photodetectors in dffeatures:
		  dataPD=dffeatures[photodetectors]      
		  featuresbyPD=features(dataPD,meanlabel) #Get the features of each PD dataset by each window time
		  #print(featuresbyPD)
		  featuresbyPDlist.append(featuresbyPD)
		  #print(featuresbyPDlist,len(featuresbyPDlist))
		  if len(featuresbyPDlist) == 2:
			featuresbywindow.append(featuresbyPDlist)
			featuresbyPDlist=[]      
		  
		featuresbywindowdf=pd.DataFrame (featuresbywindow)
		return featuresbywindowdf
	"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Real-time classifier implementation	
	
	def features(self,datasetPDs,wifidata):		#variance and rms in time and frequency domain for each PD
				
		varPD1= np.var(np.array(datasetPDs[0]))
		varPD2= np.var(np.array(datasetPDs[1]))
		rmsPD1= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[0]),2))))
		rmsPD2= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[1]),2))))
		varfreqPD1= np.var(np.fft.fft(np.array(datasetPDs[0])))
		varfreqPD2= np.var(np.fft.fft(np.array(datasetPDs[1])))
		rmsfreqPD1= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[0])),2)))))
		rmsfreqPD2= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[1])),2)))))
		features_PDs.append([varPD1,rmsPD1,varfreqPD1,rmsfreqPD1,varPD2,rmsPD2,varfreqPD2,rmsfreqPD2])	#All features
		if (len(features_PDs)==features_quantity):	#features rows
			scaler = MinMaxScaler()
			features_PDs_array=np.array([features_PDs])
			data_model = scaler.fit_transform(features_PDs)			#Data normalization		
			knn_from_joblib = joblib.load('modelv2.pkl')		#Load classification model
			output_list=knn_from_joblib.predict(data_model)
			print(output_list,mode(output_list))	#Mode number to choose command
			features_PDs.clear()
			
	def filter_wifi_neck_data(self,wifidata):	#Mean filter complete WiFi data: wheelchair-neck		
		PD1n.append(wifidata[0])  
		PD2n.append(wifidata[1]) 
		PDslists=PD1n,PD2n
		for i in PDslists:
			if len(i) == maxsamples:
				i.pop(0)#Update the last values
				
				datasetPDs.append(i)
		#print(datasetPDs)
		if (len(datasetPDs)==2):	
			del datasetPDs[0][0:overlap]
			del datasetPDs[1][0:overlap]
			t5 = threading.Thread(name="features",target=self.features(datasetPDs,wifidata), args=())		#Send info to the fuzzy controller
			t5.start()	
		
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
	
	def send_info_wheelchair(self,datawheelblue,dataneckblue,tipping):
		while datawheelblue.empty() is False:
			data_threadblue= datawheelblue.get()
			print("Data_neck_thread: ",data_threadblue)
			
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
