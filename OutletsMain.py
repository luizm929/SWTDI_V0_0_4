# -*- coding: utf-8 -*-
#--------------------------------
# Packages needed
#Matplotlib
#Python3
#PyQt5
#
#------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
# Thanks to Jose Tabarez for his help.
#------------------------------------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys
import random
import matplotlib

from OutletWindowV5 import Ui_InOutletsWindow

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import  QMainWindow,QSizePolicy, QMessageBox, QWidget
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QMessageBox, QWidget, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

from PyQt5.QtGui import QPainter, QFont
#########Ploting Modules
# from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib import pyplot as plt

# icon size
x = 60
y = 50


# One canvas for all plots this is why plots update
# with a bit of latency in the milli seconds. We want less latency we create
# one class for each plot with the risk of using more memory.
# TODO
# Create classes for all the houses so there is less latency.


# class Ui_MainWindow(object):
class Ui_outlets(object):
    def __init__(self):
        super(Ui_outlets, self).__init__()

        # These are the functions (slots) for each button.

    def home1(self):
        print("Outlet 1 clicked")
        self.OutletsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_InOutletsWindow()
        self.ui.setupUi(self.OutletsWindow)
        # w.hide()
        self.OutletsWindow.show()
        # w.hide()

    def home2(self):
        print("Outlet 2 clicked")

    def home3(self):
        print("Outlet 3 clicked")

    def home4(self):
        print("Outlet 4 clicked")

    def home5(self):
        print("Outlet 5 clicked")

    def home6(self):
        print("Outlet 6 clicked")

    def home7(self):
        print("Outlet 7 clicked")

    def home8(self):
        print("Outlet 8 clicked")

    def home9(self):
        print("Outlet 9 clicked")

    def home10(self):
        print("Outlet 10 clicked")

    def home11(self):
        print("Outlet 11 clicked")

    def home12(self):
        print("Outlet 12 clicked")

    def home13(self):
        print("Outlet 13 clicked")

    def home14(self):
        print("Outlet 14 clicked")

    def home15(self):
        print("Outlet 15 clicked")

    def home16(self):
        print("Outlet 16 clicked")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1108, 672)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ##This is where the embedded widgets which hold the live plots live. If
        ##there are performance issues we will use pyqtgraph which is suppossed
        ##to be built for perfomrance
        # This is we call the canvas and put it in the main gui(or centralwidget).
        self.PowPlotHouse1 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse2 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse3 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse4 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse5 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse6 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse7 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse8 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse9 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse10 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse11 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse12 = QtWidgets.QWidget(self.centralwidget)

        # Create the layout horizontally of the plots above
        # if we want a vertical layout QVBoxLayout()
        layout = QGridLayout()

        # We call the function with the plot or idata to create the plot
        power = dynPlot1(self.PowPlotHouse1, width=10, height=5, dpi=60)
        power2 = dynPlot2(self.PowPlotHouse2, width=10, height=5, dpi=60)
        power3 = dynPlot3(self.PowPlotHouse3, width=10, height=5, dpi=60)
        power4 = dynPlot4(self.PowPlotHouse4, width=10, height=5, dpi=60)
        power5 = dynPlot5(self.PowPlotHouse5, width=10, height=5, dpi=60)
        power6 = dynPlot6(self.PowPlotHouse6, width=10, height=5, dpi=60)
        power7 = dynPlot7(self.PowPlotHouse7, width=10, height=5, dpi=60)
        power8 = dynPlot8(self.PowPlotHouse8, width=10, height=5, dpi=60)
        power9 = dynPlot9(self.PowPlotHouse9, width=10, height=5, dpi=60)
        power10 = dynPlot10(self.PowPlotHouse10, width=10, height=5, dpi=60)
        power11 = dynPlot11(self.PowPlotHouse11, width=10, height=5, dpi=60)
        power12 = dynPlot12(self.PowPlotHouse12, width=10, height=5, dpi=60)

        ###################################################

        #
        # Plots are in odd columns
        layout.addWidget(power, 1, 1)
        layout.addWidget(power2, 1, 3)
        layout.addWidget(power3, 1, 5)
        layout.addWidget(power4, 1, 7)
        layout.addWidget(power5, 3, 1)
        layout.addWidget(power6, 3, 3)
        layout.addWidget(power7, 3, 5)
        layout.addWidget(power8, 3, 7)
        layout.addWidget(power9, 5, 1)
        layout.addWidget(power10, 5, 3)
        layout.addWidget(power11, 5, 5)
        layout.addWidget(power12, 5, 7)

        self.PowPlotHouse1.setFocus()
        self.PowPlotHouse2.setFocus()
        self.PowPlotHouse3.setFocus()
        self.PowPlotHouse4.setFocus()
        self.PowPlotHouse5.setFocus()
        self.PowPlotHouse6.setFocus()
        self.PowPlotHouse7.setFocus()
        self.PowPlotHouse8.setFocus()
        self.PowPlotHouse9.setFocus()
        self.PowPlotHouse10.setFocus()
        self.PowPlotHouse11.setFocus()
        self.PowPlotHouse12.setFocus()

        # TODO
        # Need to work on scroll bars to snap to window when resized.
        """
        ## Vertical Scroll bar
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(0, 0, 21, 611))
        sizePolicy=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalScrollBar.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar.setSizePolicy(sizePolicy)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        ## Horizontal scroll bar
        """
        """
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 610, 1051, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, -30, 151, 141))
        self.label.setStyleSheet("border-image: url(:/img/NM_State_University_logo.png);")
        self.label.setText("")
        self.label.setObjectName("SWTDI Main Window")
        """

        ############################House 1#########################################
        self.house1 = QtWidgets.QPushButton(self.centralwidget)
        self.house1.setGeometry(QtCore.QRect(31, 31, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.house1.sizePolicy().hasHeightForWidth())
        self.house1.setSizePolicy(sizePolicy)
        self.house1.setAutoFillBackground(False)
        # object house1 is case sensitive stylesheet is also case sensitive.
        self.house1.setObjectName("house1")
        self.house1.setStyleSheet("#house1 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house1:pressed {\n"
                                  "    background: white;\n"
                                  "}")

        self.house1.setText("1\n")
        self.house1.setIconSize(QtCore.QSize(70, 20))
        ###Button house1
        # layout = QVBoxLayout()
        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house1.clicked.connect(self.home1)

        ## we add this widget to the gridlayout at position (0,0)
        layout.addWidget(self.house1, 0, 0)

        ############################House 2#########################################

        self.house2 = QtWidgets.QPushButton(self.centralwidget)
        # Arguments are ( h, v, x, y)
        self.house2.setGeometry(QtCore.QRect(258, 31, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house2.sizePolicy().hasHeightForWidth())
        self.house2.setSizePolicy(sizePolicy)
        self.house2.setObjectName("house2")
        self.house2.setStyleSheet("#house2 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house2:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house2.setText("2\n")

        ###Button house1
        # self.house2.setCheckable(True)
        self.house2.clicked.connect(self.home2)

        layout.addWidget(self.house2, 0, 2)
        ############################House 3#########################################
        self.house3 = QtWidgets.QPushButton(self.centralwidget)
        self.house3.setGeometry(QtCore.QRect(485, 31, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house3.sizePolicy().hasHeightForWidth())
        self.house3.setSizePolicy(sizePolicy)
        self.house3.setObjectName("house3")
        self.house3.setStyleSheet("#house3 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house3:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house3.setText("3\n")

        ###Button house1
        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house3.clicked.connect(self.home3)

        layout.addWidget(self.house3, 0, 4)

        ############################House 4#########################################        
        self.house4 = QtWidgets.QPushButton(self.centralwidget)
        self.house4.setGeometry(QtCore.QRect(711, 31, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house4.sizePolicy().hasHeightForWidth())
        self.house4.setSizePolicy(sizePolicy)
        self.house4.setObjectName("house4")
        self.house4.setStyleSheet("#house4 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house4:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house4.setText("4\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))

        ###Button house1
        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house4.clicked.connect(self.home4)

        layout.addWidget(self.house4, 0, 6)
        ############################House 5######################
        self.house5 = QtWidgets.QPushButton(self.centralwidget)
        self.house5.setGeometry(QtCore.QRect(31, 200, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house5.sizePolicy().hasHeightForWidth())
        self.house5.setSizePolicy(sizePolicy)
        self.house5.setObjectName("house5")
        self.house5.setStyleSheet("#house5 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house5:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house5.setText("5\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))

        ###Button house1
        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house5.clicked.connect(self.home5)

        layout.addWidget(self.house5, 2, 0)
        ############################House 6#########################################
        self.house6 = QtWidgets.QPushButton(self.centralwidget)
        self.house6.setGeometry(QtCore.QRect(258, 200, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house6.sizePolicy().hasHeightForWidth())
        self.house6.setSizePolicy(sizePolicy)
        self.house6.setObjectName("house6")
        self.house6.setStyleSheet("#house6 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house6:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house6.setText("6\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))
        ###Button house1

        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house6.clicked.connect(self.home6)

        layout.addWidget(self.house6, 2, 2)
        ############################House 7#########################################
        self.house7 = QtWidgets.QPushButton(self.centralwidget)
        self.house7.setGeometry(QtCore.QRect(484, 200, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house7.sizePolicy().hasHeightForWidth())
        self.house7.setSizePolicy(sizePolicy)
        #self.house7.setStyleSheet("border-image: url(:/img/Crystal_Clear_app_kfm_home.png);")
        self.house7.setText("")
        self.house7.setObjectName("house7")
        self.house7.setStyleSheet("#house7 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house7:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house7.setText("7\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))

        ###Button house1
        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house7.clicked.connect(self.home7)

        layout.addWidget(self.house7, 2, 4)

        ############################House 8#########################################


        self.house8 = QtWidgets.QPushButton(self.centralwidget)
        self.house8.setGeometry(QtCore.QRect(711, 200, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house8.sizePolicy().hasHeightForWidth())
        self.house8.setSizePolicy(sizePolicy)
        #self.house8.setStyleSheet("border-image: url(:/img/outlet.png);")
        self.house8.setText("")
        self.house8.setIconSize(QtCore.QSize(70, 20))
        self.house8.setAutoDefault(True)
        self.house8.setObjectName("house8")
        self.house8.setStyleSheet("#house8 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house8:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house8.setText("8\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))
        ###Button house1

        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house8.clicked.connect(self.home8)

        layout.addWidget(self.house8, 2, 6)

        ############################House 9#########################################
        self.house9 = QtWidgets.QPushButton(self.centralwidget)
        self.house9.setGeometry(QtCore.QRect(31, 368, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house9.sizePolicy().hasHeightForWidth())
        self.house9.setSizePolicy(sizePolicy)
        #self.house9.setStyleSheet("border-image: url(:/img/Crystal_Clear_app_kfm_home.png);")
        self.house9.setText("")
        self.house9.setObjectName("house9")
        self.house9.setStyleSheet("#house9 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house9:pressed {\n"
                                  "    background: white;\n"
                                  "}")
        self.house9.setText("9\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))
        ###Button house1

        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house9.clicked.connect(self.home9)

        layout.addWidget(self.house9, 4, 0)
        ############################House 10#########################################
        self.house10 = QtWidgets.QPushButton(self.centralwidget)
        self.house10.setGeometry(QtCore.QRect(258, 368, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house10.sizePolicy().hasHeightForWidth())
        self.house10.setSizePolicy(sizePolicy)
        #self.house10.setStyleSheet("border-image: url(:/img/outlet.png);")
        self.house10.setText("")
        self.house10.setObjectName("house10")
        self.house10.setStyleSheet("#house10 {\n"
                                   "border-image: url(:/img/outlet.png);\n"
                                   "font-size: 15px;"
                                   "font-weight: 600;"
                                   "text-align: left,top;"
                                   "}\n"
                                   "#house10:pressed {\n"
                                   "    background: white;\n"
                                   "}")
        self.house10.setText("10\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))
        ###Button house1

        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house10.clicked.connect(self.home10)

        layout.addWidget(self.house10, 4, 2)
        ############################House 11#########################################

        self.house11 = QtWidgets.QPushButton(self.centralwidget)
        self.house11.setGeometry(QtCore.QRect(484, 368, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house11.sizePolicy().hasHeightForWidth())
        self.house11.setSizePolicy(sizePolicy)
        #self.house11.setStyleSheet("border-image: url(:/img/outlet.png);")
        self.house11.setText("")
        self.house11.setObjectName("house11")
        self.house11.setStyleSheet("#house11 {\n"
                                   "border-image: url(:/img/outlet.png);\n"
                                   "font-size: 15px;"
                                   "font-weight: 600;"
                                   "text-align: left,top;"
                                   "}\n"
                                   "#house11:pressed {\n"
                                   "    background: white;\n"
                                   "}")
        self.house11.setText("11\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))
        ###Button house1

        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house11.clicked.connect(self.home11)

        layout.addWidget(self.house11, 4, 4)
        ############################House 12#########################################
        self.house12 = QtWidgets.QPushButton(self.centralwidget)
        self.house12.setGeometry(QtCore.QRect(711, 368, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house12.sizePolicy().hasHeightForWidth())
        self.house12.setSizePolicy(sizePolicy)
        #self.house12.setStyleSheet("border-image: url(:/img/Crystal_Clear_app_kfm_home.png);")
        self.house12.setText("")
        self.house12.setObjectName("house12")
        self.house12.setStyleSheet("#house12 {\n"
                                   "border-image: url(:/img/outlet.png);\n"
                                   "font-size: 15px;"
                                   "font-weight: 600;"
                                   "text-align: left,top;"
                                   "}\n"
                                   "#house12:pressed {\n"
                                   "    background: white;\n"
                                   "}")
        self.house12.setText("12\n")
        # self.house4.setIconSize(QtCore.QSize(70, 20))
        ###Button house1

        # self.house1.setCheckable(True)
        # self.house1.toggle()
        self.house12.clicked.connect(self.home12)

        layout.addWidget(self.house12, 4, 6)

        ######################Plot for house1#######################
        # This is were we embed th plot into the main window.
        """
        self.PowPlotHouse1 = QtWidgets.QWidget(self.centralwidget)

        lay = QVBoxLayout(self.PowPlotHouse1)
        power = dynPlot(self.PowPlotHouse1, width=5, height=4, dpi=100)
        #Location in the GUI of the widget
        self.PowPlotHouse1.setGeometry(QtCore.QRect(86, 30, 171, 121))
        self.PowPlotHouse1.setObjectName("Plot of Power")
        lay.addWidget(power)
        
        self.PowPlotHouse1.setFocus()
        """

        #####################END of widget

        # Here we set the size of different rows and columnsof the gridlayout
        # QGridLayout.setRowMinimumHeight (self, int row, int minSize)
        # minSize in pixels

        # range(start, end, step)
        for r in range(0, 8, 2):
            for c in range(0, 8, 2):
                layout.setColumnMinimumWidth(c, 50)
            layout.setRowMinimumHeight(r, 50)

        # we set the layout in the main widget called centralwidget
        self.centralwidget.setLayout(layout)
        self.centralwidget.setGeometry(QtCore.QRect(590, 150, 475, 450))
        self.centralwidget.show()

        # This is where the menu lives

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")

        ################Experimental
        # self.menuAbout = QtWidgets.QMenu(self.menubar)
        # self.menuAbout.setObjectName("menuAbout")

        # Experimental #############################
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        ##########experimental 
        # self.menubar.addAction(self.menuAbout.menuAbout())
        ##########Experimental
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SWTDI Outlets Main Window", "SWTDI Outlets Main Window"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        ########Experimetnal
        # self.menuAbout.setTitle(_translate("MainWindow", "About"))
        # Experimental
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))

from OutletsMainPlots import dynPlot1, dynPlot2, dynPlot3, dynPlot4, dynPlot5, dynPlot6, dynPlot7, dynPlot8, dynPlot9, dynPlot10, dynPlot11, dynPlot12

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_outlets()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
