# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1546, 931)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(615, 10, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 425, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(615, 425, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(430, 12, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(1035, 12, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(1035, 427, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setAutoFillBackground(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 427, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAutoFillBackground(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1220, 90, 91, 92))
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
        self.HipX = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.HipX.setFont(font)
        self.HipX.setObjectName("HipX")
        self.gridLayout.addWidget(self.HipX, 0, 0, 1, 1)
        self.HipY = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HipY.setFont(font)
        self.HipY.setObjectName("HipY")
        self.gridLayout.addWidget(self.HipY, 1, 0, 1, 1)
        self.Knee = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Knee.setFont(font)
        self.Knee.setObjectName("Knee")
        self.gridLayout.addWidget(self.Knee, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1320, 90, 265, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.motor_Temperature = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.motor_Temperature.setFont(font)
        self.motor_Temperature.setObjectName("motor_Temperature")
        self.gridLayout_2.addWidget(self.motor_Temperature, 1, 1, 1, 1)
        self.drive_Voltage = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.drive_Voltage.setFont(font)
        self.drive_Voltage.setObjectName("drive_Voltage")
        self.gridLayout_2.addWidget(self.drive_Voltage, 2, 1, 1, 1)
        self.Angle = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Angle.setFont(font)
        self.Angle.setObjectName("Angle")
        self.gridLayout_2.addWidget(self.Angle, 0, 0, 1, 1)
        self.drive_Temperature = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.drive_Temperature.setFont(font)
        self.drive_Temperature.setObjectName("drive_Temperature")
        self.gridLayout_2.addWidget(self.drive_Temperature, 0, 1, 1, 1)
        self.Torque = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Torque.setFont(font)
        self.Torque.setObjectName("Torque")
        self.gridLayout_2.addWidget(self.Torque, 2, 0, 1, 1)
        self.Velocity = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Velocity.setFont(font)
        self.Velocity.setObjectName("Velocity")
        self.gridLayout_2.addWidget(self.Velocity, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1220, 250, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1240, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1240, 270, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(1227, 310, 361, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.imu_angle = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.imu_angle.setFont(font)
        self.imu_angle.setObjectName("imu_angle")
        self.imu_velocity = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.imu_velocity.setFont(font)
        self.imu_velocity.setObjectName("imu_velocity")
        self.imu_acc = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.imu_acc.setFont(font)
        self.imu_acc.setObjectName("imu_acc")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(1240, 750, 200, 52))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(8)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1220, 360, 361, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1240, 380, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1220, 500, 361, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1240, 520, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1220, 590, 361, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1240, 620, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setGeometry(QtCore.QRect(1240, 660, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.open_btn.setFont(font)
        self.open_btn.setObjectName("open_btn")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(1240, 560, 151, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.scope = QtWidgets.QSpinBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.scope.setFont(font)
        self.scope.setMaximum(146)
        self.scope.setObjectName("scope")
        self.horizontalLayout.addWidget(self.scope)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(1230, 410, 311, 91))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cost_time = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cost_time.setFont(font)
        self.cost_time.setObjectName("cost_time")
        self.gridLayout_3.addWidget(self.cost_time, 0, 0, 1, 1)
        self.alg_time = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.alg_time.setFont(font)
        self.alg_time.setObjectName("alg_time")
        self.gridLayout_3.addWidget(self.alg_time, 0, 1, 1, 1)
        self.ecat_time = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ecat_time.setFont(font)
        self.ecat_time.setObjectName("ecat_time")
        self.gridLayout_3.addWidget(self.ecat_time, 1, 0, 1, 1)
        self.cpu_rate = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cpu_rate.setFont(font)
        self.cpu_rate.setObjectName("cpu_rate")
        self.gridLayout_3.addWidget(self.cpu_rate, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(1220, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 830, 1161, 22))
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(9, 860, 1161, 22))
        self.horizontalSlider_2.setProperty("value", 5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1180, 830, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1180, 860, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1250, 835, 78, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1250, 862, 121, 16))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.label_4.setNum)
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_9.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据查看器@deeprobotics.cn"))
        self.groupBox.setTitle(_translate("MainWindow", "FL"))
        self.groupBox_2.setTitle(_translate("MainWindow", "FR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "HL"))
        self.groupBox_4.setTitle(_translate("MainWindow", "HR"))
        self.comboBox.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "IN_FL_HipX_Ang (rad)"))
        self.HipX.setText(_translate("MainWindow", "HipX"))
        self.HipY.setText(_translate("MainWindow", "HipY"))
        self.Knee.setText(_translate("MainWindow", "Knee"))
        self.motor_Temperature.setText(_translate("MainWindow", "motor_Temperature"))
        self.drive_Voltage.setText(_translate("MainWindow", "drive_Voltage"))
        self.Angle.setText(_translate("MainWindow", "Angle"))
        self.drive_Temperature.setText(_translate("MainWindow", "drive_Temperature"))
        self.Torque.setText(_translate("MainWindow", "Torque"))
        self.Velocity.setText(_translate("MainWindow", "Velocity"))
        self.label.setText(_translate("MainWindow", "关节"))
        self.label_2.setText(_translate("MainWindow", "姿态"))
        self.imu_angle.setText(_translate("MainWindow", "Angle"))
        self.imu_velocity.setText(_translate("MainWindow", "Velocity"))
        self.imu_acc.setText(_translate("MainWindow", "Acceleration"))
        self.label_3.setText(_translate("MainWindow", "最大曲线个数"))
        self.spinBox.setToolTip(_translate("MainWindow", "1~8"))
        self.label_5.setText(_translate("MainWindow", "系统"))
        self.label_6.setText(_translate("MainWindow", "算法"))
        self.label_8.setText(_translate("MainWindow", "设置"))
        self.open_btn.setText(_translate("MainWindow", "打开"))
        self.label_7.setText(_translate("MainWindow", "scope"))
        self.scope.setToolTip(_translate("MainWindow", "0-146"))
        self.cost_time.setText(_translate("MainWindow", "cost_time"))
        self.alg_time.setText(_translate("MainWindow", "alg_cycle_time"))
        self.ecat_time.setText(_translate("MainWindow", "Ecat_time"))
        self.cpu_rate.setText(_translate("MainWindow", "CPU_rate"))
        self.checkBox.setText(_translate("MainWindow", "期望曲线"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "S（当前位置）"))
        self.label_11.setText(_translate("MainWindow", "S（横轴长度：1-20s）"))
