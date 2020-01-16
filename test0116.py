import sys
import csv
from matplotlib import pyplot as plt

# 读取csv文件，append到list中
filename = 'JY-M1-001 2020-01-10 18-49-41.snapshot.csv'
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
def draw_fig(para_x,para_y):
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

#绘制：12个关节角度、角速度、力矩
def draw_joint(para_x,para_y):
    for r in ['Angle','velocity','Torque']:
        for i in ['HipX','HipY','Knee']:
            fig = plt.figure(r,dpi = 128,figsize = (12,6))
            k = 1
            for j in ['FL','FR','HL','HR']:
                plt.subplot(4,1,k)
                plt.plot(para_x,globals()['para' + str(para_y + (k-1)*3)],c='orange', alpha=1)
                plt.plot(para_x,globals()['para' + str(para_y + 36 + (k-1)*3)],c='blue',alpha=1)
                plt.title(j + '_' + i + '_' + r)
                plt.xlabel('time(s)')
                plt.ylabel(j)
                plt.grid(True)
                k += 1
            para_y += 1
            plt.tight_layout()
        para_y += 9
#绘制陀螺仪信息，roll、pitch、yaw 三张图
draw_fig(para7,8)
#绘制12个关节信息
draw_joint(para7,22)

plt.show()