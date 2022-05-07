# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeroUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 1096)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.PlotWidget = QtWidgets.QWidget(self.frame)
        self.PlotWidget.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.PlotWidget.setObjectName("PlotWidget")
        self.gridLayout.addWidget(self.PlotWidget, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.ErrorMapWidget = QtWidgets.QWidget(self.frame)
        self.ErrorMapWidget.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.ErrorMapWidget.setObjectName("ErrorMapWidget")
        self.gridLayout.addWidget(self.ErrorMapWidget, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.labelForEquation = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelForEquation.setFont(font)
        self.labelForEquation.setStyleSheet("background-color: rgb(163, 163, 163);\n"
"color: rgb(50, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.labelForEquation.setObjectName("labelForEquation")
        self.gridLayout_4.addWidget(self.labelForEquation, 0, 0, 1, 1)
        self.spinBox_For_ErrorPercenatge = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_For_ErrorPercenatge.setObjectName("spinBox_For_ErrorPercenatge")
        self.gridLayout_4.addWidget(self.spinBox_For_ErrorPercenatge, 0, 3, 1, 1, QtCore.Qt.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(754, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelForNumberOfChunks = QtWidgets.QLabel(self.centralwidget)
        self.labelForNumberOfChunks.setObjectName("labelForNumberOfChunks")
        self.gridLayout_3.addWidget(self.labelForNumberOfChunks, 0, 0, 1, 1)
        self.horizontalSliderFor_chunks = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_chunks.setMaximum(10)
        self.horizontalSliderFor_chunks.setPageStep(1)
        self.horizontalSliderFor_chunks.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_chunks.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_chunks.setObjectName("horizontalSliderFor_chunks")
        self.gridLayout_3.addWidget(self.horizontalSliderFor_chunks, 0, 1, 1, 1)
        self.labelOfNumberOfFittingOrder = QtWidgets.QLabel(self.centralwidget)
        self.labelOfNumberOfFittingOrder.setObjectName("labelOfNumberOfFittingOrder")
        self.gridLayout_3.addWidget(self.labelOfNumberOfFittingOrder, 1, 0, 1, 1)
        self.horizontalSliderFor_FittingOrder = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_FittingOrder.setMaximum(10)
        self.horizontalSliderFor_FittingOrder.setPageStep(1)
        self.horizontalSliderFor_FittingOrder.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_FittingOrder.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_FittingOrder.setObjectName("horizontalSliderFor_FittingOrder")
        self.gridLayout_3.addWidget(self.horizontalSliderFor_FittingOrder, 1, 1, 1, 1)
        self.labelForEfficacy = QtWidgets.QLabel(self.centralwidget)
        self.labelForEfficacy.setObjectName("labelForEfficacy")
        self.gridLayout_3.addWidget(self.labelForEfficacy, 2, 0, 1, 1)
        self.horizontalSliderFor_Effeciacy = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderFor_Effeciacy.setMaximum(10)
        self.horizontalSliderFor_Effeciacy.setPageStep(1)
        self.horizontalSliderFor_Effeciacy.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFor_Effeciacy.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSliderFor_Effeciacy.setObjectName("horizontalSliderFor_Effeciacy")
        self.gridLayout_3.addWidget(self.horizontalSliderFor_Effeciacy, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_X_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_X_axis.setObjectName("label_X_axis")
        self.gridLayout_2.addWidget(self.label_X_axis, 0, 0, 1, 1)
        self.comboBox_X_axis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_X_axis.setEditable(False)
        self.comboBox_X_axis.setCurrentText("")
        self.comboBox_X_axis.setObjectName("comboBox_X_axis")
        self.comboBox_X_axis.addItem("")
        self.comboBox_X_axis.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_X_axis, 0, 1, 1, 1)
        self.label_FitMethodFor_X_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_FitMethodFor_X_axis.setObjectName("label_FitMethodFor_X_axis")
        self.gridLayout_2.addWidget(self.label_FitMethodFor_X_axis, 0, 2, 1, 1)
        self.lineEdit_For_x_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_For_x_axis.setObjectName("lineEdit_For_x_axis")
        self.gridLayout_2.addWidget(self.lineEdit_For_x_axis, 0, 3, 1, 1)
        self.label_Y_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_Y_axis.setObjectName("label_Y_axis")
        self.gridLayout_2.addWidget(self.label_Y_axis, 1, 0, 1, 1)
        self.comboBox_Y_axis = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Y_axis.setEditable(False)
        self.comboBox_Y_axis.setCurrentText("")
        self.comboBox_Y_axis.setFrame(True)
        self.comboBox_Y_axis.setModelColumn(0)
        self.comboBox_Y_axis.setObjectName("comboBox_Y_axis")
        self.comboBox_Y_axis.addItem("")
        self.comboBox_Y_axis.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Y_axis, 1, 1, 1, 1)
        self.label_FitMethodFor_Y_axis = QtWidgets.QLabel(self.centralwidget)
        self.label_FitMethodFor_Y_axis.setObjectName("label_FitMethodFor_Y_axis")
        self.gridLayout_2.addWidget(self.label_FitMethodFor_Y_axis, 1, 2, 1, 1)
        self.lineEdit_For_y_axis = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_For_y_axis.setObjectName("lineEdit_For_y_axis")
        self.gridLayout_2.addWidget(self.lineEdit_For_y_axis, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_For_GenerateErrorMap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_GenerateErrorMap.setObjectName("pushButton_For_GenerateErrorMap")
        self.verticalLayout.addWidget(self.pushButton_For_GenerateErrorMap)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_For_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Open.setObjectName("pushButton_For_Open")
        self.horizontalLayout.addWidget(self.pushButton_For_Open)
        self.pushButton_For_Plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Plot.setObjectName("pushButton_For_Plot")
        self.horizontalLayout.addWidget(self.pushButton_For_Plot)
        self.pushButton_For_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_Delete.setObjectName("pushButton_For_Delete")
        self.horizontalLayout.addWidget(self.pushButton_For_Delete)
        self.pushButton_For_spare_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_spare_3.setObjectName("pushButton_For_spare_3")
        self.horizontalLayout.addWidget(self.pushButton_For_spare_3)
        self.pushButton_For_spare_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_For_spare_5.setObjectName("pushButton_For_spare_5")
        self.horizontalLayout.addWidget(self.pushButton_For_spare_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 1, 1, 3)
        self.labelForErrorPercentage = QtWidgets.QLabel(self.centralwidget)
        self.labelForErrorPercentage.setStyleSheet("background-color: rgb(163, 163, 163);\n"
"color: rgb(50, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.labelForErrorPercentage.setObjectName("labelForErrorPercentage")
        self.gridLayout_4.addWidget(self.labelForErrorPercentage, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_X_axis.setCurrentIndex(-1)
        self.comboBox_Y_axis.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_For_GenerateErrorMap.clicked.connect(lambda: self.error_map())
        #self.pushButton_For_GenerateErrorMap.clicked.connect(lambda: self.start_progress_bar())
        
        self.comboBox_X_axis.activated.connect(self.change_text)
        self.comboBox_Y_axis.activated.connect(self.change_text)
        
    
        

    def change_text(self):
        self.label_FitMethodFor_X_axis.setText(self.comboBox_X_axis.currentText())
        self.label_FitMethodFor_Y_axis.setText(self.comboBox_Y_axis.currentText())
        
        
        
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
        
        
        
        if self.label_FitMethodFor_X_axis.text == 'Number of chuncks':
            self.lineEdit_For_x_axis.setObjectName("Text_chuncks")
            
        




        if self.label_FitMethodFor_X_axis.text() == 'Number of chuncks' and self.Text_chuncks.text() == "":
            no_chuncks = 5
        else:
            no_chuncks = int(self.Text_chuncks.text())
        
        if self.Text_chuncks.text() == "":
            degree_value = 5
        else:
            degree_value = int(self.Text_order.text())
        
        if self.Text_chuncks.text() == "":
            overlapping = 0.75
            overlaprange = 5
        else:
            overlapping = 1 - int(self.Text_overlapping.text()) /100
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
                fig, self.ax = plt.subplots(figsize=(1, 1))
                self.ax = sns.heatmap(matrix1 , xticklabels=chunck_label, yticklabels=degree_label[::-1])
            else:
                fig, self.ax = plt.subplots(figsize=(1, 1))
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
                fig, self.ax = plt.subplots(figsize=(1, 1))
                self.ax = sns.heatmap(matrix2 , xticklabels=overlapping_label, yticklabels=degree_label[::-1])
            else:
                fig, self.ax = plt.subplots(figsize=(1, 1))
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
                fig, self.ax = plt.subplots(figsize=(1, 1))
                self.ax = sns.heatmap(matrix3.T, xticklabels=overlapping_label, yticklabels=chunck_label[::-1])
            else:
                fig, self.ax = plt.subplots(figsize=(1, 1))
                self.ax = sns.heatmap(matrix3.T, xticklabels=chunck_label, yticklabels=overlapping_label[::-1])

            self.toggle_errormap(fig)

        else:
            self.progressBar.hide()
            print("You can't get The error map between the same values")
            self.pushButton_For_GenerateErrorMap.setText("Generate Error map")




        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelForEquation.setText(_translate("MainWindow", "Equation to be here"))
        self.labelForNumberOfChunks.setText(_translate("MainWindow", "Number of Chuncks"))
        self.labelOfNumberOfFittingOrder.setText(_translate("MainWindow", "Fitting order"))
        self.labelForEfficacy.setText(_translate("MainWindow", "Efficency"))
        self.label_X_axis.setText(_translate("MainWindow", "X-axis"))
        self.comboBox_X_axis.setItemText(0, _translate("MainWindow", "Order of polynomial"))
        self.comboBox_X_axis.setItemText(1, _translate("MainWindow", "Number of chuncks"))
        self.label_FitMethodFor_X_axis.setText(_translate("MainWindow", "Fit Mehtod"))
        self.label_Y_axis.setText(_translate("MainWindow", "Y-axis"))
        self.comboBox_Y_axis.setItemText(0, _translate("MainWindow", "Order of polynomial"))
        self.comboBox_Y_axis.setItemText(1, _translate("MainWindow", "Number of chuncks"))
        self.label_FitMethodFor_Y_axis.setText(_translate("MainWindow", "Fit Mehtod"))
        self.pushButton_For_GenerateErrorMap.setText(_translate("MainWindow", "Generate Error map"))
        self.pushButton_For_Open.setText(_translate("MainWindow", "Open"))
        self.pushButton_For_Plot.setText(_translate("MainWindow", "Plot"))
        self.pushButton_For_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_For_spare_3.setText(_translate("MainWindow", "Spare"))
        self.pushButton_For_spare_5.setText(_translate("MainWindow", "Spare"))
        self.labelForErrorPercentage.setText(_translate("MainWindow", "Error Percentage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
