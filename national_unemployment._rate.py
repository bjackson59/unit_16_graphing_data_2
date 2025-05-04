from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, col_title in enumerate(header_row):
#    print(f'{index} {col_title}, ', end= ' ')
# print()

dates = []
unemployment_rate = []

for row in reader:
    time = str(row[0])
    rate = float(row[1])
    dates.append(time)
    unemployment_rate.append(rate)

plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(rate, color='green')

graph.set_title('The National Unemployment Rate from 1976 to 2022 by Month')
graph.set_ylabel('Unemployment Rate')

plt.show()