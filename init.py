import get_data
import bs4
import csv

data = get_data.get_data()
names = []
apartments = []
for li in data:
    names.append(li.contents[0])
    apartments += li.contents[1]
with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['names'] + names)
    filewriter.writerow(['apartments'] + apartments)
