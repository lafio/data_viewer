from dataDisplay import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#在mainwindow绘制曲线并添加到gridlayout
class curve_Display(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(1,5):
            self.gan(i)
    def gan(self,n):
        self.f = fig_Canvas()
        self.f.drawit()
        if n == 1:
            self.f.Layout = QGridLayout(self.groupBox)
        else:
            self.f.Layout = QGridLayout(getattr(self,'groupBox_'+str(n)))
        self.f.Layout.addWidget(self.f)

#定义画板
class fig_Canvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize = (39,27),dpi=100)
        self.fig.set_tight_layout(True)
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
    def drawit(self):
        x = [i for i in range(9)]
        y = [i**2 for i in range(9)]
        self.ax.plot(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = curve_Display()
    ui.show()
    sys.exit(app.exec())