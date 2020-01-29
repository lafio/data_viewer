from dataDisplay import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout,QFileDialog
import sys,csv
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#在mainwindow绘制曲线并添加到gridlayout
class curve_Display(QMainWindow,Ui_MainWindow):
    def __init__(self,index_dic):
        super().__init__()
        self.index_dic = index_dic
        self.setupUi(self)
        for k,v in index_dic.items():
            self.comboBox.addItem(k)
            self.comboBox.setItemText(v, QtCore.QCoreApplication.translate("MainWindow", k))
        self.comboBox.currentIndexChanged.connect(self.changeFigure)
    def changeFigure(self):
        index_now = index_dic[self.comboBox.currentText()]
        return self.display(1,7,index_now,self.comboBox.currentText())
    def draw_joint_data(self,index):
        title = self.comboBox.currentText()
        for i in range(1,5):
            self.display(i,7,index+3*(i-1),title)
    def display(self,n,para_x,para_y,title):
        self.f = fig_Canvas()
        self.f.draw_data(para_x,para_y)
        if n == 1:
            self.f.Layout = QGridLayout(self.groupBox)
            self.groupBox.setTitle(title)
        else:
            getattr(self,'groupBox_'+str(n)).destroy()
            self.f.Layout = QGridLayout(getattr(self,'groupBox_'+str(n)))
        self.f.Layout.addWidget(self.f)

#定义画板并构造绘制函数
class fig_Canvas(FigureCanvas):
    def __init__(self):
        #self.fig = Figure(figsize = (39,27),dpi=100)
        self.fig = plt.figure()
        self.fig.set_tight_layout(True)
        plt.grid(True)
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
    # 在画板上画图
    def draw_data(self,para_x,para_y):
        x = globals()['para'+str(para_x)]
        y = globals()['para'+str(para_y)]
        self.ax.plot(x, y)
        plt.close(self.fig)

#定义打开csv文件的类
class OpenFile():
    def __init__(self,filename):
        self.open_file_index()
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
    # 读取csv_data文件，append到list中
    def open_file_data(self,filename):
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for i in range(95):  # 285
                globals()['para' + str(i)] = []
            for row in reader:
                try:
                    for i in range(95):  # 285
                        globals()['para' + str(i)].append(float(row[i]))
                except:
                    continue
def get_key(dic,value):
    return [k for k,v in dic.items() if v == value][0]
if __name__ == '__main__':
    app = QApplication(sys.argv)
    filename, filetype = QFileDialog.getOpenFileName()
    openfile = OpenFile(filename)
    index_dic = openfile.open_file_index()
    ui = curve_Display(index_dic)
    ui.show()
    sys.exit(app.exec())