import sys
import csv
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
# 读取csv文件，append到list中
def open_file(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for i in range(95):#285
            globals()['para' + str(i)] = []
        for row in reader:
            try:
                for i in range(95):#285
                    globals()['para' + str(i)].append(float(row[i]))
            except:
                continue

#绘制陀螺仪各欧拉角的角度、角速度的函数
#para_x:csv第七列，表示imu时间（作为横坐标）
#para_y:需要打印数据的列（作为纵坐标）
def draw_imu(para_x,para_y):
    g = 0
    for i in ['roll','pitch','yaw']:
        fig = plt.figure(i,dpi = 128,figsize = (12,6))
        k = 1
        for j in ['Angle','velocity','acceleration']:
            plt.subplot(3,1,k)
            plt.plot(para_x, globals()['para' + str(para_y+(k-1)*3)], c='orange', alpha=1)
            if j == 'acceleration':
                plt.title(['x ','y ','z '][g] + j)
                g += 1
            else:
                plt.title(i + '_' + j)
            plt.xlabel('time(s)')
            plt.ylabel(j)
            plt.grid(True)
            k += 1
        para_y += 1
        plt.tight_layout()
def scatter_imu(para_x,para_y):
    x_axis_start = int(para_x[0])
    x_axis_end = x_axis_start + 1
    for i in range(0,len(para_x)):
        plt.scatter(para_x[i],para_y[i])
        plt.pause(0.0000000000000000000000001)
        if int(para_x[i]) >= x_axis_end:
            x_axis_start += 1
            x_axis_end += 1
            plt.axis([x_axis_start,x_axis_end,-10,10])
#绘制：12个关节角度、角速度、力矩
def draw_joint(para_x, para_y):
    for r in ['Angle','velocity','Torque']:
        for i in ['HipX','HipY','Knee']:
            k = 1
            fig = plt.figure(r+' '+i,dpi = 128,figsize = (12,6))
            for j in ['FL','FR','HL','HR']:
                plt.subplot(4,1,k)
                plt.plot(para_x,globals()['para' + str(para_y + (k-1)*3)],c='blue', alpha=1)
                plt.plot(para_x,globals()['para' + str(para_y + 36 + (k-1)*3)],c='orange',alpha=0.3)
                plt.title(j + '_' + i + '_' + r)
                plt.xlabel('time(s)')
                plt.ylabel(j)
                plt.grid(True)
                k += 1
            para_y += 1
            plt.tight_layout()
        para_y += 9

#打开对话框选择需要打开的文件
app = QtWidgets.QApplication([])
filename,filetype = QFileDialog.getOpenFileName()

#打开文件
open_file(filename)
#绘制点
scatter_imu(para7,para8)
#绘制陀螺仪信息，roll、pitch、yaw 三张图
#draw_imu(para7,8)
#绘制12个关节信息
#draw_joint(para7,22)

plt.show()