# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1587, 951)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(615, 10, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 425, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(615, 425, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(430, 0, 180, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(1035, 0, 180, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(1035, 415, 180, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(10, 830, 1205, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 415, 180, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(1220, 830, 62, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setAccessibleName("")
        self.doubleSpinBox.setAccessibleDescription("")
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.005)
        self.doubleSpinBox.setProperty("value", 0.02)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1220, 20, 91, 74))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.HipX = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.HipX.setFont(font)
        self.HipX.setObjectName("HipX")
        self.gridLayout.addWidget(self.HipX, 0, 0, 1, 1)
        self.HipY = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.HipY.setFont(font)
        self.HipY.setObjectName("HipY")
        self.gridLayout.addWidget(self.HipY, 1, 0, 1, 1)
        self.Knee = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Knee.setFont(font)
        self.Knee.setObjectName("Knee")
        self.gridLayout.addWidget(self.Knee, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1320, 21, 229, 74))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Angle = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Angle.setFont(font)
        self.Angle.setObjectName("Angle")
        self.gridLayout_2.addWidget(self.Angle, 0, 0, 1, 1)
        self.drive_Temperature = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drive_Temperature.setFont(font)
        self.drive_Temperature.setObjectName("drive_Temperature")
        self.gridLayout_2.addWidget(self.drive_Temperature, 0, 1, 1, 1)
        self.Velocity = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Velocity.setFont(font)
        self.Velocity.setObjectName("Velocity")
        self.gridLayout_2.addWidget(self.Velocity, 1, 0, 1, 1)
        self.motor_Temperature = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.motor_Temperature.setFont(font)
        self.motor_Temperature.setObjectName("motor_Temperature")
        self.gridLayout_2.addWidget(self.motor_Temperature, 1, 1, 1, 1)
        self.Torque = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Torque.setFont(font)
        self.Torque.setObjectName("Torque")
        self.gridLayout_2.addWidget(self.Torque, 2, 0, 1, 1)
        self.drive_Voltage = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drive_Voltage.setFont(font)
        self.drive_Voltage.setObjectName("drive_Voltage")
        self.gridLayout_2.addWidget(self.drive_Voltage, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "data_viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "FL"))
        self.groupBox_2.setTitle(_translate("MainWindow", "FR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "HL"))
        self.groupBox_4.setTitle(_translate("MainWindow", "HR"))
        self.comboBox.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.doubleSpinBox.setToolTip(_translate("MainWindow", "横轴刻度调节"))
        self.HipX.setText(_translate("MainWindow", "HipX"))
        self.HipY.setText(_translate("MainWindow", "HipY"))
        self.Knee.setText(_translate("MainWindow", "Knee"))
        self.Angle.setText(_translate("MainWindow", "Angle"))
        self.drive_Temperature.setText(_translate("MainWindow", "drive_Temperature"))
        self.Velocity.setText(_translate("MainWindow", "Velocity"))
        self.motor_Temperature.setText(_translate("MainWindow", "motor_Temperature"))
        self.Torque.setText(_translate("MainWindow", "Torque"))
        self.drive_Voltage.setText(_translate("MainWindow", "drive_Voltage"))
