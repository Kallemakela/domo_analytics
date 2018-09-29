import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime

def transform_time(times):
    newTimes = []
    for time in times:
        newTimes.append(mdates.date2num(datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')))
    return newTimes

data = pd.read_csv("data.csv")
names = list(data)[1:]
x = list(data['names'][1:])
x = transform_time(x)

for name in names:
    y = list(data[name][1:])
    plt.scatter(x, y)

plt.show()
