import csv
import ctypes
from matplotlib import pyplot as plt

# Get imu_time, roll_deg, and pitch_deg temperatures from file.
filename = 'JY-M1-001 2020-01-10 18-49-41.snapshot.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	imu_times, roll_degs, pitch_degs, yaw_degs, roll_vels, pitch_vels, yaw_vels\
	 = [], [], [], [], [], [], []
	for row in reader:
		try:
			imu_time = float(row[7])
			roll_deg = float(row[8])
			pitch_deg = float(row[9])
			yaw_deg = float(row[10])
			roll_vel = float(row[11])
			pitch_vel = float(row[12])
			yaw_vel = float(row[13])
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
whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd) 

# Plot data.
plt.subplot(321)
#fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(imu_times, roll_degs, c='red', alpha=0.5)
plt.title('roll_degree')
plt.xlabel('time/s')
plt.ylabel('roll')
plt.grid(True)

plt.subplot(323)
plt.plot(imu_times, pitch_degs, c='blue', alpha=0.5)
plt.title('pitch_degree')
plt.xlabel('time/s')
plt.ylabel('pitch')
plt.grid(True)

plt.subplot(325)
plt.plot(imu_times, yaw_degs, c='black', alpha=0.5)
plt.title('yaw_degree')
plt.xlabel('time/s')
plt.ylabel('yaw')
plt.grid(True)

plt.subplot(322)
plt.plot(imu_times, roll_vels, c='red', alpha=0.5)
plt.title('roll_velocity')
plt.xlabel('time/s')
plt.ylabel('roll')
plt.grid(True)

plt.subplot(324)
plt.plot(imu_times, pitch_vels, c='blue', alpha=0.5)
plt.title('pitch_velocity')
plt.xlabel('time/s')
plt.ylabel('pitch')
plt.grid(True)

plt.subplot(326)
plt.plot(imu_times, yaw_vels, c='black', alpha=0.5)
plt.title('yaw_velocity')
plt.xlabel('time/s')
plt.ylabel('yaw')
plt.grid(True)

plt.tight_layout()
plt.show()
