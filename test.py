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
filename = 'JY-L1-002 2020-01-14 08-25-46.snapshot.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	imu_times, roll_degs, pitch_degs, yaw_degs, roll_vels, pitch_vels, yaw_vels,\
	x_accs, y_accs, z_accs, in_FL_HipX_Angs, in_FL_HipY_Angs, in_FL_Knee_Angs,\
	in_FL_HipX_Vels, in_FL_HipY_Vels, in_FL_Knee_Vels,\
	in_FL_HipX_Tors, in_FL_HipY_Tors, in_FL_Knee_Tors,\
	in_FR_HipX_Angs, in_FR_HipY_Angs, in_FR_Knee_Angs,\
	in_FR_HipX_Vels, in_FR_HipY_Vels, in_FR_Knee_Vels,\
	in_FR_HipX_Tors, in_FR_HipY_Tors, in_FR_Knee_Tors,\
	in_HL_HipX_Angs, in_HL_HipY_Angs, in_HL_Knee_Angs,\
	in_HL_HipX_Vels, in_HL_HipY_Vels, in_HL_Knee_Vels,\
	in_HL_HipX_Tors, in_HL_HipY_Tors, in_HL_Knee_Tors,\
	in_HR_HipX_Angs, in_HR_HipY_Angs, in_HR_Knee_Angs,\
	in_HR_HipX_Vels, in_HR_HipY_Vels, in_HR_Knee_Vels,\
	in_HR_HipX_Tors, in_HR_HipY_Tors, in_HR_Knee_Tors,\
	 = [], [], [], [], [], [], [], [], [], [],\
	 [], [], [], [], [], [], [], [], [],\
	 [], [], [], [], [], [], [], [], [],\
	 [], [], [], [], [], [], [], [], [],\
	 [], [], [], [], [], [], [], [], []
	for row in reader:
		try:
			imu_time = float(row[7])
			roll_deg = float(row[8])
			pitch_deg = float(row[9])
			yaw_deg = float(row[10])
			roll_vel = float(row[11])
			pitch_vel = float(row[12])
			yaw_vel = float(row[13])
			x_acc = float(row[14])
			y_acc = float(row[15])
			z_acc = float(row[16])
			in_FL_HipX_Ang = float(row[22])
			in_FL_HipY_Ang = float(row[23]) 
			in_FL_Knee_Ang = float(row[24])
			in_FR_HipX_Ang = float(row[25])
			in_FR_HipY_Ang = float(row[26])
			in_FR_Knee_Ang = float(row[27])
			in_HL_HipX_Ang = float(row[28])
			in_HL_HipY_Ang = float(row[29])
			in_HL_Knee_Ang = float(row[30])
			in_HR_HipX_Ang = float(row[31])
			in_HR_HipY_Ang = float(row[32])
			in_HR_Knee_Ang = float(row[33])
			in_FL_HipX_Vel = float(row[34])
			in_FL_HipY_Vel = float(row[35])
			in_FL_Knee_Vel = float(row[36])
			in_FR_HipX_Vel = float(row[37])
			in_FR_HipY_Vel = float(row[38])
			in_FR_Knee_Vel = float(row[39])
			in_HL_HipX_Vel = float(row[40])
			in_HL_HipY_Vel = float(row[41])
			in_HL_Knee_Vel = float(row[42])
			in_HR_HipX_Vel = float(row[43])
			in_HR_HipY_Vel = float(row[44])
			in_HR_Knee_Vel = float(row[45])
			in_FL_HipX_Tor = float(row[46])
			in_FL_HipY_Tor = float(row[47])
			in_FL_Knee_Tor = float(row[48])
			in_FR_HipX_Tor = float(row[49])
			in_FR_HipY_Tor = float(row[50])
			in_FR_Knee_Tor = float(row[51])
			in_HL_HipX_Tor = float(row[52])
			in_HL_HipY_Tor = float(row[53])
			in_HL_Knee_Tor = float(row[54])
			in_HR_HipX_Tor = float(row[55])
			in_HR_HipY_Tor = float(row[56])
			in_HR_Knee_Tor = float(row[57])
		except:
			continue
		else:
			imu_times.append(imu_time)
			roll_degs.append(roll_deg)
			pitch_degs.append(pitch_deg)
			yaw_degs.append(yaw_deg)
			roll_vels.append(roll_vel)
			pitch_vels.append(pitch_vel)
			yaw_vels.append(yaw_vel)
			x_accs.append(x_acc)
			y_accs.append(y_acc)
			z_accs.append(z_acc)
			in_FL_HipX_Angs.append(in_FL_HipX_Ang)
			in_FL_HipY_Angs.append(in_FL_HipY_Ang)
			in_FL_Knee_Angs.append(in_FL_Knee_Ang)
			in_FL_HipX_Vels.append(in_FL_HipX_Vel)
			in_FL_HipY_Vels.append(in_FL_HipY_Vel)
			in_FL_Knee_Vels.append(in_FL_Knee_Vel)
			in_FL_HipX_Tors.append(in_FL_HipX_Tor)
			in_FL_HipY_Tors.append(in_FL_HipY_Tor)
			in_FL_Knee_Tors.append(in_FL_Knee_Tor)
			in_FR_HipX_Angs.append(in_FR_HipX_Ang)
			in_FR_HipY_Angs.append(in_FR_HipY_Ang)
			in_FR_Knee_Angs.append(in_FR_Knee_Ang)
			in_FR_HipX_Vels.append(in_FR_HipX_Vel)
			in_FR_HipY_Vels.append(in_FR_HipY_Vel)
			in_FR_Knee_Vels.append(in_FR_Knee_Vel)
			in_FR_HipX_Tors.append(in_FR_HipX_Tor)
			in_FR_HipY_Tors.append(in_FR_HipY_Tor)
			in_FR_Knee_Tors.append(in_FR_Knee_Tor)
			in_HL_HipX_Angs.append(in_HL_HipX_Ang)
			in_HL_HipY_Angs.append(in_HL_HipY_Ang)
			in_HL_Knee_Angs.append(in_HL_Knee_Ang)
			in_HL_HipX_Vels.append(in_HL_HipX_Vel)
			in_HL_HipY_Vels.append(in_HL_HipY_Vel)
			in_HL_Knee_Vels.append(in_HL_Knee_Vel)
			in_HL_HipX_Tors.append(in_HL_HipX_Tor)
			in_HL_HipY_Tors.append(in_HL_HipY_Tor)
			in_HL_Knee_Tors.append(in_HL_Knee_Tor)
			in_HR_HipX_Angs.append(in_HR_HipX_Ang)
			in_HR_HipY_Angs.append(in_HR_HipY_Ang)
			in_HR_Knee_Angs.append(in_HR_Knee_Ang)
			in_HR_HipX_Vels.append(in_HR_HipX_Vel)
			in_HR_HipY_Vels.append(in_HR_HipY_Vel)
			in_HR_Knee_Vels.append(in_HR_Knee_Vel)
			in_HR_HipX_Tors.append(in_HR_HipX_Tor)
			in_HR_HipY_Tors.append(in_HR_HipY_Tor)
			in_HR_Knee_Tors.append(in_HR_Knee_Tor)
whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd) 

#绘制第一张图，陀螺仪信息
fig1 = plt.figure('imu',dpi=128, figsize=(12, 6))
plt.subplot(331)
plt.plot(imu_times, roll_degs, c='red', alpha=0.5)
plt.title('roll_degree')
plt.xlabel('time(s)')
plt.ylabel('roll')
plt.grid(True)

plt.subplot(334)
plt.plot(imu_times, pitch_degs, c='blue', alpha=0.5)
plt.title('pitch_degree')
plt.xlabel('time(s)')
plt.ylabel('pitch')
plt.grid(True)

plt.subplot(337)
plt.plot(imu_times, yaw_degs, c='black', alpha=0.5)
plt.title('yaw_degree')
plt.xlabel('time(s)')
plt.ylabel('yaw')
plt.grid(True)

plt.subplot(332)
plt.plot(imu_times, roll_vels, c='red', alpha=0.5)
plt.title('roll_velocity')
plt.xlabel('time(s)')
plt.ylabel('roll')
plt.grid(True)

plt.subplot(335)
plt.plot(imu_times, pitch_vels, c='blue', alpha=0.5)
plt.title('pitch_velocity')
plt.xlabel('time(s)')
plt.ylabel('pitch')
plt.grid(True)

plt.subplot(338)
plt.plot(imu_times, yaw_vels, c='black', alpha=0.5)
plt.title('yaw_velocity')
plt.xlabel('time(s)')
plt.ylabel('yaw')
plt.grid(True)

plt.subplot(333)
plt.plot(imu_times, x_accs, c='red', alpha=0.5)
plt.title('x_acc')
plt.xlabel('time(s)')
plt.ylabel('x_acc')
plt.grid(True)

