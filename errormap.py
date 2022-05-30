# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:31:28 2022

@author: Enj.Ammar
"""
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

class Window():
    """Main Window."""

    def error_map(self):
            if self.pushButton_For_GenerateErrorMap.text() != "Generate Error map":
                self.progressBar.hide()
                self.pushButton_For_GenerateErrorMap.setText("Generate Error map")
                if self.bool_heatmap == 1:
                    self.canvas1.hide()
                return
            self.pushButton_For_GenerateErrorMap.setText("Cancel")
            self.progressBar.show()
            comboX = self.comboBox_X_axis.currentIndex()
            comboY = self.comboBox_Y_axis.currentIndex()
            if self.comboBox_X_axis.currentText() == 'Number of chuncks':
                #self.lineEdit_For_x_axis.setObjectName("Text_chuncks")
                print('first step')
                print(self.lineEdit_For_x_axis.objectName())
                # print(self.lineEdit_For_x_axis.displayText())
                # print(self.label_FitMethodFor_X_axis.text)
                # print(self.label_FitMethodFor_X_axis.text())
                
            if self.label_FitMethodFor_X_axis.text() == 'Number of chuncks' and self.lineEdit_For_x_axis.text() == "":
                no_chuncks = 5
            else:
                no_chuncks = int(self.lineEdit_For_x_axis.text())
            
            if self.lineEdit_For_x_axis.text() == "":
                degree_value = 5
            else:
                degree_value = int(self.label_Z_axis.text())
            
            if self.lineEdit_For_x_axis.text() == "":
                overlapping = 0.75
                overlaprange = 5
            else:
                overlapping = 1 - int(self.label_Z_axis.text()) /100
                overlaprange = overlapping
    
            chunck_label = list(map(str, range(1, no_chuncks + 1)))
            degree_label = list(map(str, range(1, degree_value + 1)))
            overlapping_label = [f"{overlapping_index}%" for overlapping_index in range(5, int(overlaprange*5+5), 5)]
            overlapping_values, overlap = [], 1
            while overlap > overlapping:
                overlap -= .05
                overlapping_values.append(overlap)
            if (comboX == 0 and comboY == 1) or  (comboX == 1 and comboY == 0) :
                matrix1 = []
                for i in range(1, no_chuncks+1):
                    matrix1.append([])
                    for j in range(degree_value):
                            X_ErrorMap = self.calculate_chuncks(self.x_axis_data, i, overlapping)
                            Y_ErrorMap = self.calculate_chuncks(self.data_amplitude, i, overlapping)
                            errors = []
                            for k in range(i):
                                x_map_val = X_ErrorMap[k]
                                y_map_val = Y_ErrorMap[k]
                                error_x = self.get_error(x_map_val,y_map_val,j)
                                errors.append(error_x)
                            matrix1[i-1].append(np.average(errors))
    
                matrix1 = np.array(matrix1)[::-1]
                if comboX == 1 and comboY == 0:
                    matrix1=matrix1.T
                    fig, self.ax = plt.subplots(figsize=(4, 4))
                    self.ax = sns.heatmap(matrix1 , xticklabels=chunck_label, yticklabels=degree_label[::-1])
                else:
                    fig, self.ax = plt.subplots(figsize=(4, 4))
                    self.ax = sns.heatmap(matrix1 , xticklabels=degree_label, yticklabels=chunck_label[::-1])
    
                self.toggle_errormap(fig)
    
            elif (comboX == 0 and comboY == 2) or (comboX == 2 and comboY == 0) :
                matrix2=[]
                for i in range(degree_value):
                    matrix2.append([])
                    for j in range(len(overlapping_values)):
                            X_Error_Map = self.calculate_chuncks(self.x_axis_data,no_chuncks,overlapping_values[j])
                            Y_Error_Map = self.calculate_chuncks(self.data_amplitude,no_chuncks,overlapping_values[j])
                            x1_map_val,y1_map_val= X_Error_Map[0],Y_Error_Map[0]
                            x2_map_val,y2_map_val = X_Error_Map[1],Y_Error_Map[1]
                            error_x1 = self.get_error(x1_map_val,y1_map_val,i)
                            error_x2 = self.get_error(x2_map_val,y2_map_val,i)
                            matrix2[i].append((error_x1+error_x2)/2)
                matrix2 = np.array(matrix2)[::-1]
                if comboX == 2 and comboY == 0:
                    matrix2=matrix2.T
                    fig, self.ax = plt.subplots(figsize=(4, 4))
                    self.ax = sns.heatmap(matrix2 , xticklabels=overlapping_label, yticklabels=degree_label[::-1])
                else:
                    fig, self.ax = plt.subplots(figsize=(1, 4))
                    self.ax = sns.heatmap(matrix2 , xticklabels=degree_label, yticklabels=overlapping_label[::-1])
                self.toggle_errormap(fig)
    
    
            elif (comboX == 1 and comboY == 2) or  (comboX == 2 and comboY == 1):
    
                matrix3 = []
                for i in range(1,no_chuncks+1):
                    matrix3.append([])
                    for j in range(len(overlapping_values)):
                            X_Error_Map = self.calculate_chuncks(self.x_axis_data, i, overlapping_values[j])
                            Y_Error_Map = self.calculate_chuncks(self.data_amplitude, i, overlapping_values[j])
                            errors = []
                            for k in range(i):
                                x_error_val = X_Error_Map[k]
                                y_error_val = Y_Error_Map[k]
                                error_x = self.get_error(x_error_val,y_error_val,degree_value)
                                errors.append(error_x)
                            matrix3[i-1].append(np.average(errors))
                matrix3 = np.array(matrix3)[::-1]
    
                if (comboX == 2 and comboY == 1):
                    matrix3 = matrix3.T
                    fig, self.ax = plt.subplots(figsize=(4, 4))
                    self.ax = sns.heatmap(matrix3.T, xticklabels=overlapping_label, yticklabels=chunck_label[::-1])
                else:
                    fig, self.ax = plt.subplots(figsize=(4, 4))
                    self.ax = sns.heatmap(matrix3.T, xticklabels=chunck_label, yticklabels=overlapping_label[::-1])
                self.toggle_errormap(fig)
            else:
                self.progressBar.hide()
                print("You can't get The error map between the same values")
                self.pushButton_For_GenerateErrorMap.setText("Generate Error map")