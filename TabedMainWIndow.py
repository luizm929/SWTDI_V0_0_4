# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\SWTDI_GUI\TabedMainWIndow.ui'
#
#Written by Luis Martinez  luizmartines@gmail.com

from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
#from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtWidgets import  QMainWindow,QSizePolicy, QMessageBox, QWidget
from PyQt5.QtWidgets import (QApplication, QMainWindow,QSizePolicy, QMessageBox,QWidget, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)

from PyQt5.QtGui import QPainter, QFont, QColor, QBrush
#########Ploting Modules
#from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib import pyplot as plt

import matplotlib.animation as animation
from matplotlib import style
import sys
import numpy as np
#from window_at_load_level import Ui_Form as Form 
from window_at_load_level import Ui_Form

class mplCanvas(FigureCanvas):
    def __init__(self,parent=None,width=5,height=4,dpi=100):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        #we clear the screen otherwise we run out of memory. 
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass
    
#############################################################
#Each plot has one of these. 
#Outlet 1 POWER

class dynPlot1(mplCanvas):
    
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)
    def compute_initial_figure(self):
        self.axes.plot([0,1,2,3], [0,1,2,3], 'r')
        
    def update_figure(self):
        f = open('E:\SWTDI_GUI\outlet1.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')
            
            x.append(float(hold[0]))
            y.append(float(hold[1]))
            
        self.axes.plot(x,y, 'r', label='Power (W)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Power (W)')
        ###Legend on plot
        self.axes.legend(loc='upper left')
        
        self.draw()

        
#Outlet 2 VOltage
class dynPlot2(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)
    def compute_initial_figure(self):
        self.axes.plot([0,1,2,3], [0,1,2,3], 'r')

    def update_figure(self):
        f = open('E:\SWTDI_GUI\outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')
            
            x.append(float(hold[0]))
            y.append(float(hold[1]))
            
        self.axes.plot(x,y, 'r', label='Voltage (V)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Voltage (V)')
        ###Legend on plot
        self.axes.legend(loc='upper left')
        self.draw()

#CUrrent
class dynPlot3(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)
    def compute_initial_figure(self):
        self.axes.plot([0,1,2,3], [0,1,2,3], 'r')

    def update_figure(self):
        f = open('E:\SWTDI_GUI\outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')
            
            x.append(float(hold[0]))
            y.append(float(hold[1]))
            
        self.axes.plot(x,y, 'r', label='Current (A)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Current (A)')
        ###Legend on plot
        self.axes.legend(loc='upper left')
        self.draw()

#Temperature        
class dynPlot4(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)
    def compute_initial_figure(self):
        self.axes.plot([0,1,2,3], [0,1,2,3], 'r')

    def update_figure(self):
        f = open('E:\SWTDI_GUI\outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')
            
            x.append(float(hold[0]))
            y.append(float(hold[1]))
            
        self.axes.plot(x,y, 'r', label='Temperature (F)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Temperature (F)')
        ###Legend on plots
        self.axes.legend(loc='upper left')
        self.draw()
####################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1335, 769)
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1600, 920))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #---------------------------
        
        
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        
        
        
        
        
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1335, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAdministrator = QtWidgets.QMenu(self.menubar)
        self.menuAdministrator.setObjectName("menuAdministrator")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAdministrator.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    # def voltUpdate(self):
        # f = open('E:\SWTDI_GUI\outlet2.txt', 'r')
        # d = f.readlines()
        
        # f.close()
        # voltage=120
        # voltage=QtGui.QLabel(str(voltage ),self)
        # voltageUpdate.resize(VoltageUpdate.sizeHint())
        # voltage.move(160,100)
        # voltUpdate.move(170,100)
        # # after 4 sec call self.updateLabel
        # #QtCore.QTimer.singleShot(3000, lambda: self.updateLabel(voltageUpdate)
        
        # newVoltage=int(voltageUpdate.text()) +1
        # voltageUpdate.setText(str(newVoltage))
        # QtCore.QTimer.singleshot(3000, lambda: self.updateLabel(voltageUpdate))
        
    
    
    
    
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 5"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAdministrator.setTitle(_translate("MainWindow", "Administrator"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAbout.setText(_translate("MainWindow", "About"    ))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())