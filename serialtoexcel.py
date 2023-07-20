

import serial
import xlwt
from datetime import datetime

class SerialToExcel:

    def __init__(self,port,speed):
        
        self.port = port
        self.speed = speed

        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet("Data from Serial",cell_overwrite_ok=True)
        self.ws.write(0, 0, "Data from Serial")
        self.columns = ["Date Time"]
        self.number = 100
        self.sensor=0
        self.weight=0
        

    def setColumns(self,col):
        self.columns.extend(col)  
        self.sensor= col[2]
        self.weight= col[3]
        
    def setRecordsNumber(self,number):
        self.number = number
        print("number: ",number)
        
    def readPort(self):
        ser = serial.Serial(self.port, self.speed, timeout=1)
        c = 0
        for col in self.columns:
            self.ws.write(1, c, col)
            c = c + 1
        self.fila = 2

        i = 0
        while(i<self.number):
            line = str(ser.readline())
            #print(line)
            print(i)
            bin2=[]
            out=[]
            bincomma=line.split(",")
            for k in range(len(bincomma)):
              for j in range(len(bincomma[k])):
                if bincomma[k][j]=="0" or bincomma[k][j]=="1" or bincomma[k][j]=="2" or bincomma[k][j]=="3" or bincomma[k][j]=="4" or bincomma[k][j]=="5" or bincomma[k][j]=="6" or bincomma[k][j]=="7" or bincomma[k][j]=="8" or bincomma[k][j]=="9":
                  bin2.append(bincomma[k][j])  
                binn=''.join(bin2)
              out.append(binn)
              bin2=[]
            outst=','.join(out)
            print(outst)
            out=[]
            if(len(outst) > 0):
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                #print(date_time,outst)
                if(outst.find(",")):
                    c = 1
                    self.ws.write(self.fila, 0, date_time)
                    self.ws.write(self.fila, 3, self.sensor)
                    self.ws.write(self.fila, 4, self.weight)
                    self.ws.write(self.fila, 5, i)
                    columnas = outst.split(",")
                    for col in columnas:
                        self.ws.write(self.fila, c, col)
                        c = c + 1

                i = i + 1
                self.fila = self.fila + 1
    
    def writeFile(self,archivo):
    	self.wb.save(archivo)

    
    def writeFile(self,archivo):
    	self.wb.save(archivo)



  


#Final version
