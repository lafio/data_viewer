import sys
import numpy as np
from open_file import OpenFile
from dataDisplay import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout,QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar
import index

#在mainwindow绘制曲线并添加到gridlayout
class curve_Display(QMainWindow,Ui_MainWindow):
    def __init__(self,index_dic):
        super().__init__()
        #导入索引字典
        self.index_dic = index_dic
        #初始化UI
        self.setupUi(self)
        #定义四个画板，放于gridLayout
        self.f1 = fig_Canvas()
        self.f2 = fig_Canvas()
        self.f3 = fig_Canvas()
        self.f4 = fig_Canvas()
        NavigationToolbar(self.f1.canvas, self).setGeometry(QtCore.QRect(10, 42, 600, 30))
        NavigationToolbar(self.f2.canvas, self).setGeometry(QtCore.QRect(617, 42, 600, 30))
        NavigationToolbar(self.f3.canvas, self).setGeometry(QtCore.QRect(10, 457, 600, 30))
        NavigationToolbar(self.f4.canvas, self).setGeometry(QtCore.QRect(617, 457, 600, 30))
        self.Layout1 = QGridLayout(self.groupBox)
        self.Layout2 = QGridLayout(self.groupBox_2)
        self.Layout3 = QGridLayout(self.groupBox_3)
        self.Layout4 = QGridLayout(self.groupBox_4)
        #使用索引字典对四个comboBox添加item
        for k,v in index_dic.items():
            self.comboBox.addItem(k)
            self.comboBox_2.addItem(k)
            self.comboBox_3.addItem(k)
            self.comboBox_4.addItem(k)
            self.comboBox.setItemText(v, QtCore.QCoreApplication.translate("MainWindow", k))
            self.comboBox_2.setItemText(v, QtCore.QCoreApplication.translate("MainWindow", k))
            self.comboBox_3.setItemText(v, QtCore.QCoreApplication.translate("MainWindow", k))
            self.comboBox_4.setItemText(v, QtCore.QCoreApplication.translate("MainWindow", k))
        #设定comboBox对应的槽函数：触发display()
        self.comboBox.currentIndexChanged.connect(lambda:self.display(1,0,index_dic[
            self.comboBox.currentText()],self.comboBox.currentText()))
        self.comboBox_2.currentIndexChanged.connect(lambda:self.display(2,0,index_dic[
            self.comboBox_2.currentText()],self.comboBox_2.currentText()))
        self.comboBox_3.currentIndexChanged.connect(lambda:self.display(3,0,index_dic[
            self.comboBox_3.currentText()],self.comboBox_3.currentText()))
        self.comboBox_4.currentIndexChanged.connect(lambda:self.display(4,0,index_dic[
            self.comboBox_4.currentText()],self.comboBox_4.currentText()))
        #设定scrollBar等
        #self.limit = np.array(self.f1.ax.get_xlim() + self.f1.ax.get_ylim())
        self.scroll = self.horizontalScrollBar
        self.step = self.doubleSpinBox.value()
        self.doubleSpinBox.valueChanged.connect(self.getDoubleSpinValue)
        self.spinBox.valueChanged.connect(self.getSpinValue)
        self.get_data_dic()

        # 设定scope绘制策略
        self.scope.valueChanged.connect(lambda: self.draw4Figure(self.scope.value() + 94, self.scope.value() + 95,
                                                                 self.scope.value() + 96, self.scope.value() + 97))
        #16个radioButton设定槽函数
        self.Knee.toggled.connect(self.radioButtonState)
        self.HipX.toggled.connect(self.radioButtonState)
        self.HipY.toggled.connect(self.radioButtonState)
        self.Torque.toggled.connect(self.radioButtonState)
        self.Angle.toggled.connect(self.radioButtonState)
        self.Velocity.toggled.connect(self.radioButtonState)
        self.drive_Temperature.toggled.connect(self.radioButtonState)
        self.drive_Voltage.toggled.connect(self.radioButtonState)
        self.motor_Temperature.toggled.connect(self.radioButtonState)
        self.imu_angle.toggled.connect(self.radioButtonState2)
        self.imu_velocity.toggled.connect(self.radioButtonState2)
        self.imu_acc.toggled.connect(self.radioButtonState2)
        self.cost_time.toggled.connect(lambda:self.draw4Figure(1,1,1,1))
        self.alg_time.toggled.connect(lambda:self.draw4Figure(2,2,2,2))
        self.ecat_time.toggled.connect(lambda:self.draw4Figure(3,4,5,6))
        self.cpu_rate.toggled.connect(lambda:self.draw4Figure(6,6,6,6))
        self.open_btn.clicked.connect(self.get_data_dic)
    #radioButton的槽函数，根据button的不同对应不同的绘图对象
    def radioButtonState(self):
        if self.HipX.isChecked():
            if self.Angle.isChecked():
                self.draw4Figure(22,25,28,31)
            elif self.Velocity.isChecked():
                self.draw4Figure(34,37,40,43)
            elif self.Torque.isChecked():
                self.draw4Figure(46,49,52,55)
            elif self.drive_Temperature.isChecked():
                self.draw4Figure(256,259,262,265)
            elif self.drive_Voltage.isChecked():
                self.draw4Figure(244,247,250,253)
            elif self.motor_Temperature.isChecked():
                self.draw4Figure(269,272,275,278)
        elif self.HipY.isChecked():
            if self.Angle.isChecked():
                self.draw4Figure(23,26,29,32)
            elif self.Velocity.isChecked():
                self.draw4Figure(35,38,41,44)
            elif self.Torque.isChecked():
                self.draw4Figure(47,50,53,56)
            elif self.drive_Temperature.isChecked():
                self.draw4Figure(257,260,263,266)
            elif self.drive_Voltage.isChecked():
                self.draw4Figure(245,248,251,254)
            elif self.motor_Temperature.isChecked():
                self.draw4Figure(270,273,276,279)
        elif self.Knee.isChecked():
            if self.Angle.isChecked():
                self.draw4Figure(24,27,30,33)
            elif self.Velocity.isChecked():
                self.draw4Figure(36,39,42,45)
            elif self.Torque.isChecked():
                self.draw4Figure(48,51,54,57)
            elif self.drive_Temperature.isChecked():
                self.draw4Figure(258,261,264,267)
            elif self.drive_Voltage.isChecked():
                self.draw4Figure(246,249,252,255)
            elif self.motor_Temperature.isChecked():
                self.draw4Figure(271,274,277,280)
    def radioButtonState2(self):
        if self.imu_angle.isChecked():
            self.draw3Figure(8,9,10)
        elif self.imu_velocity.isChecked():
            self.draw3Figure(11,12,13)
        elif self.imu_acc.isChecked():
            self.draw3Figure(14,15,16)
    def getSpinValue(self):
        self.f1.num_limit = self.spinBox.value()
        self.f2.num_limit = self.spinBox.value()
        self.f3.num_limit = self.spinBox.value()
        self.f4.num_limit = self.spinBox.value()
    def getDoubleSpinValue(self):
        self.step=self.doubleSpinBox.value()
    #scrollbar
    def setupSlider(self):
        self.lims = np.array(self.f1.ax.get_xlim())
        print(self.lims)
        self.scroll.setPageStep(self.step * 100)
        self.scroll.actionTriggered.connect(self.update)
        self.update()
    #scroll更新
    def update(self,evt=None):
        r = self.scroll.value() / ((1 + self.step)*100)
        l1 = self.lims[0] + r * np.diff(self.lims)
        l2 = l1 + np.diff(self.lims) * self.step
        self.f1.ax.set_xlim(l1, l2)
        self.f2.ax.set_xlim(l1, l2)
        self.f3.ax.set_xlim(l1, l2)
        self.f4.ax.set_xlim(l1, l2)
        #print(self.scroll.value(), l1, l2)
        self.f1.canvas.draw_idle()
        self.f2.canvas.draw_idle()
        self.f3.canvas.draw_idle()
        self.f4.canvas.draw_idle()
    #改变画板上的图像，暂时弃用
    def changeFigure(self,index):
        index_now = index_dic[index]
        return self.display(1,7,index_now,index)
    #绘制关节数据
    def draw4Figure(self,fl,fr,hl,hr):
        self.comboBox.setCurrentIndex(fl)
        self.comboBox_2.setCurrentIndex(fr)
        self.comboBox_3.setCurrentIndex(hl)
        self.comboBox_4.setCurrentIndex(hr)
        if fl >= 22 and hr <= 57:
            self.comboBox.setCurrentIndex(fl+36)
            self.comboBox_2.setCurrentIndex(fr+36)
            self.comboBox_3.setCurrentIndex(hl+36)
            self.comboBox_4.setCurrentIndex(hr+36)
    #绘制陀螺仪数据
    def draw3Figure(self,x,y,z):
        self.comboBox.setCurrentIndex(x)
        self.comboBox_2.setCurrentIndex(y)
        self.comboBox_3.setCurrentIndex(z)
    #display()，被comboBox作为槽函数调用，以改变画板上的图像
    def display(self,n,para_x,para_y,title):
        f = getattr(self,'f'+str(n))
        f.draw_data(self.data_dic[para_x],self.data_dic[para_y],title)
        f.Layout = getattr(self,'Layout'+str(n))
        if n == 1:
            self.groupBox.setTitle(title)
        else:
            getattr(self,'groupBox_'+str(n)).setTitle(title)
        f.Layout.addWidget(f.canvas)
        print('画板放上去了')
    def get_data_dic(self):
        # 打开数据csv
        filename, filetype = QFileDialog.getOpenFileName()  # 读取文件，将文件路径存储到filename中
        openfile = OpenFile()  # 实例化一个OpenFile，并打开filename
        self.data_dic = openfile.open_file_data(filename)
        #调用进度条类以显示打开文件的进度条

        # 调用一次draw_data以确认ax-limit,同时默认打开4个Knee-Torque
        self.draw4Figure(48, 51, 54, 57)
        self.setupSlider()
