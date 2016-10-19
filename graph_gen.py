import matplotlib.pyplot as plt
import sys

df_list = []

filename = 'logfile.txt'

if len(sys.argv) >= 2:
    filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        # remove whitespace at the start and the newline at the end
        line = line.strip()
        row = line.split("\t")
        if len(row) == 5:  # skip lines with only one value
            cols = [float(l) for l in row]
            df_list.append(cols)

timestamps = map(lambda x: x[0], df_list)
ref_angle_1 = map(lambda x: abs(x[1]), df_list)
angle_1 = map(lambda x: abs(x[2]), df_list)
error_1 = [(ang - ref) for (ang, ref) in zip(angle_1, ref_angle_1)]
ref_angle_2 = map(lambda x: abs(x[3]), df_list)
angle_2 = map(lambda x: abs(x[4]), df_list)
error_2 = [(ang - ref) for (ang, ref) in zip(angle_2, ref_angle_2)]

plt.subplot(1, 2, 1)
plt.plot(timestamps, ref_angle_1, label="reference angle 1")
plt.plot(timestamps, angle_1, label="angle 1")
plt.plot(timestamps, error_1, label="error")
plt.xlabel('time (s)')
plt.ylabel('angle (radians)')
plt.legend(loc=0)
plt.title('Motor 1')

plt.subplot(1, 2, 2)
plt.plot(timestamps, ref_angle_2, label="reference angle 2")
plt.plot(timestamps, angle_2, label="angle 2")
plt.plot(timestamps, error_2, label="error")
plt.xlabel('time (s)')
plt.ylabel('angle (radians)')
plt.legend(loc=0)
plt.title('Motor 2')

plt.suptitle('Angle values before tuning')
plt.show()
