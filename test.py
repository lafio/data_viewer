import sys
import csv
from matplotlib import pyplot as plt

toolbar_width = 40
# Get dates, roll_deg, and pitch_deg temperatures from file.
filename = 'JY-M1-001 2020-01-10 18-49-41.snapshot.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	timestramps, roll_degs, pitch_degs, yaw_degs = [], [], [], []
	for row in reader:
		try:
			timestramp = float(row[7])
			roll_deg = float(row[8])
			pitch_deg = float(row[9])
			yaw_deg = float(row[10])
		except:
			continue
		else:
			timestramps.append(timestramp)
			roll_degs.append(roll_deg)
			pitch_degs.append(pitch_deg)
			yaw_degs.append(yaw_deg)

# Plot data.
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(timestramps, roll_degs, c='red', alpha=0.5)
plt.plot(timestramps, pitch_degs, c='blue', alpha=0.5)
#plt.fill_between(timestramps, roll_degs, pitch_degs, facecolor='blue', alpha=0.1)
plt.plot(timestramps, yaw_degs, c='yellow', alpha=0.5)
# Format plot.
title = "IMU_degrees"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("roll,pitch,yaw", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.grid(True)

plt.show()
