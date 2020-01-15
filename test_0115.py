import sys
import csv
from matplotlib import pyplot as plt

# 读取csv文件，append到list中
filename = 'JY-M1-001 2020-01-10 18-49-41.snapshot.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for i in range(17):#285
		globals()['para' + str(i)] = []
	for row in reader:
		try:
			for i in range(17):#285
				globals()['para' + str(i)].append(float(row[i]))
		except:
			continue
#绘制陀螺仪各欧拉角的角度、角速度的函数
#para_x:csv第七列，表示imu时间（作为横坐标）
#para_y:需要打印数据的列（作为纵坐标）
def draw_fig(para_x,para_y):
    for i in ['roll','pitch','yaw']:
        fig = plt.figure(i,dpi = 128,figsize = (12,6))
        k = 1
        for j in ['Angle','velocity']:
            plt.subplot(2,1,k)
            plt.plot(para_x, globals()['para' + str(para_y+(k-1)*3)], c='red', alpha=0.5)
            plt.title(i + '_' + j)
            plt.xlabel('time(s)')
            plt.ylabel(j)
            plt.grid(True)
            k += 1
        para_y += 1
        plt.tight_layout()

draw_fig(para7,8)
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