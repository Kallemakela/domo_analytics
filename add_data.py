import get_data
import bs4
from datetime import datetime
import csv
import config

data = get_data.get_data()
pos = []
time = str(datetime.now())
for li in data:
    pos += li.contents[2]
#Add full path so you can run program wihtout being in the dir
with open(config.path + 'Domo_analytics/data.csv','a') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([time] + pos)
print("Data added!")
