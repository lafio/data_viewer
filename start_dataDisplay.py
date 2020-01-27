from dataDisplay import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout
from PyQt5.QtCore import QTimer
import sys,time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.lines import Line2D

class curve_Display(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LineFigure = fig_Canvas()
        self.LineFigure.drawit()
        self.LineFigureLayout = QGridLayout(self.groupBox)
        self.LineFigureLayout.addWidget(self.LineFigure)
        #self.LineFigure.ax.set_xlim(-4, 4)
        #self.LineFigure.ax.set_ylim(-1, 1)
        #self.line = Line2D([-4,-3,-2,-1,1,2,3,4], [0.2,-0.3,0.9,-0.8,0.8,0.9,0,-0.4])
        #self.LineFigure.ax.add_line(self.line)
class fig_Canvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize = (39,27),dpi=100)
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