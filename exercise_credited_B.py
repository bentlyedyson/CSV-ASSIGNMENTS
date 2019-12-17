import csv          
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

with open('activity.csv', 'r') as f:
    data = csv.reader(f)
    mydict = {}
    for row in data:
        if row[0] != 'NA' and row[0] != 'steps':
            if row[2] not in mydict:
                mydict[row[2]] = [int(row[0])]
            else:
                mydict[row[2]].append(int(row[0]))


totalpertime = {}
mean_totaltime = {}
median_pertime = {}
for key, value in mydict.items():
    totalpertime[key] = sum(value)
    mean_totaltime[key] = round(mean(value),2)
plt.plot(list(mean_totaltime.keys()), list(mean_totaltime.values()))
plt.ylabel('steps each 5 time')
plt.xlabel('time')
plt.show()