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

from ui_neck_control_ui import  Ui_neck_window
#Variables for UDP communication
msgFromClient       = "0"		#Security command to the wheelchair
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
		
		#Wheelchair connection
		global arduino
		arduino = serial.Serial(port='COM10', baudrate=115200, timeout=.1)	
			
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
		self.start_wizard_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\power-on.png"))
		self.stop_btn.setIcon(QtGui.QIcon(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\icons8-stop-sign-96.png"))
		self.stop_btn.clicked.connect(self.stop_control)
		self.pixmap = QPixmap(r"C:\Users\Personal\Desktop\wheelchair_project\Desktop_app\icons\neck_pillow.png")
		self.neck_pillow_guide.setPixmap(self.pixmap)				
		self.show()
			
	def startWizard(self):
		global activeWidget
		self.pages.expandMenu()
		self.welcome.collapseMenu()		
		
	def stopWizard(self):
		self.pages.collapseMenu()
		self.welcome.expandMenu()
	
	def stop_control(self):
		print("stop","0")
		arduino.write(str.encode("0"))
		time.sleep(10)
			
	def come_back_mainmenu(self):
		#arduino.write(str.encode("0"))
		#time.sleep(10)
		self.UDPClientSocketneck.shutdown(socket.SHUT_RDWR)
		self.UDPClientSocketneck.close()
		
		print("serial status: ",arduino.is_open)
		if(arduino.is_open == True):
			arduino.close()	
		
		from main import MainWindow
		window=MainWindow()		
			
	#Thread functions
	def psutil_thread(self):
		t1 = threading.Thread(name="fuzzy",target=self.fuzzy, args=())		#Send info to the fuzzy controller	with wifi comm
		t1.start()
		
		#t2 = threading.Thread(name="blue_communication",target=self.blue_communication, args=())
		#t2.start()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Seinding wheelchair commands
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Process wifi data and filtering process
			
	def start_comm(self,tipping): 
		datawifiwheelchair=[]
		datawifineck=[]		
		dataneck= Queue()
		self.UDPClientSocketneck.sendto(bytesToSend, serverAddressPortNeck)
		while True:			
			#clean neck data			
			msgFromServerneck = self.UDPClientSocketneck.recvfrom(bufferSize) 
			neck_data=msgFromServerneck[0].decode("utf-8")			
			neck_data=neck_data.rstrip()
			neck_data = neck_data.strip('\n')
			neck_data = neck_data.split(",")
			newLista=filter(lambda x:not x in ("",None),neck_data)	#clean None values			
			neck_wifi_data = [int(item) for item in newLista]				
			dataneck.put(neck_wifi_data)
			#print("Raw data first: ",neck_wifi_data)			
			t6 = threading.Thread(name="sending_data_wheelchair",target=self.sending_data_wheelchair, args=(dataneck,tipping,))		#Send info to the fuzzy controller
			t6.start()
			
	
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
			knn_from_joblib = joblib.load('ExtraTreesClassifierwithout.pkl')		#Load classification model
			output_list=knn_from_joblib.predict(data_model)
			print(output_list,mode(output_list))	#Mode number to choose command
			features_PDs.clear()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Fuzzy logic controller
	def fuzzy(self):
		# Input and output functions
		PD1 = ctrl.Antecedent(np.linspace(-5000, 5000,100), 'PD1')
		PD2 = ctrl.Antecedent(np.linspace(-5000,5000,100), 'PD2')
		dir = ctrl.Consequent(np.linspace(0, 5.01, 100), 'direction')#Fuzzify and defuzz inputs and output
		#Membership functions for neck movements
		
		#Discurse universe for PD1
		PD1['forw1'] = fuzz.trimf(PD1.universe, [-1000, -800, -601]) 
		PD1['left1'] = fuzz.trimf(PD1.universe, [-400,-325,-50])
		PD1['right1'] = fuzz.trimf(PD1.universe, [-2500,-1750,-1000])
		PD1['stop1'] = fuzz.trimf(PD1.universe, [-250, 0, 300]) 
		PD1['stop11'] = fuzz.trimf(PD1.universe, [-30000, -13000, -2500]) 
		PD1['stop111'] = fuzz.trimf(PD1.universe, [2000, 14000, 30000]) 
		PD1['zeroval'] = fuzz.trimf(PD1.universe, [300, 1150, 2000]) 	#Response after set zero values 		
		
		
		#Discurse universe for PD2
		PD2['forw2'] = fuzz.trimf(PD2.universe, [-250, 0, 250]) 
		PD2['left2'] = fuzz.trimf(PD2.universe, [1500,2200,3000])
		PD2['right2'] = fuzz.trimf(PD2.universe, [-500,-350,0])
		PD2['stop2'] = fuzz.trimf(PD2.universe, [-250,0,250])
		PD2['stop22'] = fuzz.trimf(PD2.universe, [-30000,-14000,-800])
		PD2['stop23'] = fuzz.trimf(PD2.universe, [-800,-500,250])
		PD2['stop24'] = fuzz.trimf(PD2.universe, [3000,14000,30000])
		
		#Discurse universe for direction
		dir['forw'] = fuzz.trimf(dir.universe,[0.9, 1, 1.1])
		dir['right'] = fuzz.trimf(dir.universe,[1.9, 2, 2.1])
		dir['left'] = fuzz.trimf(dir.universe,[2.9, 3, 3.1])
		dir['stop'] = fuzz.trimf(dir.universe,[-0.1, 0, 0.1])
		#dir['back'] = fuzz.trimf(dir.universe,[3.9, 4, 4.1])

		#Linguistic rules
		rule1 = ctrl.Rule(PD1['forw1'] & PD2['forw2'], dir['forw'])
		rule2 = ctrl.Rule(PD1['right1'] & PD2['right2'], dir['right'])
		rule3 = ctrl.Rule(PD1['left1'] & PD2['left2'], dir['left'])
		rule4 = ctrl.Rule(PD1['right1'] & PD2['forw2'], dir['right'])
		rule5 = ctrl.Rule(PD1['stop1'] & PD2['stop2'], dir['stop'])
		rule6 = ctrl.Rule(PD1['stop1'] & PD2['stop22'], dir['stop'])
		rule7 = ctrl.Rule(PD1['stop1'] & PD2['stop23'], dir['stop'])
		rule8 = ctrl.Rule(PD1['zeroval'] & PD2['stop2'], dir['stop'])
		rule9 = ctrl.Rule(PD1['zeroval'] & PD2['left2'], dir['stop'])
		rule10 = ctrl.Rule(PD1['stop111'] & PD2['stop24'], dir['stop'])

		tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10])
		tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
		#Send fuzzy output
		t7 = threading.Thread(name="start_comm",target=self.start_comm, args=(tipping,))		
		t7.start()
		
	def sending_data_wheelchair(self,dataneck,tipping):
		while dataneck.empty() is False:
			initialize_time=time.time()
			neck_wifi_data= dataneck.get()						
			#print("Raw data: ", neck_wifi_data)
			tipping.input['PD1'] = neck_wifi_data[0]
			tipping.input['PD2'] = neck_wifi_data[1]			
			try:
				tipping.compute()
				comm=int(round(tipping.output['direction']))
				comm=str(comm)
				#print("PDs_after:",neck_wifi_data)
				print("msg_wheelchair: ",comm)
				self.send_comm(comm)	
				final_time=time.time()
				execution_time=final_time-initialize_time
				#print("Response time: ",execution_time)
			except:
				pass
	
	def send_comm(self,comm):
		#print("Send data wheelchair")
		arduino.write(str.encode(comm))
		#data = arduino.readline()
		#print(data)
		#time.sleep(0.5)
		#print("Sent")
		
	"""	
	def send_comm(self,msg_wheelchair):
		t8 = threading.Thread(name="talkWheelchair",target=self.talkToClient, args=(msg_wheelchair,))
		t8.start()
		
	
	def send_comm(self,comm):
		#print("Send data wheelchair")
		arduino.write(str.encode(comm))
		time.sleep(1)
		#print("Sent")
	"""
		
	def talkToClient(self,msg):
		bytesToSend = str.encode(msg)
		self.UDPClientSocketneck.sendto(bytesToSend, serverAddressPortWheelchair)
		print("msg: ",msg)
		time.sleep(0.1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Receiving data		
			
	def filter_wifi_neck_data(self,wifidata):	#Update data		
		PD1n.append(wifidata[0])  
		PD2n.append(wifidata[1]) 
		PDslists=PD1n,PD2n
		for i in PDslists:
			if len(i) == maxsamples:
				i.pop(0)#Update the last values				
				datasetPDs.append(i)
		if (len(datasetPDs)==2):	
			del datasetPDs[0][0:overlap]
			del datasetPDs[1][0:overlap]
			#t5 = threading.Thread(name="features",target=self.features(datasetPDs,wifidata), args=())		#Send info to the fuzzy controller
			#t5.start()	
			t6 = threading.Thread(name="fuzzy",target=self.fuzzy(datasetPDs,wifidata), args=())		#Send info to the fuzzy controller
			t6.start()	
		
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
