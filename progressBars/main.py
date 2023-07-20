#####
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
import qdarkstyle
from PySide2 import QtCore
########################################################################
## 
########################################################################

# #########################
# IMPORT GUI FILE
from ui_main import *
# ##########################

# GLOBAL
progress_val = 0



########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # APPLY QDARKSTYLE THEME
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())


        # SET PROGRESS BAR VALUE
        self.ui.progressBar.rpb_setMaximum(420) 

        # SET PROGRESS BAR STYLE
        self.ui.progressBar.rpb_setBarStyle('Donet')

        # SET PROGRESS BAR LINE COLOR
        self.ui.progressBar.rpb_setLineColor((0, 170, 255)) #ARGUMENT RGB AS A TUPLE

        #CHANGING THE PATH COLOR
        self.ui.progressBar.rpb_setPathColor((255, 30, 99))

        #SET PROGRESS BAR TEXT COLOR
        self.ui.progressBar.rpb_setTextColor((233, 30, 99)) #ARGUMENT RGB AS A TUPLE

        # SET PROGRESS BAR STARTING POSITION
        # North, East, West, South
        self.ui.progressBar.rpb_setInitialPos('West') #WEST AS STARTING POSITION.

        #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
        # Value, Percentage
        self.ui.progressBar.rpb_setTextFormat('Percentage')

        #SET PROGRESS BAR FONT
        self.ui.progressBar.rpb_setTextFont('Arial')
        
        #TEXT HIDDEN
        self.ui.progressBar.rpb_enableText(False) 

        #SET PROGRESS BAR LINE WIDTH 
        self.ui.progressBar.rpb_setLineWidth(10)

        #PATH WIDTH
        self.ui.progressBar.rpb_setPathWidth(15)

        #SET PROGRESS BAR LINE CAP
        # RoundCap, SquareCap
        self.ui.progressBar.rpb_setLineCap('RoundCap')

        #LINE STYLE
        # DotLine, DashLine
        self.ui.progressBar.rpb_setLineStyle('DotLine')


        #######################################################################
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## == #



        # ANIMATE THE PROGRESS
        # LETS ADD TIMER TO CHANGE PROGRESSES
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress) #progress function
        self.timer.start(60)

        # Change all progresses to zero on start
        QtCore.QTimer.singleShot(0, lambda: self.ui.progressBar.rpb_setValue(0))



    def progress(self):        
        global progress_val
        # Set progress values
        self.ui.progressBar.rpb_setValue(progress_val)
        

        # Reset progresses if the maximum value is reached
        if progress_val > 420:
            progress_val = 0;
            

        # Increase value every 60 ms
        progress_val+=1




########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################       