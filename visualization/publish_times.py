import csv
import matplotlib.pyplot as plt
import sys
from dateutil import parser
import datetime
import numpy as np
from pathlib import Path

# path where the plot gets saved
plot_name = 'publish_time.png'
SAVE_PATH = Path(__file__).resolve().parent.joinpath('plots/').joinpath(plot_name)

# pass csv file via commandline
data = sys.argv[1]

# col where the publish date is located
date_col = 12

# dict for the time the articles get published and the amount
d = {0: 0,
     1: 0,
     2: 0,
     3: 0,
     4: 0,
     5: 0,
     6: 0,
     7: 0,
     8: 0,
     9: 0,
     10: 0,
     11: 0,
     12: 0,
     13: 0,
     14: 0,
     15: 0,
     16: 0,
     17: 0,
     18: 0,
     19: 0,
     20: 0,
     21: 0,
     22: 0,
     23: 0,}

article_counter = 0

with open(data, encoding='utf-8', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)
    next(reader)

    for row in reader:
        hour = parser.parse(row[date_col]).hour
        d[hour] += 1
        article_counter += 1

print('Total articles:', article_counter)



objects = d.keys()
y_pos = range(len(d))
performance = d.values()

plt.style.use('ggplot')
plt.bar(y_pos, performance, align='center', edgecolor='k')
plt.xticks(y_pos, objects)
plt.xlabel('Time of day in hours')
plt.ylabel('Number of published articles')
plt.title('Time of day when articles get published on Zeit.de')

plt.savefig(SAVE_PATH)
plt.show()
