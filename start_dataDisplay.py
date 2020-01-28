from dataDisplay import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout,QFileDialog
import sys,csv
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#在mainwindow绘制曲线并添加到gridlayout
class curve_Display(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.index_dic = {'Angle_HipX': 22, 'Angle_HipY': 23, 'Angle_Knee': 24,\
                     'Velocity_HipX': 34, 'Velocity_HipY': 35, 'Velocity_Knee': 36,\
                     'Torque_HipX': 46, 'Torque_HipY': 47, 'Torque_Knee': 48}
        self.draw_joint_data(self.index_dic['Angle_HipX'])
    def draw_joint_data(self,index):
        for i in range(1,5):
            self.display(i,7,index+3*(i-1))
    def display(self,n,para_x,para_y):
        self.f = fig_Canvas()
        self.f.draw_data(para_x,para_y)
        if n == 1:
            self.f.Layout = QGridLayout(self.groupBox)
        else:
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

#定义打开csv文件的类
class OpenFile():
    def __init__(self,filename):
        self.open_file(filename)
    # 读取csv文件，append到list中
    def open_file(self,filename):
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    filename, filetype = QFileDialog.getOpenFileName()
    openfile = OpenFile(filename)
    ui = curve_Display()
    ui.show()
    sys.exit(app.exec())