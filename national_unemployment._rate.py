# Brianna Jackson
# 5/4/25
# Graphing unemployment data 

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, col_title in enumerate(header_row):
   print(f'{index} {col_title}, ', end= ' ')
print()

dates = []
unemployment_rate = []

for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    rate = float(row[1])
    dates.append(current_date)
    unemployment_rate.append(rate)

plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(dates, unemployment_rate, color='green')


graph.set_title('The National Unemployment Rate from 1975 - 2022 by Year')
graph.set_ylabel('Unemployment Rate')
graph.set_xlabel('Date (Yearly)')


plt.show()