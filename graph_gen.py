import matplotlib.pyplot as plt
import pandas as pd


df_list = []

with open('logfile.txt', 'r') as f:
    for line in f:
        # remove whitespace at the start and the newline at the end
        line = line.strip()
        row = line.split("\t")
        if len(row) != 1:
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

#, angle_1, ref_angle_2, angle_2)


plt.show()
savefig("graph.png")
#df = pd.DataFrame(df_list)
#print(df)

#df.plot()
