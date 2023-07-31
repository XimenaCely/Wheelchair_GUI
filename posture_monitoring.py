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
import skfuzzy as fuzz
from skfuzzy import control as ctrl
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
#Storage data
from serialtoexcel import SerialToExcel
import time

from ui_posture_monitoring_ui import  Ui_posture_window
#Variables for UDP communication
msgFromClient       = "0"		#Security command to the wheelchair
bytesToSend         = str.encode(msgFromClient)
serverAddressPortWheelchair   = ("192.168.137.20", 1234)
serverAddressPortNeck   = ("192.168.137.23", 1234)
serverAddressPortHead   = ("192.168.137.141", 2390)
bufferSize          = 1024

#Variables
quantityPhotodetectors=23;
activeWidget=1
global arduino
maxsamples = 21
# Configuration Butterworth low pass filter
fs = 1000  # Sampling frequency
fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
order = 5
#Classifier variables
maxsamples = 201
features_quantity = 92
overlap= 10
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
features_PDs=[]
meanCAR=[]
meanbutter=[]
df_butter = pd.DataFrame()

class posture_window(QtWidgets.QMainWindow):
	def __init__(self):
		"""
		#Bluetooth connection
		global arduino
		arduino = serial.Serial(port='COM12', baudrate=115200, timeout=.1)
		"""		
		#WiFi connection
		self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	
		#Application init
		super(posture_window,self).__init__()
		QMainWindow.__init__(self)			
		uic.loadUi("posture_monitoring_ui.ui",self)
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
		self.setWindowTitle("Wheelchair posture monitoring")#title_app
		self.centralwidget.setGraphicsEffect(self.shadow)
		#self.setWindowIcon(QtGui.QIcon("C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\wheelchair.png"))#image_app
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
		#self.validateWizard()
		
		self.return_btn.clicked.connect(lambda: self.close())
		self.info_btn.clicked.connect(lambda: self.slideRightMenu())
		#Style clicked menu button 		
		for w in self.main_frame.findChildren(QPushButton):
			w.clicked.connect(self.applyButtonStyle)
		#Turn on system
		self.start_wizard_btn.clicked.connect(lambda: self.psutil_thread())
		self.start_wizard_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\power-on.png"))				
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
#Posture monitoring processing 
	def posture_processing(self,datawheelchair):
		print("Posture_data: ",datawheechair)
	
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Process wifi data and filtering
		
	def wifi_communication(self): 	
		datawheelchair= Queue()
		self.UDPClientSocket.sendto(bytesToSend, serverAddressPortWheelchair)
		knn_from_joblib = joblib.load('kNN.pkl')		#Load classification model
		while True:			
			#clean neck data			
			msgFromServerWheelchair = self.UDPClientSocket.recvfrom(bufferSize) 
			try:
				wheelchair_data=msgFromServerWheelchair[0].decode("utf-8")			
				wheelchair_data=wheelchair_data.rstrip()
				wheelchair_data = wheelchair_data.strip('\n')
				wheelchair_data = wheelchair_data.split(",")
				newLista=filter(lambda x:not x in ("",None),wheelchair_data)	#clean None values			
				wifi_wheelchair_data = [int(item) for item in newLista]				
				datawheelchair.put(wifi_wheelchair_data)
				#print("Raw data first: ",wifi_wheelchair_data)			
				t6 = threading.Thread(name="windows_generation_overlap",target=self.windows_generation_overlap, args=(datawheelchair,knn_from_joblib,))		#Send info to the fuzzy controller
				t6.start()
			except ValueError:
				continue
	
	def windows_generation_overlap(self,datawheelchair,knn_from_joblib):
		while datawheelchair.empty() is False:
			wheelchair_wifi_data= datawheelchair.get()
			#print(wheelchair_wifi_data)
			#print(len(wheelchair_wifi_data))
			if (len(wheelchair_wifi_data)==23):			
				PD1w.append(wheelchair_wifi_data[0])  	#PDseat11
				PD2w.append(wheelchair_wifi_data[1])	#PDseat12
				PD3w.append(wheelchair_wifi_data[2])	#PDseat21
				PD4w.append(wheelchair_wifi_data[3])	#PDseat22
				PD5w.append(wheelchair_wifi_data[4])	#PDseat31
				PD6w.append(wheelchair_wifi_data[5])	#PDseat32
				PD7w.append(wheelchair_wifi_data[6])	#PDseat41
				PD8w.append(wheelchair_wifi_data[7])	#PDseat42
				PD9w.append(wheelchair_wifi_data[8])  	#PDseat51
				PD10w.append(wheelchair_wifi_data[9])	#PDseat52
				PD11w.append(wheelchair_wifi_data[10])	#PDseat61
				PD12w.append(wheelchair_wifi_data[11])	#PDback11
				PD13w.append(wheelchair_wifi_data[12])	#PDback12
				PD14w.append(wheelchair_wifi_data[13])	#PDback21
				PD15w.append(wheelchair_wifi_data[14])	#PDback22
				PD16w.append(wheelchair_wifi_data[15])	#PDback31
				PD17w.append(wheelchair_wifi_data[16])	#PDback32
				PD18w.append(wheelchair_wifi_data[17])	#PDback41
				PD19w.append(wheelchair_wifi_data[18])	#PDback42
				PD20w.append(wheelchair_wifi_data[19])	#PDback51
				PD21w.append(wheelchair_wifi_data[20])	#PDback52
				PD22w.append(wheelchair_wifi_data[21])	#PDback61
				PD23w.append(wheelchair_wifi_data[22])	#PDback62
				
				PDslists=PD1w,PD2w,PD3w,PD4w,PD5w,PD6w,PD7w,PD8w,PD9w,PD10w,PD11w,PD12w,PD13w,PD14w,PD15w,PD16w,PD17w,PD18w,PD19w,PD20w,PD21w,PD22w,PD23w
				
				for i in PDslists:
					if len(i) == maxsamples:
						i.pop(0)#Update the last values				
						datasetPDs.append(i)
				#print("before overlap: ",datasetPDs[0])
				if (len(datasetPDs)==23):	
					del datasetPDs[0][0:overlap]
					del datasetPDs[1][0:overlap]
					del datasetPDs[2][0:overlap]
					del datasetPDs[3][0:overlap]
					del datasetPDs[4][0:overlap]
					del datasetPDs[5][0:overlap]
					del datasetPDs[6][0:overlap]
					del datasetPDs[7][0:overlap]
					del datasetPDs[8][0:overlap]
					del datasetPDs[9][0:overlap]
					del datasetPDs[10][0:overlap]
					del datasetPDs[11][0:overlap]
					del datasetPDs[12][0:overlap]
					del datasetPDs[13][0:overlap]
					del datasetPDs[14][0:overlap]
					del datasetPDs[15][0:overlap]
					del datasetPDs[16][0:overlap]
					del datasetPDs[17][0:overlap]
					del datasetPDs[18][0:overlap]
					del datasetPDs[19][0:overlap]
					del datasetPDs[20][0:overlap]
					del datasetPDs[21][0:overlap]
					del datasetPDs[22][0:overlap]	
					
					t5 = threading.Thread(name="features",target=self.features(datasetPDs,wheelchair_wifi_data,knn_from_joblib), args=())		#Send info to the fuzzy controller
					t5.start()					
				datasetPDs.clear()
	
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Real-time classifier implementation	
	
	def features(self,datasetPDs,datawheelchair,knn_from_joblib):		#variance and rms in time and frequency domain for each PD
		try:
			#print("Samples: ",datasetPDs[0],len(datasetPDs))					
			#print("after overlap: ",datasetPDs[0])
			varPD1= np.var(np.array(datasetPDs[0]))
			varPD2= np.var(np.array(datasetPDs[1]))
			varPD3= np.var(np.array(datasetPDs[2]))
			varPD4= np.var(np.array(datasetPDs[3]))
			varPD5= np.var(np.array(datasetPDs[4]))
			varPD6= np.var(np.array(datasetPDs[5]))
			varPD7= np.var(np.array(datasetPDs[6]))
			varPD8= np.var(np.array(datasetPDs[7]))
			varPD9= np.var(np.array(datasetPDs[8]))
			varPD10= np.var(np.array(datasetPDs[9]))
			varPD11= np.var(np.array(datasetPDs[10]))
			varPD12= np.var(np.array(datasetPDs[11]))
			varPD13= np.var(np.array(datasetPDs[12]))
			varPD14= np.var(np.array(datasetPDs[13]))
			varPD15= np.var(np.array(datasetPDs[14]))
			varPD16= np.var(np.array(datasetPDs[15]))
			varPD17= np.var(np.array(datasetPDs[16]))
			varPD18= np.var(np.array(datasetPDs[17]))
			varPD19= np.var(np.array(datasetPDs[18]))
			varPD20= np.var(np.array(datasetPDs[19]))
			varPD21= np.var(np.array(datasetPDs[20]))
			varPD22= np.var(np.array(datasetPDs[21]))
			varPD23= np.var(np.array(datasetPDs[22]))		
			rmsPD1= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[0]),2))))
			rmsPD2= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[1]),2))))
			rmsPD3= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[2]),2))))
			rmsPD4= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[3]),2))))
			rmsPD5= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[4]),2))))
			rmsPD6= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[5]),2))))
			rmsPD7= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[6]),2))))
			rmsPD8= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[7]),2))))
			rmsPD9= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[8]),2))))
			rmsPD10= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[9]),2))))
			rmsPD11= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[10]),2))))
			rmsPD12= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[11]),2))))
			rmsPD13= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[12]),2))))
			rmsPD14= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[13]),2))))
			rmsPD15= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[14]),2))))
			rmsPD16= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[15]),2))))
			rmsPD17= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[16]),2))))
			rmsPD18= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[17]),2))))
			rmsPD19= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[18]),2))))
			rmsPD20= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[19]),2))))
			rmsPD21= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[20]),2))))
			rmsPD22= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[21]),2))))
			rmsPD23= np.sqrt(np.mean(abs(np.power(np.array(datasetPDs[22]),2))))			
			varfreqPD1= np.var(np.fft.fft(np.array(datasetPDs[0])))
			varfreqPD2= np.var(np.fft.fft(np.array(datasetPDs[1])))
			varfreqPD3= np.var(np.fft.fft(np.array(datasetPDs[2])))
			varfreqPD4= np.var(np.fft.fft(np.array(datasetPDs[3])))
			varfreqPD5= np.var(np.fft.fft(np.array(datasetPDs[4])))
			varfreqPD6= np.var(np.fft.fft(np.array(datasetPDs[5])))
			varfreqPD7= np.var(np.fft.fft(np.array(datasetPDs[6])))
			varfreqPD8= np.var(np.fft.fft(np.array(datasetPDs[7])))
			varfreqPD9= np.var(np.fft.fft(np.array(datasetPDs[8])))
			varfreqPD10= np.var(np.fft.fft(np.array(datasetPDs[9])))
			varfreqPD11= np.var(np.fft.fft(np.array(datasetPDs[10])))
			varfreqPD12= np.var(np.fft.fft(np.array(datasetPDs[11])))
			varfreqPD13= np.var(np.fft.fft(np.array(datasetPDs[12])))
			varfreqPD14= np.var(np.fft.fft(np.array(datasetPDs[13])))
			varfreqPD15= np.var(np.fft.fft(np.array(datasetPDs[14])))
			varfreqPD16= np.var(np.fft.fft(np.array(datasetPDs[15])))
			varfreqPD17= np.var(np.fft.fft(np.array(datasetPDs[16])))
			varfreqPD18= np.var(np.fft.fft(np.array(datasetPDs[17])))
			varfreqPD19= np.var(np.fft.fft(np.array(datasetPDs[18])))
			varfreqPD20= np.var(np.fft.fft(np.array(datasetPDs[19])))
			varfreqPD21= np.var(np.fft.fft(np.array(datasetPDs[20])))
			varfreqPD22= np.var(np.fft.fft(np.array(datasetPDs[21])))
			varfreqPD23= np.var(np.fft.fft(np.array(datasetPDs[22])))
			rmsfreqPD1= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[0])),2)))))
			rmsfreqPD2= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[1])),2)))))
			rmsfreqPD3= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[2])),2)))))
			rmsfreqPD4= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[3])),2)))))
			rmsfreqPD5= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[4])),2)))))
			rmsfreqPD6= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[5])),2)))))
			rmsfreqPD7= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[6])),2)))))
			rmsfreqPD8= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[7])),2)))))
			rmsfreqPD9= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[8])),2)))))
			rmsfreqPD10= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[9])),2)))))
			rmsfreqPD11= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[10])),2)))))
			rmsfreqPD12= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[11])),2)))))
			rmsfreqPD13= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[12])),2)))))
			rmsfreqPD14= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[13])),2)))))
			rmsfreqPD15= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[14])),2)))))
			rmsfreqPD16= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[15])),2)))))
			rmsfreqPD17= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[16])),2)))))
			rmsfreqPD18= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[17])),2)))))
			rmsfreqPD19= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[18])),2)))))
			rmsfreqPD20= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[19])),2)))))
			rmsfreqPD21= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[20])),2)))))
			rmsfreqPD22= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[21])),2)))))
			rmsfreqPD23= abs(np.sqrt(np.mean(abs(np.power(np.fft.fft(np.array(datasetPDs[22])),2)))))
			features_PDs.append([varPD1,rmsPD1,varfreqPD1,rmsfreqPD1,varPD2,rmsPD2,varfreqPD2,rmsfreqPD2,varPD3,rmsPD3,varfreqPD3,rmsfreqPD3,varPD4,rmsPD4,varfreqPD4,rmsfreqPD4,varPD5,rmsPD5,varfreqPD5,rmsfreqPD5,varPD6,rmsPD6,varfreqPD6,rmsfreqPD6,varPD7,rmsPD7,varfreqPD7,rmsfreqPD7,varPD8,rmsPD8,varfreqPD8,rmsfreqPD8,varPD9,rmsPD9,varfreqPD9,rmsfreqPD9,varPD10,rmsPD10,varfreqPD10,rmsfreqPD10,varPD11,rmsPD11,varfreqPD11,rmsfreqPD11,varPD12,rmsPD12,varfreqPD12,rmsfreqPD12,varPD13,rmsPD13,varfreqPD13,rmsfreqPD13,varPD14,rmsPD14,varfreqPD14,rmsfreqPD14,varPD15,rmsPD15,varfreqPD15,rmsfreqPD15,varPD16,rmsPD16,varfreqPD16,rmsfreqPD16,varPD17,rmsPD17,varfreqPD17,rmsfreqPD17,varPD18,rmsPD18,varfreqPD18,rmsfreqPD18,varPD19,rmsPD19,varfreqPD19,rmsfreqPD19,varPD20,rmsPD20,varfreqPD20,rmsfreqPD20,varPD21,rmsPD21,varfreqPD21,rmsfreqPD21,varPD22,rmsPD22,varfreqPD22,rmsfreqPD22,varPD23,rmsPD23,varfreqPD23,rmsfreqPD23])	#All features
			scaler = MinMaxScaler()
			
			#features_PDs_array=np.array([features_PDs])
			data_model = scaler.fit_transform(features_PDs)			#Data normalization	
			pred_labels = knn_from_joblib.predict(data_model)

			pred_confidences = knn_from_joblib.predict_proba(data_model)
			print(pred_labels)
			features_PDs.clear()
			"""
			print(len(features_PDs))
			if (len(features_PDs)==features_quantity):	#features rows
				scaler = MinMaxScaler()
				features_PDs_array=np.array([features_PDs])
				data_model = scaler.fit_transform(features_PDs)			#Data normalization		
				knn_from_joblib = joblib.load('ETC.pkl')		#Load classification model
				output_list=knn_from_joblib.predict(data_model)
				print(output_list,mode(output_list))	#Mode number to choose command
				features_PDs.clear()
			"""
				
		except IndexError:
			pass
			
				
			
			
	
	def listeachPD(self,list1):   
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
		return PD1w,PD2w,PD3w,PD4w,PD5w,PD6w,PD7w,PD8w,PD9w,PD10w,PD11w,PD12w,PD13w,PD14w,PD15w,PD16w,PD17w,PD18w,PD19w,PD20w,PD21w,PD22w,PD23w,PD24w
	
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
		
	def filter_wifi_data(self,wifidata):	#Mean filter complete WiFi data: wheelchair-neck
		datawheelchair= Queue()
		print("First data: ",wifidata)
		PDslists=self.listeachPD(wifidata)		
		for i in PDslists:
			if len(i) == maxsamples:
				i.pop(0)#Update the last values
				#print("Values: ",i)
				dataPDs_butter = self.butter_lowpass_filter(order,i, w)
				#print("Filtered value: ",dataPDs_butter)				
				datasetPDs.append(dataPDs_butter)	
				if (len(datasetPDs)==24):	#convert to columns
					wheelchairPDsarray = np.stack((datasetPDs[0], datasetPDs[1],datasetPDs[2],datasetPDs[3],datasetPDs[4],datasetPDs[5],datasetPDs[6],datasetPDs[7],datasetPDs[8],datasetPDs[9],datasetPDs[10],datasetPDs[11],datasetPDs[12],datasetPDs[13],datasetPDs[14],datasetPDs[15],datasetPDs[16],datasetPDs[17],datasetPDs[18],datasetPDs[19],datasetPDs[20],datasetPDs[21],datasetPDs[22],datasetPDs[23]), axis=1)
					dfwheelchair = pd.DataFrame(wheelchairPDsarray)
					meanswheelchair=self.processCARfilter(dfwheelchair)
					print("means wheelchair: ",meanswheelchair)						
					self.clearfilters(meanswheelchair)
					datawheechair.put(meanswheelchair)
					t5 = threading.Thread(name="posture_processing",target=self.posture_processing(datawheechair), args=())		#Send info to the fuzzy controller
					t5.start()					
					self.clearfilters(meanswheelchair)					
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
						#t6 = threading.Thread(name="design_fuzzy_control",target=self.send_info_wheelchair(), args=(datawheelblue,))
						#t6.start()
	
	def send_info_wheelchair(self,datawheelblue,tipping):
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
