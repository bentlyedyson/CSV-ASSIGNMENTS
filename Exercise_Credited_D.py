import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt

with open('activity.csv', 'r') as f:
    data = csv.reader(f)
    mydictWeekend = {}
    mydictWeekdays = {}
    weekendList = ('2012-10-06', '2012-10-07', '2012-10-13', '2012-10-14', '2012-10-20', '2012-10-21', '2012-10-27', '2012-10-28', '2012-11-03', '2012-11-04', '2012-11-10', '2012-11-11', '2012-11-17', '2012-11-18', '2012-11-24', '2012-11-25')

    for row in data:
        if row[1] in weekendList:
            if row[0] != 'NA' and row[0] != 'steps':
                if row[2] not in mydictWeekend:
                    mydictWeekend[row[2]] = [int(row[0])]
                else:
                    mydictWeekend[row[2]].append(int(row[0]))
        else:
            if row[0] != 'NA' and row[0] != 'steps':
                if row[2] not in mydictWeekdays:
                    mydictWeekdays[row[2]] = [int(row[0])]
                else:
                    mydictWeekdays[row[2]].append(int(row[0]))
#print(mydictWeekend)
#print(mydictWeekdays)

#graph for Weekends
pertimeWeekend = {}
mean_pertimeWeekend = {}

for key, value in mydictWeekend.items():
    pertimeWeekend[key] = sum(value)
    mean_pertimeWeekend[key] = round(statistics.mean(value),2)

plt.plot(list(mean_pertimeWeekend.keys()), list(mean_pertimeWeekend.values()))
plt.title('Weekends')
plt.xlabel('time')
plt.ylabel('steps each 5 time')
plt.show()

#graph for Weekdays
pertimeWeekdays = {}
mean_pertimeWeekdays = {}

for key, value in mydictWeekdays.items():
    pertimeWeekdays[key] = sum(value)
    mean_pertimeWeekdays[key] = round(statistics.mean(value),2)

plt.plot(list(mean_pertimeWeekdays.keys()), list(mean_pertimeWeekdays.values()))
plt.title('Weekdays')
plt.xlabel('time')
plt.ylabel('steps each 5 time')
plt.show()

#plt.plot([semua x value], [semua y value])