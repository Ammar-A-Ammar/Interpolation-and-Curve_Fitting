import scipy
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import plot
from pyqtgraph import PlotWidget
import numpy as np
from scipy.fftpack import fft
from scipy import interpolate
from math import ceil, inf
from matplotlib.figure import Figure
import pandas as pd
import pyqtgraph as pg
matplotlib.use('Qt5Agg')
from numpy.core.fromnumeric import size
from scipy import signal
#from scipy import make_interp_spline
import math
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class MyThread(QThread):
    change_value = pyqtSignal(int)
    def run(self):
        cnt = 0
        while cnt < 100:
            cnt+=1
            #time.sleep(0.00001)
            self.change_value.emit(cnt)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1301, 1101)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_for_equation_and_error = QtWidgets.QHBoxLayout()
        self.horizontalLayout_for_equation_and_error.setObjectName("horizontalLayout_for_equation_and_error")
        self.gridLayout_for_equation = QtWidgets.QGridLayout()
        self.gridLayout_for_equation.setObjectName("gridLayout_for_equation")
        self.horizontalLayout_for_equation_and_error.addLayout(self.gridLayout_for_equation)
        self.gridLayout_For_error = QtWidgets.QGridLayout()
        self.gridLayout_For_error.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_For_error.setHorizontalSpacing(1)
        self.gridLayout_For_error.setObjectName("gridLayout_For_error")
        self.horizontalLayout_for_equation_and_error.addLayout(self.gridLayout_For_error)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_for_equation_and_error.addWidget(self.comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_for_equation_and_error, 0, 0, 1, 2)
        self.frame_for_main_widget = QtWidgets.QFrame(self.centralwidget)
        self.frame_for_main_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_main_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_main_widget.setObjectName("frame_for_main_widget")
        #self.PlotWidget = QtWidgets.QWidget(self.frame_for_main_widget)
        self.PlotWidget = PlotWidget(self.frame_for_main_widget)
        self.PlotWidget.setGeometry(QtCore.QRect(14, 5, 1221, 451))
        self.PlotWidget.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.PlotWidget.setObjectName("PlotWidget")
        self.gridLayout_2.addWidget(self.frame_for_main_widget, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 501, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.frame_for_errorMap = QtWidgets.QFrame(self.centralwidget)
        self.frame_for_errorMap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_errorMap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_errorMap.setObjectName("frame_for_errorMap")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_for_errorMap)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)

        self.gridLayout_2.addWidget(self.frame_for_errorMap, 2, 0, 1, 1)
        self.verticalLayout_for_seetings = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_seetings.setObjectName("verticalLayout_for_seetings")
        self.gridLayout_for_plot_Settings = QtWidgets.QGridLayout()
        self.gridLayout_for_plot_Settings.setObjectName("gridLayout_for_plot_Settings")
        self.labelOfNumberOfFittingOrder = QtWidgets.QLabel(self.centralwidget)
        self.labelOfNumberOfFittingOrder.setObjectName("labelOfNumberOfFittingOrder")
        self.gridLayout_for_plot_Settings.addWidget(self.labelOfNumberOfFittingOrder, 1, 0, 1, 1)
        self.labelForNumberOfChunks = QtWidgets.QLabel(self.centralwidget)
        self.labelForNumberOfChunks.setObjectName("labelForNumberOfChunks")
        self.gridLayout_for_plot_Settings.addWidget(self.labelForNumberOfChunks, 0, 0, 1, 1)
        self.horizontalSliderFor_chunks = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_chunks.setMinimum(1)
        self.horizontalSliderFor_chunks.setValue(1)
        self.horizontalSliderFor_chunks.setMaximum(10)
        self.horizontalSliderFor_chunks.setPageStep(1)
        self.horizontalSliderFor_chunks.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_chunks.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_chunks.setObjectName("horizontalSliderFor_chunks")
        self.gridLayout_for_plot_Settings.addWidget(self.horizontalSliderFor_chunks, 0, 1, 1, 1)
        self.horizontalSliderFor_FittingOrder = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_FittingOrder.setMaximum(10)
        self.horizontalSliderFor_FittingOrder.setPageStep(1)
        self.horizontalSliderFor_FittingOrder.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_FittingOrder.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_FittingOrder.setObjectName("horizontalSliderFor_FittingOrder")
        self.gridLayout_for_plot_Settings.addWidget(self.horizontalSliderFor_FittingOrder, 1, 1, 1, 1)
        self.horizontalSliderFor_Effeciacy = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_Effeciacy.setMaximum(10)
        self.horizontalSliderFor_Effeciacy.setPageStep(1)
        self.horizontalSliderFor_Effeciacy.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_Effeciacy.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_Effeciacy.setObjectName("horizontalSliderFor_Effeciacy")
        self.gridLayout_for_plot_Settings.addWidget(self.horizontalSliderFor_Effeciacy, 2, 1, 1, 1)
        self.labelForEfficacy = QtWidgets.QLabel(self.centralwidget)
        self.labelForEfficacy.setObjectName("labelForEfficacy")
        self.gridLayout_for_plot_Settings.addWidget(self.labelForEfficacy, 2, 0, 1, 1)
        self.verticalLayout_for_seetings.addLayout(self.gridLayout_for_plot_Settings)
        self.gridLayout_for_ = QtWidgets.QGridLayout()
        self.gridLayout_for_.setObjectName("gridLayout_for_")
        self.lineEdit_For_y_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_For_y_axis.setObjectName("lineEdit_For_y_axis")
        self.gridLayout_for_.addWidget(self.lineEdit_For_y_axis, 2, 3, 1, 1)
        self.label_FitMethodFor_Y_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_FitMethodFor_Y_axis.setObjectName("label_FitMethodFor_Y_axis")
        self.gridLayout_for_.addWidget(self.label_FitMethodFor_Y_axis, 2, 2, 1, 1)
        self.lineEdit_For_x_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_For_x_axis.setObjectName("lineEdit_For_x_axis")
        self.gridLayout_for_.addWidget(self.lineEdit_For_x_axis, 0, 3, 1, 1)
        self.label_Y_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_Y_axis.setObjectName("label_Y_axis")
        self.gridLayout_for_.addWidget(self.label_Y_axis, 2, 0, 1, 1)
        self.label_X_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_X_axis.setObjectName("label_X_axis")
        self.gridLayout_for_.addWidget(self.label_X_axis, 0, 0, 1, 1)
        self.comboBox_Y_axis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Y_axis.setEditable(False)
        self.comboBox_Y_axis.setCurrentText("")
        self.comboBox_Y_axis.setFrame(True)
        self.comboBox_Y_axis.setModelColumn(0)
        self.comboBox_Y_axis.setObjectName("comboBox_Y_axis")
        self.comboBox_Y_axis.addItem("")
        self.comboBox_Y_axis.addItem("")
        self.gridLayout_for_.addWidget(self.comboBox_Y_axis, 2, 1, 1, 1)
        self.label_FitMethodFor_X_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_FitMethodFor_X_axis.setObjectName("label_FitMethodFor_X_axis")
        self.gridLayout_for_.addWidget(self.label_FitMethodFor_X_axis, 0, 2, 1, 1)
        self.comboBox_X_axis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_X_axis.setEditable(False)
        self.comboBox_X_axis.setCurrentText("")
        self.comboBox_X_axis.setObjectName("comboBox_X_axis")
        self.comboBox_X_axis.addItem("")
        self.comboBox_X_axis.addItem("")
        self.gridLayout_for_.addWidget(self.comboBox_X_axis, 0, 1, 1, 1)
        self.label_Z_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.label_Z_axis.setObjectName("label_Z_axis")
        self.gridLayout_for_.addWidget(self.label_Z_axis, 1, 3, 1, 1)
        self.label_for_Z_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_for_Z_axis.setObjectName("label_for_Z_axis")
        self.gridLayout_for_.addWidget(self.label_for_Z_axis, 1, 2, 1, 1)
        self.verticalLayout_for_seetings.addLayout(self.gridLayout_for_)
        self.verticalLayout_for_progressBar = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_progressBar.setObjectName("verticalLayout_for_progressBar")
        self.pushButton_For_GenerateErrorMap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_GenerateErrorMap.setObjectName("pushButton_For_GenerateErrorMap")
        self.verticalLayout_for_progressBar.addWidget(self.pushButton_For_GenerateErrorMap)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_for_progressBar.addWidget(self.progressBar)
        self.verticalLayout_for_seetings.addLayout(self.verticalLayout_for_progressBar)
        self.horizontalLayout_for_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_for_buttons.setObjectName("horizontalLayout_for_buttons")
        self.pushButton_For_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Open.setObjectName("pushButton_For_Open")
        self.horizontalLayout_for_buttons.addWidget(self.pushButton_For_Open)
        self.pushButton_For_Plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Plot.setObjectName("pushButton_For_Plot")
        self.horizontalLayout_for_buttons.addWidget(self.pushButton_For_Plot)
        self.pushButton_For_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Delete.setObjectName("pushButton_For_Delete")
        self.horizontalLayout_for_buttons.addWidget(self.pushButton_For_Delete)
        self.pushButton_For_spare_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_spare_3.setObjectName("pushButton_For_spare_3")
        self.horizontalLayout_for_buttons.addWidget(self.pushButton_For_spare_3)
        self.pushButton_For_spare_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_spare_5.setObjectName("pushButton_For_spare_5")
        self.horizontalLayout_for_buttons.addWidget(self.pushButton_For_spare_5)
        self.comboBox_for_main_plot = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_for_main_plot.setObjectName("comboBox_for_main_plot")
        self.comboBox_for_main_plot.addItem("")
        self.comboBox_for_main_plot.addItem("")
        self.comboBox_for_main_plot.addItem("")
        self.horizontalLayout_for_buttons.addWidget(self.comboBox_for_main_plot)
        self.verticalLayout_for_seetings.addLayout(self.horizontalLayout_for_buttons)
        self.gridLayout_2.addLayout(self.verticalLayout_for_seetings, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1301, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_Y_axis.setCurrentIndex(-1)
        self.comboBox_X_axis.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.comboBox_for_main_plot.currentIndexChanged.connect(lambda:self.ComboboxIndex())
        self.pushButton_For_Open.clicked.connect(self.open_file)
        self.horizontalSliderFor_Effeciacy.valueChanged.connect(lambda: self.extrapolation_change())
        self.horizontalSliderFor_FittingOrder.valueChanged.connect(lambda: self.orderchange())
        self.horizontalSliderFor_chunks.valueChanged.connect(lambda: self.chunk_change())
        self.pushButton_For_GenerateErrorMap.clicked.connect(lambda: self.error_map())
        self.pushButton_For_GenerateErrorMap.clicked.connect(lambda: self.start_progress_bar())
        self.comboBox_X_axis.activated.connect(self.change_text)
        self.comboBox_Y_axis.activated.connect(self.change_text)
        self.comboBox.currentIndexChanged.connect(lambda: self.latex_eqn(self.slider_order_val))

        self.pen_blue = pg.mkPen((0,0,255), width=2, style=QtCore.Qt.DotLine)
        self.pen_green = pg.mkPen((0, 255, 0), width=2, style=QtCore.Qt.DotLine)
        self.pen_red = pg.mkPen((255, 0, 0), width=2, style=QtCore.Qt.DotLine)
        self.chunk_size=1000
        self.slider_order_val = 1
        self.slider_chunk_val = 1
        self.extrapolation_sliderval = 1
        self.extrapolation_pecentage = 100
        self.bool_heatmap = 0

    


        self.fig_error = Figure()
        self.canvas_error = FigureCanvasQTAgg(self.fig_error)
        self.gridLayout_For_error.addWidget(self.canvas_error)
        self.fig_error.clear()
        
        self.progressBar.hide()

        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.gridLayout_for_equation.addWidget(self.canvas, *(0, 1))
        self.fig.clear()
        
        
        
    # def error_map(self):
    #     if self.pushButton_For_GenerateErrorMap.text() != "Generate Error map":
    #         self.progressBar.hide()
    #         self.pushButton_For_GenerateErrorMap.setText("Generate Error map")
    #         if self.bool_heatmap == 1:
    #             self.canvas1.hide()
    #         return
    #     self.pushButton_For_GenerateErrorMap.setText("Cancel")
    #     self.progressBar.show()
    #     comboX = self.comboBox_X_axis.currentIndex()
    #     comboY = self.comboBox_Y_axis.currentIndex()
    #     if self.comboBox_X_axis.currentText() == 'Number of chuncks':
    #         #self.lineEdit_For_x_axis.setObjectName("Text_chuncks")
    #         print('first step')
    #         print(self.lineEdit_For_x_axis.objectName())
    #         # print(self.lineEdit_For_x_axis.displayText())
    #         # print(self.label_FitMethodFor_X_axis.text)
    #         # print(self.label_FitMethodFor_X_axis.text())
            
    #     if self.label_FitMethodFor_X_axis.text() == 'Number of chuncks' and self.lineEdit_For_x_axis.text() == "":
    #         no_chuncks = 5
    #     else:
    #         no_chuncks = int(self.lineEdit_For_x_axis.text())
        
    #     if self.lineEdit_For_x_axis.text() == "":
    #         degree_value = 5
    #     else:
    #         degree_value = int(self.label_Z_axis.text())
        
    #     if self.lineEdit_For_x_axis.text() == "":
    #         overlapping = 0.75
    #         overlaprange = 5
    #     else:
    #         overlapping = 1 - int(self.label_Z_axis.text()) /100
    #         overlaprange = overlapping

    #     chunck_label = list(map(str, range(1, no_chuncks + 1)))
    #     degree_label = list(map(str, range(1, degree_value + 1)))
    #     overlapping_label = [f"{overlapping_index}%" for overlapping_index in range(5, int(overlaprange*5+5), 5)]
    #     overlapping_values, overlap = [], 1
    #     while overlap > overlapping:
    #         overlap -= .05
    #         overlapping_values.append(overlap)
    #     if (comboX == 0 and comboY == 1) or  (comboX == 1 and comboY == 0) :
    #         matrix1 = []
    #         for i in range(1, no_chuncks+1):
    #             matrix1.append([])
    #             for j in range(degree_value):
    #                     X_ErrorMap = self.calculate_chuncks(self.x_axis_data, i, overlapping)
    #                     Y_ErrorMap = self.calculate_chuncks(self.data_amplitude, i, overlapping)
    #                     errors = []
    #                     for k in range(i):
    #                         x_map_val = X_ErrorMap[k]
    #                         y_map_val = Y_ErrorMap[k]
    #                         error_x = self.get_error(x_map_val,y_map_val,j)
    #                         errors.append(error_x)
    #                     matrix1[i-1].append(np.average(errors))

    #         matrix1 = np.array(matrix1)[::-1]
    #         if comboX == 1 and comboY == 0:
    #             matrix1=matrix1.T
    #             fig, self.ax = plt.subplots(figsize=(4, 4))
    #             self.ax = sns.heatmap(matrix1 , xticklabels=chunck_label, yticklabels=degree_label[::-1])
    #         else:
    #             fig, self.ax = plt.subplots(figsize=(4, 4))
    #             self.ax = sns.heatmap(matrix1 , xticklabels=degree_label, yticklabels=chunck_label[::-1])

    #         self.toggle_errormap(fig)

    #     elif (comboX == 0 and comboY == 2) or (comboX == 2 and comboY == 0) :
    #         matrix2=[]
    #         for i in range(degree_value):
    #             matrix2.append([])
    #             for j in range(len(overlapping_values)):
    #                     X_Error_Map = self.calculate_chuncks(self.x_axis_data,no_chuncks,overlapping_values[j])
    #                     Y_Error_Map = self.calculate_chuncks(self.data_amplitude,no_chuncks,overlapping_values[j])
    #                     x1_map_val,y1_map_val= X_Error_Map[0],Y_Error_Map[0]
    #                     x2_map_val,y2_map_val = X_Error_Map[1],Y_Error_Map[1]
    #                     error_x1 = self.get_error(x1_map_val,y1_map_val,i)
    #                     error_x2 = self.get_error(x2_map_val,y2_map_val,i)
    #                     matrix2[i].append((error_x1+error_x2)/2)
    #         matrix2 = np.array(matrix2)[::-1]
    #         if comboX == 2 and comboY == 0:
    #             matrix2=matrix2.T
    #             fig, self.ax = plt.subplots(figsize=(4, 4))
    #             self.ax = sns.heatmap(matrix2 , xticklabels=overlapping_label, yticklabels=degree_label[::-1])
    #         else:
    #             fig, self.ax = plt.subplots(figsize=(1, 4))
    #             self.ax = sns.heatmap(matrix2 , xticklabels=degree_label, yticklabels=overlapping_label[::-1])
    #         self.toggle_errormap(fig)


    #     elif (comboX == 1 and comboY == 2) or  (comboX == 2 and comboY == 1):

    #         matrix3 = []
    #         for i in range(1,no_chuncks+1):
    #             matrix3.append([])
    #             for j in range(len(overlapping_values)):
    #                     X_Error_Map = self.calculate_chuncks(self.x_axis_data, i, overlapping_values[j])
    #                     Y_Error_Map = self.calculate_chuncks(self.data_amplitude, i, overlapping_values[j])
    #                     errors = []
    #                     for k in range(i):
    #                         x_error_val = X_Error_Map[k]
    #                         y_error_val = Y_Error_Map[k]
    #                         error_x = self.get_error(x_error_val,y_error_val,degree_value)
    #                         errors.append(error_x)
    #                     matrix3[i-1].append(np.average(errors))
    #         matrix3 = np.array(matrix3)[::-1]

    #         if (comboX == 2 and comboY == 1):
    #             matrix3 = matrix3.T
    #             fig, self.ax = plt.subplots(figsize=(4, 4))
    #             self.ax = sns.heatmap(matrix3.T, xticklabels=overlapping_label, yticklabels=chunck_label[::-1])
    #         else:
    #             fig, self.ax = plt.subplots(figsize=(4, 4))
    #             self.ax = sns.heatmap(matrix3.T, xticklabels=chunck_label, yticklabels=overlapping_label[::-1])
    #         self.toggle_errormap(fig)
    #     else:
    #         self.progressBar.hide()
    #         print("You can't get The error map between the same values")
    #         self.pushButton_For_GenerateErrorMap.setText("Generate Error map")
    def error_map(self):

        if self.ui.start_button.text() != "Generate error map":
            self.ui.progressBar.hide()
            self.ui.start_button.setText("Generate error map")
            if self.bool_heatmap == 1:
                self.canvas1.hide()
            return

        self.ui.start_button.setText("Cancel")
        self.ui.progressBar.show()

        comboX = self.ui.x_error_map.currentIndex()
        comboY = self.ui.y_error_map.currentIndex()
        if comboX == comboY:
            self.ui.progressBar.hide()
            print("You can't get The error map between the same values")
            self.ui.start_button.setText("Generate error map")
            return

        if self.ui.num_of_chunksLineEdit.text() == "":
            no_chuncks = 5
        else:
            no_chuncks = int(self.ui.num_of_chunksLineEdit.text())

        if self.ui.num_of_chunksLineEdit.text() == "":
            degree_value = 5
        else:
            degree_value = int(self.ui.lineEdit_3.text())

        if self.ui.num_of_chunksLineEdit.text() == "":
            overlapping = 0.75
            overlaprange = 5
        else:
            overlapping = 1 - int(self.ui.overlap_LineEdit.text()) / 100
            overlaprange = overlapping

        chunck_label = list(map(str, range(1, no_chuncks + 1)))
        degree_label = list(map(str, range(1, degree_value + 1)))
        overlapping_label = [f"{overlapping_index}%" for overlapping_index in range(5, int(overlaprange * 5 + 5), 5)]

        overlapping_values, overlap = [], 1
        while overlap > overlapping:
            overlap -= .05
            overlapping_values.append(overlap)

        plotting_options = [no_chuncks + 1,degree_value, overlapping_values] 
        option1 = 0
        option2=1

        matrix1 = []
        for i in range(1, no_chuncks + 1):
                matrix1.append([])
                for j in range(degree_value):
                    X_start_button = self.calculate_chuncks(self.x_axis_data, i, overlapping)
                    Y_start_button = self.calculate_chuncks(self.data_amplitude, i, overlapping)
                    errors = []
                    for k in range(i):
                        x_map_val = X_start_button[k]
                        y_map_val = Y_start_button[k]
                        error_x = self.get_error(x_map_val, y_map_val, j)
                        errors.append(error_x)
                    matrix1[i - 1].append(np.average(errors))

        matrix1 = np.array(matrix1)[::-1]

        if comboX == 1 :
            xticklabels = chunck_label
            matrix1 = matrix1.T
        elif comboX == 2 :
            xticklabels=overlapping_label
            matrix1 = matrix1.T

        elif comboX == 0:
            xticklabels=degree_label
            

        

        if  comboY == 0:
            yticklabels = degree_label[::-1]
            matrix1 = matrix1.T
        elif comboY == 1:
            yticklabels=chunck_label[::-1]
        elif comboY == 2:
            yticklabels=overlapping_label[::-1]
        
        if ((comboX == 2 and comboY == 1) or (comboX == 1 and comboY == 2)):
            matrix1 = matrix1.T

        fig, self.ax = plt.subplots(figsize=(3, 3))
        self.ax = sns.heatmap(matrix1, xticklabels=xticklabels, yticklabels=yticklabels)

        self.toggle_start_button(fig)        
            
    def toggle_errormap (self, fig):
        if self.bool_heatmap == 0:
            self.canvas1 = FigureCanvasQTAgg(fig)
            self.gridLayout.addWidget(self.canvas1)
            self.bool_heatmap = 1
        else:
            self.canvas1.hide()
            self.canvas1 = FigureCanvasQTAgg(fig)
            self.gridLayout.addWidget(self.canvas1)


    def get_error(self,x,y,i):
        # self.coeffs, res, _, _, _ = np.polyfit(t[0:interpol_range], data[0:interpol_range], interpol_order, full=True)
        z_chunk1, res, _, _, _ = np.polyfit(x, y, i, full=True)
        avgerror =math.sqrt(res[0])
            
        return(avgerror)

    def ComboboxIndex(self):
        index = self.comboBox_for_main_plot.currentIndex()
        if index == 0:
            self.interpolate_the_curve(self.slider_order_val)
            
            self.horizontalSliderFor_Effeciacy.show()
            self.horizontalSliderFor_FittingOrder.show()
            self.horizontalSliderFor_chunks.show()
            self.labelForEfficacy.show()
            self.labelForNumberOfChunks.show()
            self.labelOfNumberOfFittingOrder.show()
            
        elif index == 1:
            self.splineInterpolation()
            self.horizontalSliderFor_Effeciacy.hide()
            self.horizontalSliderFor_FittingOrder.hide()
            self.horizontalSliderFor_chunks.hide()
            self.labelForEfficacy.hide()
            self.labelForNumberOfChunks.hide()
            self.labelOfNumberOfFittingOrder.hide()
            
            
            
        elif index==2:
            self.horizontalSliderFor_FittingOrder.setValue(3)
            self.cubicInterpolation()
            self.horizontalSliderFor_Effeciacy.hide()
            self.horizontalSliderFor_FittingOrder.hide()
            self.horizontalSliderFor_chunks.hide()
            self.labelForEfficacy.hide()
            self.labelForNumberOfChunks.hide()
            self.labelOfNumberOfFittingOrder.hide()
            
            

    def extrapolation_change(self):
        self.horizontalSliderFor_chunks.setValue(0)
        self.chunk_size = 1000
        self.slider_chunk_val=1
        self.extrapolation_sliderval = self.horizontalSliderFor_Effeciacy.value()
        val = self.extrapolation_sliderval-1
        self.extrapolation_pecentage = 100-val*5 #100 10
        self.plotting_data(self.slider_order_val)

    def open_file(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open csv', QtCore.QDir.rootPath(), 'csv(*.csv)')
        self.data_set = pd.read_csv(self.fileName, header=None)
        self.data_amplitude = self.data_set[1]
        self.x_axis_data = self.data_set[0]
        self.canvas.draw()
        self.Get_max_freq()
        #self.plotting_data(self.slider_order_val)
        self.ComboboxIndex()

    def Get_max_freq(self):
        data_amp=[]
        n=size(self.data_amplitude)

        for i in self.data_amplitude:
            if len(data_amp)== len(self.x_axis_data):
                break
            else:
                data_amp.append(i)

        frequencies_array=np.arange(1,n/2,dtype ='int')
        data_freq=fft(data_amp)
        freq_mag=(2/n)*abs(data_freq[0:np.size(frequencies_array)])

        imp_freq=freq_mag>0.2
        clean_frequencies_array=imp_freq*frequencies_array
        self.fmax=round(clean_frequencies_array.max())

    def plotting_data(self,order_val):
        if self.fmax == 0:
            self.PlotWidget.clear()
            self.PlotWidget.plot(self.x_axis_data,self.data_amplitude)
        else:
            self.PlotWidget.clear()
            self.PlotWidget.plotItem.vb.setLimits(xMin=min(self.x_axis_data)-0.01, xMax=max(self.x_axis_data),yMin=min(self.data_amplitude) - 0.2, yMax=max(self.data_amplitude) + 0.2)
            self.PlotWidget.plot(self.x_axis_data,self.data_amplitude)
            self.interpolate_the_curve(order_val)

    def interpolate_the_curve(self,interpol_order):
        self.PlotWidget.clear()
        self.PlotWidget.plot(self.x_axis_data,self.data_amplitude)
        self.chunk_coeffs = []
        self.residuals = []
        for i in range(0,len(self.x_axis_data)-1,self.chunk_size):
            data = []
            t = []
            ind = i
            for j in range(self.chunk_size-1):
                if ind < len(self.x_axis_data):
                    data.append(self.data_amplitude[ind])
                    t.append(self.x_axis_data[ind])
                    ind += 1
            extrapolation_fraction = self.extrapolation_pecentage/100 #100
            interpol_range = int(extrapolation_fraction*(self.chunk_size-1))
            self.coeffs,res, _, _, _= np.polyfit(t[0:interpol_range], data[0:interpol_range], interpol_order, full=True)
            if res.size != 0:
                self.residuals.append(res[0])
            self.chunk_coeffs.append(self.coeffs)

            p = np.poly1d(self.coeffs)
            self.PlotWidget.plot(t,p(t),pen = self.pen_blue)

    def splineInterpolation(self):
        self.PlotWidget.clear()
        self.PlotWidget.plot(self.x_axis_data,self.data_amplitude)
        amplitude = self.data_amplitude
        interpolationEquation = scipy.interpolate.make_interp_spline(self.x_axis_data,amplitude)
        time = np.linspace(0,self.x_axis_data.max(),500)
        self.PlotWidget.plot(time,interpolationEquation(time),pen = self.pen_green)

    def cubicInterpolation(self):
        self.PlotWidget.clear()
        self.PlotWidget.plot(self.x_axis_data, self.data_amplitude)
        amplitude = self.data_amplitude
        interpolationEquation = scipy.interpolate.CubicSpline(self.x_axis_data, amplitude)
        time = np.linspace(0, self.x_axis_data.max(), 500)
        self.PlotWidget.plot(time, interpolationEquation(time), pen=self.pen_red)
        

    def interpolate(self,interpol_order,chunk):
        sampling_rate=int(2.5*self.fmax)
        sample_time = 1/sampling_rate
        no_of_samples = int(max(self.x_axis_data)/sample_time)
        for i in range(0,len(self.x_axis_data)-1,chunk):
            data = []
            t = []
            ind = i
            for j in range(chunk-1):
                if ind < len(self.x_axis_data):
                    data.append(self.data_amplitude[ind])
                    t.append(self.x_axis_data[ind])
                    ind += 1
            self.Sample_amp,self.Sample_time = signal.resample(data,no_of_samples,t)
            z = np.polyfit(self.Sample_time, self.Sample_amp, interpol_order)
            p = np.poly1d(z)
            y = p(t)
            return p 

    def orderchange(self):
        self.slider_order_val = int(self.horizontalSliderFor_FittingOrder.value())
        self.plotting_data(self.slider_order_val)
        self.latex_eqn(self.slider_order_val)

    def chunk_change(self):
        self.comboBox.clear()
        self.slider_chunk_val = self.horizontalSliderFor_chunks.value()
        if self.slider_chunk_val != 0:
            self.chunk_size = ceil(1000 / self.slider_chunk_val)
        else:
            self.chunk_size=0
        self.plotting_data(self.slider_order_val)
        for i in range(self.slider_chunk_val):
                self.comboBox.addItem(str(self.slider_chunk_val - i))

    def change_text(self):
        self.label_FitMethodFor_X_axis.setText(self.comboBox_X_axis.currentText())
        self.label_FitMethodFor_Y_axis.setText(self.comboBox_Y_axis.currentText())
        
    def latex_eqn(self, slider_order_val):
        if self.slider_order_val<7 and self.slider_chunk_val<9:
            chunck_no = self.comboBox.currentIndex()
            coeffs = self.chunk_coeffs[chunck_no]
            res = self.residuals[chunck_no]
            eqn = []
            order = slider_order_val
            for i in range(slider_order_val - 1):
                eq1 = '{}\cdot x^{}'.format(ceil(coeffs[i]), order)
                order -= 1
                eqn.append(eq1)
            equation = ''
            for eq in eqn:
                equation = equation + eq + ' + '
            latex_eqn = '$y=' + equation + '{}\cdot x'.format(ceil(coeffs[slider_order_val - 1])) + '+'+'{}\cdot$'.format(
                round(coeffs[slider_order_val],2))
            if len(self.residuals) != 0:
                res = self.residuals[chunck_no]
                error = math.sqrt(res)
                if (error >1):
                    error=1
                error_latex = '$Error = {} \%$ '.format(round(error*100,1))
                
                    
                
                self.fig_error.suptitle(error_latex, x=0.0, y=0.5, horizontalalignment='left', verticalalignment='center')
                #self.gridLayout_For_error.draw()
                self.canvas_error.draw()
            self.fig.suptitle(latex_eqn, x=0.0, y=0.5, horizontalalignment='left', verticalalignment='center')
            self.canvas.draw()
        else:
            self.fig.suptitle('', x=0.0, y=0.5, horizontalalignment='left', verticalalignment='center')
            self.canvas.draw()

    def start_progress_bar(self):
         self.thread = MyThread()
         self.thread.change_value.connect(self.set_progress_val)
         self.thread.start()

    def set_progress_val(self, val):
        
        self.progressBar.setValue(val)
        
    def calculate_chuncks(self,Array_A,no_chunks,overlap_per):
        size = int(1000 / no_chunks)
        step = int(overlap_per * size)
        Array_A = [Array_A[i: i + size] for i in range(0, len(Array_A), step)]
        return Array_A
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelOfNumberOfFittingOrder.setText(_translate("MainWindow", "Fitting order"))
        self.labelForNumberOfChunks.setText(_translate("MainWindow", "Number of Chuncks"))
        self.labelForEfficacy.setText(_translate("MainWindow", "Efficency"))
        self.label_FitMethodFor_Y_axis.setText(_translate("MainWindow", "Fit Mehtod"))
        self.label_Y_axis.setText(_translate("MainWindow", "Y-axis"))
        self.label_X_axis.setText(_translate("MainWindow", "X-axis"))
        self.comboBox_Y_axis.setItemText(0, _translate("MainWindow", "Order of polynomial"))
        self.comboBox_Y_axis.setItemText(1, _translate("MainWindow", "Number of chuncks"))
        self.label_FitMethodFor_X_axis.setText(_translate("MainWindow", "Fit Mehtod"))
        self.comboBox_X_axis.setItemText(0, _translate("MainWindow", "Order of polynomial"))
        self.comboBox_X_axis.setItemText(1, _translate("MainWindow", "Number of chuncks"))
        self.label_for_Z_axis.setText(_translate("MainWindow", "Over Lapping"))
        self.pushButton_For_GenerateErrorMap.setText(_translate("MainWindow", "Generate Error map"))
        self.pushButton_For_Open.setText(_translate("MainWindow", "Open"))
        self.pushButton_For_Plot.setText(_translate("MainWindow", "Plot"))
        self.pushButton_For_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_For_spare_3.setText(_translate("MainWindow", "Spare"))
        self.pushButton_For_spare_5.setText(_translate("MainWindow", "Spare"))
        self.comboBox_for_main_plot.setItemText(0, _translate("MainWindow", "Polynomial"))
        self.comboBox_for_main_plot.setItemText(1, _translate("MainWindow", "Spline"))
        self.comboBox_for_main_plot.setItemText(2, _translate("MainWindow", "Cubic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
