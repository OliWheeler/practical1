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

times = map(lambda x: x[0], df_list)
ref_angle_1 = map(lambda x: abs(x[1]), df_list)
angle_1 = map(lambda x: abs(x[2]), df_list)
ref_angle_2 = map(lambda x: abs(x[3]), df_list)
angle_2 = map(lambda x: abs(x[4]), df_list)

plt.plot(times, ref_angle_1)
plt.plot(times, angle_1)
plt.plot(times, ref_angle_2)
plt.plot(times, angle_2)

plt.show()
