import sys
import csv
import ctypes
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np

class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig, ax, step=0.1):
        plt.close("all")
        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance() 

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.ax = ax
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollBar(QtCore.Qt.Horizontal)
        self.step = step
        self.setupSlider()
        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.canvas)
        self.widget.layout().addWidget(self.scroll)

        self.canvas.draw()
        self.show()
        self.app.exec_()

    def setupSlider(self):
        self.lims = np.array(self.ax.get_xlim())
        self.scroll.setPageStep(self.step*100)
        self.scroll.actionTriggered.connect(self.update)
        self.update()

    def update(self, evt=None):
        r = self.scroll.value()/((1+self.step)*100)
        l1 = self.lims[0]+r*np.diff(self.lims)
        l2 = l1 +  np.diff(self.lims)*self.step
        self.ax.set_xlim(l1,l2)
        print(self.scroll.value(), l1,l2)
        self.fig.canvas.draw_idle()

# Get imu_time, roll_deg, and pitch_deg ... from file.
filename = 'JY-L1-001 2020-01-06 02-00-59.snapshot.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for i in range(285):
		locals()['para' + str(i)] = []
	for row in reader:
		try:
			for i in range(285):
				locals()['para' + str(i)].append(float(row[i]))
		except:
			continue
whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd) 

#绘制第一张图，陀螺仪信息
fig1 = plt.figure('imu',dpi=128, figsize=(12, 6))
plt.subplot(331)
plt.plot(para7, para8, c='red', alpha=0.5)
plt.title('roll_degree')
plt.xlabel('time(s)')
plt.ylabel('roll')
plt.grid(True)

plt.subplot(334)
plt.plot(para7, para9, c='blue', alpha=0.5)
plt.title('pitch_degree')
plt.xlabel('time(s)')
plt.ylabel('pitch')
plt.grid(True)

plt.subplot(337)
plt.plot(para7, para10, c='black', alpha=0.5)
plt.title('yaw_degree')
plt.xlabel('time(s)')
plt.ylabel('yaw')
plt.grid(True)

plt.subplot(332)
plt.plot(para7, para11, c='red', alpha=0.5)
plt.title('roll_velocity')
plt.xlabel('time(s)')
plt.ylabel('roll')
plt.grid(True)

plt.subplot(335)
plt.plot(para7, para12, c='blue', alpha=0.5)
plt.title('pitch_velocity')
plt.xlabel('time(s)')
plt.ylabel('pitch')
plt.grid(True)

plt.subplot(338)
plt.plot(para7, para13, c='black', alpha=0.5)
plt.title('yaw_velocity')
plt.xlabel('time(s)')
plt.ylabel('yaw')
plt.grid(True)

plt.subplot(333)
plt.plot(para7, para14, c='red', alpha=0.5)
plt.title('x_acc')
plt.xlabel('time(s)')
plt.ylabel('x_acc')
plt.grid(True)

plt.subplot(336)
plt.plot(para7, para15, c='blue', alpha=0.5)
plt.title('y_acc')
plt.xlabel('time(s)')
plt.ylabel('y_acc')
plt.grid(True)

plt.subplot(339)
plt.plot(para7, para16, c='black', alpha=0.5)
plt.title('z_acc')
plt.xlabel('time(s)')
plt.ylabel('z_acc')
plt.grid(True)
plt.tight_layout()

plt.show()