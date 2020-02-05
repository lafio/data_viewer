import sys,csv
import numpy as np
from dataDisplay import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout,QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

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
        self.comboBox.currentIndexChanged.connect(lambda:self.display(1,7,index_dic[
            self.comboBox.currentText()],self.comboBox.currentText()))
        self.comboBox_2.currentIndexChanged.connect(lambda:self.display(2,7,index_dic[
            self.comboBox_2.currentText()],self.comboBox_2.currentText()))
        self.comboBox_3.currentIndexChanged.connect(lambda: self.display(3, 7, index_dic[
            self.comboBox_3.currentText()], self.comboBox_3.currentText()))
        self.comboBox_4.currentIndexChanged.connect(lambda: self.display(4, 7, index_dic[
            self.comboBox_4.currentText()], self.comboBox_4.currentText()))
        #调用一次draw_data以确认ax-limit
        self.f1.draw_data(7,8)
        self.limit = np.array(self.f1.ax.get_xlim()+self.f1.ax.get_ylim())
        #设定scrollBar
        self.scroll = self.horizontalScrollBar
        self.step = 0.1
        self.setupSlider()
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
    #绘制关节数据，暂时弃用
    def draw_joint_data(self,index):
        title = self.comboBox.currentText()
        for i in range(1,5):
            self.display(i,7,index+3*(i-1),title)
    #display()，被comboBox作为槽函数调用，以改变画板上的图像
    def display(self,n,para_x,para_y,title):
        f = getattr(self,'f'+str(n))
        f.draw_data(para_x,para_y)
        f.Layout = getattr(self,'Layout'+str(n))
        if n == 1:
            self.groupBox.setTitle(title)
        else:
            getattr(self,'groupBox_'+str(n)).setTitle(title)
        f.Layout.addWidget(f.canvas)
        print('画板放上去了')
#定义画板并构造绘制函数
class fig_Canvas():
    def __init__(self):
        #self.fig = Figure(figsize = (39,27),dpi=100)
        #plt.cla()
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_axes([0.08, 0.15, 0.9, 0.8])
    # 在画板上画图
    def draw_data(self,para_x,para_y):
        self.ax.clear()
        x = globals()['para'+str(para_x)]
        y = globals()['para'+str(para_y)]
        self.ax.plot(x,y)
        self.ax.grid(True)
        self.canvas.draw()
        print('画好了')
#定义打开csv文件的类
class OpenFile():
    def __init__(self,filename):
        self.open_file_data(filename)
    # 读取index.csv 文件，获得data的索引
    def open_file_index(self):
        with open('index.csv') as f:
            reader = csv.reader(f)
            index_dic = {},
            dic_key,dic_value = [],[]
            for row in reader:
                dic_key.append(row[2])
                dic_value.append(int(row[0].strip()))
            index_dic = dict(zip(dic_key,dic_value))
        return index_dic
    # 读取csv_data文件，append到285个作为全局变量的list
    def open_file_data(self,filename):
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for i in range(285):  # 285
                globals()['para' + str(i)] = []
            for row in reader:
                try:
                    for i in range(285):  # 285
                        globals()['para' + str(i)].append(float(row[i]))
                except:
                    continue
#对于给定字典，输入值返回对应的键
def get_key(dic,value):
    return [k for k,v in dic.items() if v == value][0]
if __name__ == '__main__':
    app = QApplication(sys.argv)#实例化一个QApplication
    filename, filetype = QFileDialog.getOpenFileName()#读取文件，将文件路径存储到filename中
    openfile = OpenFile(filename)#实例化一个OpenFile，并打开filename
    index_dic = openfile.open_file_index()#导入索引，存储到index_dic中
    ui = curve_Display(index_dic)#实例化一个curve_Display并运行所有初始化函数
    ui.show()
    sys.exit(app.exec())