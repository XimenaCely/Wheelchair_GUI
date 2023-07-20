# Wheelchair_GUI
This repository contains information about the design of a Graphic User Interface used for wheelchair control and posture monitoring.
The GUI was developed in Python and using Qt Creator to design the interface and all blocks involved.
The "main" file executes the whole interface and other files related to posture monitoring and wheelchair controllers. Some libraries need to be installed or imported such as:
* Socket
* threading
* PySide2
* skfuzzy
* scipy
* sklearn
* numpy
* joblib
* pandas
Moreover, the images need to be in the same carpet, so, if you wanna install and execute the application it is necessary to change the path of some images used in the interface.

In terms of code, there are Python files which execute the buttons and other elements of the interface. Those files are named such as "ui_..." For instance, the main file is "ui_Desktop_app", where the main window is being executed. Other blocks are "neck_control", "manual_control", "head_control" and "posture_monitoring". All files related to the interface are name in the same way, only changing for "ui_..."
The application could not work if the socket library is calling a communication between ESP32 devices. However, you can comment these lines in order to execute the application. 
Files with extension ".plk" were imported to evaluate the posture monitoring system, and they are a good example to import data from a classification system. Moreover, some carpets are used to save elements from the interface such as progress Bars, icons, among others. 

