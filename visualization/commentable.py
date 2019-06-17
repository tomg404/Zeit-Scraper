'''
Example script to generate a bar chart which shows the number of commentable
articles on Zeit.de
'''

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# path where the plot gets saved
plot_name = 'commentable.png'
SAVE_PATH = Path(__file__).resolve().parent.joinpath('plots/').joinpath(plot_name)

# pass csv file via commandline
data = sys.argv[1]
d = {}

# row where the ressorts are in the csv file
rowNumber = 6

with open(data, 'r', encoding='utf-8', newline='') as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	next(reader)	# skip the first two lines IMPORTANT
	next(reader)

	for row in reader:
		if row[rowNumber] not in d:
			d[str(row[rowNumber])] = 1
		else:
			d[str(row[rowNumber])] += 1

print(d)



objects = tuple(key for key in d.keys())
y_pos = np.arange(len(objects))
number = d.values()

plt.style.use('ggplot')
barlist = plt.bar(y_pos, number, align='center')
barlist[0].set_color('#60BD68')
barlist[1].set_color('#F15854')

plt.xticks(y_pos, objects)
plt.xlabel('Commentable?')
plt.ylabel('Number')
plt.title('Number of commentable articles on Zeit.de')

plt.savefig(SAVE_PATH)
plt.show()