plt.subplot(336)
plt.plot(imu_times, y_accs, c='blue', alpha=0.5)
plt.title('y_acc')
plt.xlabel('time(s)')
plt.ylabel('y_acc')
plt.grid(True)

plt.subplot(339)
plt.plot(imu_times, z_accs, c='black', alpha=0.5)
plt.title('z_acc')
plt.xlabel('time(s)')
plt.ylabel('z_acc')
plt.grid(True)
plt.tight_layout()

#绘制第二张图，各HipX关节角度
fig2 = plt.figure('actual joint angle motion-HipX',dpi=128, figsize=(12, 6))
plt.subplot(221)
plt.plot(imu_times, in_FL_HipX_Angs, c='red', alpha=0.5)
plt.title('in_FL_HipX_Angle')
plt.xlabel('time(s)')
plt.ylabel('in_FL_HipX_Ang(rad)')
plt.grid(True)

plt.subplot(222)
plt.plot(imu_times, in_FR_HipX_Angs, c='red', alpha=0.5)
plt.title('in_FR_HipX_Angle')
plt.xlabel('time(s)')
plt.ylabel('in_FR_HipX_Ang(rad)')
plt.grid(True)

plt.subplot(223)
plt.plot(imu_times, in_HL_HipX_Angs, c='red', alpha=0.5)
plt.title('in_HL_HipX_Angle')
plt.xlabel('time(s)')
plt.ylabel('in_HL_HipX_Ang(rad)')
plt.grid(True)

plt.subplot(224)
plt.plot(imu_times, in_HR_HipX_Angs, c='red', alpha=0.5)
plt.title('in_HR_HipX_Angle')
plt.xlabel('time(s)')
plt.ylabel('in_HR_HipX_Ang(rad)')
plt.grid(True)
plt.tight_layout()

#绘制第三张图，各HipX关节角速度
fig3 = plt.figure('actual joint velocity motion-HipX',dpi=128, figsize=(12, 6))
plt.subplot(221)
plt.plot(imu_times, in_FL_HipX_Vels, c='red', alpha=0.5)
plt.title('in_FL_HipX_Velocity')
plt.xlabel('time(s)')
plt.ylabel('in_FL_HipX_Velocity(rad/s)')
plt.grid(True)

plt.subplot(222)
plt.plot(imu_times, in_FR_HipX_Vels, c='red', alpha=0.5)
plt.title('in_FR_HipX_Velocity')
plt.xlabel('time(s)')
plt.ylabel('in_FR_HipX_Velocity(rad/s)')
plt.grid(True)

plt.subplot(223)
plt.plot(imu_times, in_HL_HipX_Vels, c='red', alpha=0.5)
plt.title('in_HL_HipX_Velocity')
plt.xlabel('time(s)')
plt.ylabel('in_HL_HipX_Velocity(rad/s)')
plt.grid(True)

plt.subplot(224)
plt.plot(imu_times, in_HR_HipX_Vels, c='red', alpha=0.5)
plt.title('in_HR_HipX_Velocity')
plt.xlabel('time(s)')
plt.ylabel('in_HR_HipX_Velocity(rad/s)')
plt.grid(True)
plt.tight_layout()

#绘制第四张图，各HipX关节力矩
fig4 = plt.figure('actual joint torque motion-HipX',dpi=128, figsize=(12, 6))
plt.subplot(221)
plt.plot(imu_times, in_FL_HipX_Tors, c='red', alpha=0.5)
plt.title('in_FL_HipX_Torque')
plt.xlabel('time(s)')
plt.ylabel('in_FL_HipX_Torque(Nm)')
plt.grid(True)

plt.subplot(222)
plt.plot(imu_times, in_FR_HipX_Tors, c='red', alpha=0.5)
plt.title('in_FR_HipX_Torque')
plt.xlabel('time(s)')
plt.ylabel('in_FR_HipX_Torque(Nm)')
plt.grid(True)

plt.subplot(223)
plt.plot(imu_times, in_HL_HipX_Tors, c='red', alpha=0.5)
plt.title('in_HL_HipX_Torque')
plt.xlabel('time(s)')
plt.ylabel('in_HL_HipX_Torque(Nm)')
plt.grid(True)

plt.subplot(224)
plt.plot(imu_times, in_HR_HipX_Tors, c='red', alpha=0.5)
plt.title('in_HR_HipX_Torque')
plt.xlabel('time(s)')
plt.ylabel('in_HR_HipX_Torque(Nm)')
plt.grid(True)
plt.tight_layout()



plt.show()