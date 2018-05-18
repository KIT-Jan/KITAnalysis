# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Resources import Logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1001, 571))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.updateButton = QtWidgets.QPushButton(self.tab_1)
        self.updateButton.setGeometry(QtCore.QRect(160, 500, 111, 31))
        self.updateButton.setObjectName("updateButton")
        self.nameBox_tab1 = QtWidgets.QLineEdit(self.tab_1)
        self.nameBox_tab1.setGeometry(QtCore.QRect(10, 70, 121, 20))
        self.nameBox_tab1.setText("")
        self.nameBox_tab1.setObjectName("nameBox_tab1")
        self.pathBox_tab1 = QtWidgets.QLineEdit(self.tab_1)
        self.pathBox_tab1.setGeometry(QtCore.QRect(10, 130, 271, 20))
        self.pathBox_tab1.setText("")
        self.pathBox_tab1.setObjectName("pathBox_tab1")
        self.value_label_2 = QtWidgets.QLabel(self.tab_1)
        self.value_label_2.setGeometry(QtCore.QRect(810, 20, 171, 111))
        self.value_label_2.setObjectName("value_label_2")
        self.results_label = QtWidgets.QLabel(self.tab_1)
        self.results_label.setGeometry(QtCore.QRect(10, 160, 51, 21))
        self.results_label.setObjectName("results_label")
        self.saveButton = QtWidgets.QPushButton(self.tab_1)
        self.saveButton.setGeometry(QtCore.QRect(810, 370, 161, 31))
        self.saveButton.setObjectName("saveButton")
        self.projectTable = QtWidgets.QTableWidget(self.tab_1)
        self.projectTable.setGeometry(QtCore.QRect(810, 190, 161, 161))
        self.projectTable.setMaximumSize(QtCore.QSize(161, 16777215))
        self.projectTable.setObjectName("projectTable")
        self.projectTable.setColumnCount(1)
        self.projectTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.projectTable.setHorizontalHeaderItem(0, item)
        self.headLabel_tab1 = QtWidgets.QLabel(self.tab_1)
        self.headLabel_tab1.setGeometry(QtCore.QRect(10, 0, 181, 21))
        self.headLabel_tab1.setStyleSheet("text-decoration: underline;\n"
"font: 75 10pt \"Verdana\";")
        self.headLabel_tab1.setObjectName("headLabel_tab1")
        self.valueBox_tab1 = QtWidgets.QLineEdit(self.tab_1)
        self.valueBox_tab1.setGeometry(QtCore.QRect(470, 70, 113, 20))
        self.valueBox_tab1.setText("")
        self.valueBox_tab1.setObjectName("valueBox_tab1")
        self.pathLabel_tab1 = QtWidgets.QLabel(self.tab_1)
        self.pathLabel_tab1.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.pathLabel_tab1.setObjectName("pathLabel_tab1")
        self.projectLabel2_tab1 = QtWidgets.QLabel(self.tab_1)
        self.projectLabel2_tab1.setGeometry(QtCore.QRect(470, 100, 121, 21))
        self.projectLabel2_tab1.setObjectName("projectLabel2_tab1")
        self.paraCombo_tab1 = QtWidgets.QComboBox(self.tab_1)
        self.paraCombo_tab1.setGeometry(QtCore.QRect(320, 70, 111, 22))
        self.paraCombo_tab1.setObjectName("paraCombo_tab1")
        self.paraCombo_tab1.addItem("")
        self.paraCombo_tab1.addItem("")
        self.projectBox_tab1 = QtWidgets.QLineEdit(self.tab_1)
        self.projectBox_tab1.setGeometry(QtCore.QRect(470, 130, 121, 20))
        self.projectBox_tab1.setText("")
        self.projectBox_tab1.setObjectName("projectBox_tab1")
        self.resultTab_tab1 = QtWidgets.QTableWidget(self.tab_1)
        self.resultTab_tab1.setGeometry(QtCore.QRect(10, 190, 761, 291))
        self.resultTab_tab1.setMinimumSize(QtCore.QSize(671, 0))
        self.resultTab_tab1.setObjectName("resultTab_tab1")
        self.resultTab_tab1.setRowCount(0)
        self.projectLabel3_tab1 = QtWidgets.QLabel(self.tab_1)
        self.projectLabel3_tab1.setGeometry(QtCore.QRect(810, 160, 91, 21))
        self.projectLabel3_tab1.setObjectName("projectLabel3_tab1")
        self.drawButton = QtWidgets.QPushButton(self.tab_1)
        self.drawButton.setGeometry(QtCore.QRect(810, 450, 161, 31))
        self.drawButton.setObjectName("drawButton")
        self.exportButton = QtWidgets.QPushButton(self.tab_1)
        self.exportButton.setGeometry(QtCore.QRect(10, 500, 111, 31))
        self.exportButton.setObjectName("exportButton")
        self.valueLabel_tab1 = QtWidgets.QLabel(self.tab_1)
        self.valueLabel_tab1.setGeometry(QtCore.QRect(470, 40, 91, 21))
        self.valueLabel_tab1.setObjectName("valueLabel_tab1")
        self.paraLabel_tab1 = QtWidgets.QLabel(self.tab_1)
        self.paraLabel_tab1.setGeometry(QtCore.QRect(320, 40, 91, 21))
        self.paraLabel_tab1.setObjectName("paraLabel_tab1")
        self.nameLabel_tab1 = QtWidgets.QLabel(self.tab_1)
        self.nameLabel_tab1.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.nameLabel_tab1.setObjectName("nameLabel_tab1")
        self.clearButton = QtWidgets.QPushButton(self.tab_1)
        self.clearButton.setGeometry(QtCore.QRect(810, 410, 161, 31))
        self.clearButton.setObjectName("clearButton")
        self.addButton = QtWidgets.QPushButton(self.tab_1)
        self.addButton.setGeometry(QtCore.QRect(310, 500, 111, 31))
        self.addButton.setObjectName("addButton")
        self.startButton = QtWidgets.QPushButton(self.tab_1)
        self.startButton.setGeometry(QtCore.QRect(660, 40, 111, 111))
        self.startButton.setObjectName("startButton")
        self.projectCombo_tab1 = QtWidgets.QComboBox(self.tab_1)
        self.projectCombo_tab1.setGeometry(QtCore.QRect(170, 70, 111, 22))
        self.projectCombo_tab1.setObjectName("projectCombo_tab1")
        self.projectCombo_tab1.addItem("")
        self.projectCombo_tab1.addItem("")
        self.projectCombo_tab1.addItem("")
        self.projectCombo_tab1.addItem("")
        self.projectCombo_tab1.addItem("")
        self.projectCombo_tab1.addItem("")
        self.projecLabel1_tab1 = QtWidgets.QLabel(self.tab_1)
        self.projecLabel1_tab1.setGeometry(QtCore.QRect(170, 40, 91, 21))
        self.projecLabel1_tab1.setObjectName("projecLabel1_tab1")
        self.tabWidget.addTab(self.tab_1, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.exportButton_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.exportButton_tab2.setGeometry(QtCore.QRect(840, 440, 131, 91))
        self.exportButton_tab2.setObjectName("exportButton_tab2")
        self.pathBox_tab2 = QtWidgets.QLineEdit(self.tab_2)
        self.pathBox_tab2.setGeometry(QtCore.QRect(10, 130, 271, 20))
        self.pathBox_tab2.setText("")
        self.pathBox_tab2.setObjectName("pathBox_tab2")
        self.resultTab_tab2 = QtWidgets.QTableWidget(self.tab_2)
        self.resultTab_tab2.setGeometry(QtCore.QRect(10, 190, 961, 201))
        self.resultTab_tab2.setMinimumSize(QtCore.QSize(671, 0))
        self.resultTab_tab2.setObjectName("resultTab_tab2")
        self.resultTab_tab2.setRowCount(0)
        self.resultsLabel_tab2 = QtWidgets.QLabel(self.tab_2)
        self.resultsLabel_tab2.setGeometry(QtCore.QRect(10, 160, 51, 21))
        self.resultsLabel_tab2.setObjectName("resultsLabel_tab2")
        self.head_label_tab2 = QtWidgets.QLabel(self.tab_2)
        self.head_label_tab2.setGeometry(QtCore.QRect(10, 0, 181, 21))
        self.head_label_tab2.setStyleSheet("text-decoration: underline;\n"
"font: 75 10pt \"Verdana\";")
        self.head_label_tab2.setObjectName("head_label_tab2")
        self.updateButton_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.updateButton_tab2.setGeometry(QtCore.QRect(700, 440, 131, 41))
        self.updateButton_tab2.setObjectName("updateButton_tab2")
        self.value_label_tab2 = QtWidgets.QLabel(self.tab_2)
        self.value_label_tab2.setGeometry(QtCore.QRect(810, 20, 171, 111))
        self.value_label_tab2.setObjectName("value_label_tab2")
        self.pathLabel_tab2 = QtWidgets.QLabel(self.tab_2)
        self.pathLabel_tab2.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.pathLabel_tab2.setObjectName("pathLabel_tab2")
        self.nameLabel_tab2 = QtWidgets.QLabel(self.tab_2)
        self.nameLabel_tab2.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.nameLabel_tab2.setObjectName("nameLabel_tab2")
        self.clearButton_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.clearButton_tab2.setGeometry(QtCore.QRect(700, 490, 131, 41))
        self.clearButton_tab2.setObjectName("clearButton_tab2")
        self.nameBox_tab2 = QtWidgets.QLineEdit(self.tab_2)
        self.nameBox_tab2.setGeometry(QtCore.QRect(10, 70, 121, 20))
        self.nameBox_tab2.setText("")
        self.nameBox_tab2.setObjectName("nameBox_tab2")
        self.limitsLabel_tab2 = QtWidgets.QLabel(self.tab_2)
        self.limitsLabel_tab2.setGeometry(QtCore.QRect(320, 40, 81, 21))
        self.limitsLabel_tab2.setObjectName("limitsLabel_tab2")
        self.startButton_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.startButton_tab2.setGeometry(QtCore.QRect(660, 40, 111, 111))
        self.startButton_tab2.setObjectName("startButton_tab2")
        self.limitLabel_tab2 = QtWidgets.QLabel(self.tab_2)
        self.limitLabel_tab2.setGeometry(QtCore.QRect(10, 410, 51, 21))
        self.limitLabel_tab2.setObjectName("limitLabel_tab2")
        self.limitTable = QtWidgets.QTableWidget(self.tab_2)
        self.limitTable.setGeometry(QtCore.QRect(10, 440, 681, 91))
        self.limitTable.setObjectName("limitTable")
        self.limitTable.setColumnCount(6)
        self.limitTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.limitTable.setHorizontalHeaderItem(6, item)
        self.paraCombo_tab2 = QtWidgets.QComboBox(self.tab_2)
        self.paraCombo_tab2.setGeometry(QtCore.QRect(320, 70, 111, 22))
        self.paraCombo_tab2.setObjectName("paraCombo_tab2")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.paraCombo_tab2.addItem("")
        self.projectCombo_tab2 = QtWidgets.QComboBox(self.tab_2)
        self.projectCombo_tab2.setGeometry(QtCore.QRect(170, 70, 111, 22))
        self.projectCombo_tab2.setObjectName("projectCombo_tab2")
        self.projectCombo_tab2.addItem("")
        self.projectCombo_tab2.addItem("")
        self.projectCombo_tab2.addItem("")
        self.projectCombo_tab2.addItem("")
        self.projectCombo_tab2.addItem("")
        self.projectCombo_tab2.addItem("")
        self.projectLabel_tab2 = QtWidgets.QLabel(self.tab_2)
        self.projectLabel_tab2.setGeometry(QtCore.QRect(170, 40, 81, 21))
        self.projectLabel_tab2.setObjectName("projectLabel_tab2")
        self.tabWidget.addTab(self.tab_2, "")
        self.para_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.para_label_2.setGeometry(QtCore.QRect(860, 570, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.para_label_2.setFont(font)
        self.para_label_2.setObjectName("para_label_2")


        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.nameBox_tab3 = QtWidgets.QLineEdit(self.tab_3)
        self.nameBox_tab3.setGeometry(QtCore.QRect(10, 70, 121, 20))
        self.nameBox_tab3.setText("")
        self.nameBox_tab3.setObjectName("nameBox_tab3")
        self.pathBox_tab3 = QtWidgets.QLineEdit(self.tab_3)
        self.pathBox_tab3.setGeometry(QtCore.QRect(10, 130, 271, 20))
        self.pathBox_tab3.setText("")
        self.pathBox_tab3.setObjectName("pathBox_tab1")
        self.value_label_3 = QtWidgets.QLabel(self.tab_3)
        self.value_label_3.setGeometry(QtCore.QRect(810, 20, 171, 111))
        self.value_label_3.setObjectName("value_label_3")
        self.results_label_3 = QtWidgets.QLabel(self.tab_3)
        self.results_label_3.setGeometry(QtCore.QRect(10, 160, 51, 21))
        self.results_label_3.setObjectName("results_label_3")
        self.projectTable_3 = QtWidgets.QTableWidget(self.tab_3)
        self.projectTable_3.setGeometry(QtCore.QRect(810, 190, 161, 161))
        self.projectTable_3.setMaximumSize(QtCore.QSize(161, 16777215))
        self.projectTable_3.setObjectName("projectTable_3")
        self.projectTable_3.setColumnCount(1)
        self.projectTable_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.projectTable_3.setHorizontalHeaderItem(0, item)
        self.headLabel_tab3 = QtWidgets.QLabel(self.tab_3)
        self.headLabel_tab3.setGeometry(QtCore.QRect(10, 0, 181, 21))
        self.headLabel_tab3.setStyleSheet("text-decoration: underline;\n"
"font: 75 10pt \"Verdana\";")
        self.headLabel_tab3.setObjectName("headLabel_tab3")
        self.valueBox_tab3 = QtWidgets.QLineEdit(self.tab_3)
        self.valueBox_tab3.setGeometry(QtCore.QRect(470, 70, 113, 20))
        self.valueBox_tab3.setText("")
        self.valueBox_tab3.setObjectName("valueBox_tab3")
        self.pathLabel_tab3 = QtWidgets.QLabel(self.tab_3)
        self.pathLabel_tab3.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.pathLabel_tab3.setObjectName("pathLabel_tab3")
        self.projectLabel2_tab3 = QtWidgets.QLabel(self.tab_3)
        self.projectLabel2_tab3.setGeometry(QtCore.QRect(470, 100, 121, 21))
        self.projectLabel2_tab3.setObjectName("projectLabel2_tab3")
        self.projectBox_tab3 = QtWidgets.QLineEdit(self.tab_3)
        self.projectBox_tab3.setGeometry(QtCore.QRect(470, 130, 121, 20))
        self.projectBox_tab3.setText("")
        self.projectBox_tab3.setObjectName("projectBox_tab3")
        self.resultTab_tab3 = QtWidgets.QTableWidget(self.tab_3)
        self.resultTab_tab3.setGeometry(QtCore.QRect(10, 190, 761, 291))
        self.resultTab_tab3.setMinimumSize(QtCore.QSize(671, 0))
        self.resultTab_tab3.setObjectName("resultTab_tab3")
        self.resultTab_tab3.setRowCount(0)
        self.projectLabel3_tab3 = QtWidgets.QLabel(self.tab_1)
        self.projectLabel3_tab3.setGeometry(QtCore.QRect(810, 160, 91, 21))
        self.projectLabel3_tab3.setObjectName("projectLabel3_tab3")
        self.exportButton = QtWidgets.QPushButton(self.tab_1)
        self.exportButton.setGeometry(QtCore.QRect(10, 500, 111, 31))
        self.exportButton.setObjectName("exportButton")
        self.valueLabel_tab3 = QtWidgets.QLabel(self.tab_3)
        self.valueLabel_tab3.setGeometry(QtCore.QRect(470, 40, 91, 21))
        self.valueLabel_tab3.setObjectName("valueLabel_tab3")
        self.paraLabel_tab3 = QtWidgets.QLabel(self.tab_3)
        self.paraLabel_tab3.setGeometry(QtCore.QRect(320, 40, 91, 21))
        self.paraLabel_tab3.setObjectName("paraLabel_tab3")
        self.nameLabel_tab3 = QtWidgets.QLabel(self.tab_3)
        self.nameLabel_tab3.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.nameLabel_tab3.setObjectName("nameLabel_tab3")
        self.clearButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.clearButton_3.setGeometry(QtCore.QRect(810, 410, 161, 31))
        self.clearButton_3.setObjectName("clearButton_3")
        self.addButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.addButton_3.setGeometry(QtCore.QRect(310, 500, 111, 31))
        self.addButton_3.setObjectName("addButton_3")
        self.startButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.startButton_3.setGeometry(QtCore.QRect(660, 40, 111, 111))
        self.startButton_3.setObjectName("startButton")
        self.projectCombo_tab3 = QtWidgets.QComboBox(self.tab_3)
        self.projectCombo_tab3.setGeometry(QtCore.QRect(170, 70, 111, 22))
        self.projectCombo_tab3.setObjectName("projectCombo_tab3")
        self.projectCombo_tab3.addItem("")
        self.projectCombo_tab3.addItem("")
        self.projectCombo_tab3.addItem("")
        self.projectCombo_tab3.addItem("")
        self.projectCombo_tab3.addItem("")
        self.projectCombo_tab3.addItem("")
        self.projecLabel1_tab3 = QtWidgets.QLabel(self.tab_3)
        self.projecLabel1_tab3.setGeometry(QtCore.QRect(170, 40, 91, 21))
        self.projecLabel1_tab3.setObjectName("projecLabel1_tab3")
        self.tabWidget.addTab(self.tab_3, "")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.updateButton.setText(_translate("MainWindow", "Update Table"))
        self.value_label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/KIT.png\"/></p></body></html>"))
        self.results_label.setText(_translate("MainWindow", "Results"))
        self.saveButton.setText(_translate("MainWindow", "Save Project"))
        item = self.projectTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Project Item"))
        self.headLabel_tab1.setText(_translate("MainWindow", "ALiBaVa Search Tool"))
        self.pathLabel_tab1.setText(_translate("MainWindow", "Output path"))
        self.projectLabel2_tab1.setText(_translate("MainWindow", "Project Name"))
        self.paraCombo_tab1.setItemText(0, _translate("MainWindow", "Voltage"))
        self.paraCombo_tab1.setItemText(1, _translate("MainWindow", "Annealing"))
        self.projectLabel3_tab1.setText(_translate("MainWindow", "Current Project"))
        self.drawButton.setText(_translate("MainWindow", "Draw Project"))
        self.exportButton.setText(_translate("MainWindow", "Export to File"))
        self.valueLabel_tab1.setText(_translate("MainWindow", "Parameter Value"))
        self.paraLabel_tab1.setText(_translate("MainWindow", "Search Parameter"))
        self.nameLabel_tab1.setText(_translate("MainWindow", "Sensor Name"))
        self.clearButton.setText(_translate("MainWindow", "Clear Project"))
        self.addButton.setText(_translate("MainWindow", ">> Add to Project"))
        self.startButton.setText(_translate("MainWindow", "Start Search"))
        self.projectCombo_tab1.setItemText(0, _translate("MainWindow", "HPK_2S_I"))
        self.projectCombo_tab1.setItemText(1, _translate("MainWindow", "HPK_2S_II"))
        self.projectCombo_tab1.setItemText(2, _translate("MainWindow", "CEC BabyStd"))
        self.projectCombo_tab1.setItemText(3, _translate("MainWindow", "CEC Badd"))
        self.projectCombo_tab1.setItemText(4, _translate("MainWindow", "CEC Bstd"))
        self.projectCombo_tab1.setItemText(5, _translate("MainWindow", "CEC BPA"))
        self.projecLabel1_tab1.setText(_translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "ALiBaVa Search Tool"))

        self.exportButton_tab2.setText(_translate("MainWindow", "Export"))
        self.resultsLabel_tab2.setText(_translate("MainWindow", "Results"))
        self.head_label_tab2.setText(_translate("MainWindow", "Strip Mean Calculator"))
        self.updateButton_tab2.setText(_translate("MainWindow", "Update"))
        self.value_label_tab2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/KIT.png\"/></p></body></html>"))
        self.pathLabel_tab2.setText(_translate("MainWindow", "Output path"))
        self.nameLabel_tab2.setText(_translate("MainWindow", "Sensor Name"))
        self.clearButton_tab2.setText(_translate("MainWindow", "Clear"))
        self.limitsLabel_tab2.setText(_translate("MainWindow", "Strip Parameter"))
        self.startButton_tab2.setText(_translate("MainWindow", "Start Search"))
        self.limitLabel_tab2.setText(_translate("MainWindow", "Limits"))
        item = self.limitTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lower Limit"))
        item = self.limitTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upper Limit"))
        item = self.limitTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "R_int"))
        item = self.limitTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "R_poly_dc"))
        item = self.limitTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "I_leak_dc"))
        item = self.limitTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Pinhole"))
        item = self.limitTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CC"))
        item = self.limitTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "C_int"))
        self.paraCombo_tab2.setItemText(0, _translate("MainWindow", "*"))
        self.paraCombo_tab2.setItemText(1, _translate("MainWindow", "R_int"))
        self.paraCombo_tab2.setItemText(2, _translate("MainWindow", "R_poly_dc"))
        self.paraCombo_tab2.setItemText(3, _translate("MainWindow", "I_leak_dc"))
        self.paraCombo_tab2.setItemText(4, _translate("MainWindow", "Pinhole"))
        self.paraCombo_tab2.setItemText(5, _translate("MainWindow", "CC"))
        self.paraCombo_tab2.setItemText(6, _translate("MainWindow", "C_int"))
        self.paraCombo_tab2.setItemText(7, _translate("MainWindow", "R_int_Ramp"))
        self.paraCombo_tab2.setItemText(8, _translate("MainWindow", "C_int_Ramp"))
        self.projectCombo_tab2.setItemText(0, _translate("MainWindow", "HPK_2S_I"))
        self.projectCombo_tab2.setItemText(1, _translate("MainWindow", "HPK_2S_II"))
        self.projectCombo_tab2.setItemText(2, _translate("MainWindow", "CEC BabyStd"))
        self.projectCombo_tab2.setItemText(3, _translate("MainWindow", "CEC Bstd"))
        self.projectCombo_tab2.setItemText(4, _translate("MainWindow", "CEC Badd"))
        self.projectCombo_tab2.setItemText(5, _translate("MainWindow", "CEC BPA"))
        self.projectLabel_tab2.setText(_translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Strip Mean Calculator"))
        self.para_label_2.setText(_translate("MainWindow", "Created by Marius Metzler"))

        self.results_label_3.setText(_translate("MainWindow", "Results"))
        item = self.projectTable_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Project Item_3"))
        self.headLabel_tab3.setText(_translate("MainWindow", "ALiBaVa Search Tool"))
        self.pathLabel_tab3.setText(_translate("MainWindow", "Output path"))
        self.projectLabel2_tab3.setText(_translate("MainWindow", "Project Name"))
        self.projectLabel3_tab3.setText(_translate("MainWindow", "Current Project"))
        self.valueLabel_tab3.setText(_translate("MainWindow", "Parameter Value"))
        self.paraLabel_tab3.setText(_translate("MainWindow", "Search Parameter"))
        self.nameLabel_tab3.setText(_translate("MainWindow", "Sensor Name"))
        self.clearButton_3.setText(_translate("MainWindow", "Clear Project"))
        self.addButton_3.setText(_translate("MainWindow", ">> Add to Project"))
        self.startButton_3.setText(_translate("MainWindow", "Start Search"))
        self.projectCombo_tab3.setItemText(0, _translate("MainWindow", "HPK_2S_I"))
        self.projectCombo_tab3.setItemText(1, _translate("MainWindow", "HPK_2S_II"))
        self.projectCombo_tab3.setItemText(2, _translate("MainWindow", "CEC BabyStd"))
        self.projectCombo_tab3.setItemText(3, _translate("MainWindow", "CEC Badd"))
        self.projectCombo_tab3.setItemText(4, _translate("MainWindow", "CEC Bstd"))
        self.projectCombo_tab3.setItemText(5, _translate("MainWindow", "CEC BPA"))
        self.projecLabel1_tab3.setText(_translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Alpha Calculator"))