#定义画板并构造绘制函数
class fig_Canvas():
    def __init__(self):
        #self.fig = Figure(figsize = (39,27),dpi=100)
        #plt.cla()
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        #self.ax = self.fig.add_axes([0.08, 0.15, 0.9, 0.8])
        self.ax = self.fig.add_subplot(111)
        self.num = 0
        self.num_limit = 2
    # 在画板上画图
    def draw_data(self,x,y,title):
        self.num += 1
        if self.num > self.num_limit:
            self.ax.clear()
            self.num = 1
        self.ax.plot(x,y,label = title)
        #self.ax.scatter(x,y,s=5)
        self.ax.legend(loc = 'upper right')
        self.ax.grid(True)
        self.canvas.draw()
        print('画好了')

#对于给定字典，输入值返回对应的键
def get_key(dic,value):
    return [k for k,v in dic.items() if v == value][0]

if __name__ == '__main__':
    app = QApplication(sys.argv)#实例化一个QApplication
    #openfile = OpenFile()
    #index_dic = openfile.open_file_index()#导入索引，存储到index_dic中
    #openfile.write_index(index_dic) #将index.csv中的索引以字典形式写到index.py中，便于打包程序时不包含index.csv文件
    index_dic = index.get_index_dic()#从index.py中获得索引字典，需要运行一次以上注释掉的三行
    ui = curve_Display(index_dic)#实例化一个curve_Display并运行所有初始化函数
    ui.show()
    sys.exit(app.exec())