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
from main import *
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



        #######################################################################
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## == #






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