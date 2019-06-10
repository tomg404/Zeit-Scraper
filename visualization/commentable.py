'''
Example script to generate a bar chart which shows the number of commentable
articles on Zeit.de
'''

import csv
import numpy as np

data = 'data.csv'
d = {}

rowNumber = 6

with open(data, 'r', encoding='utf-8') as csvFile:
	reader = csv.reader(csvFile, delimiter=',')
	next(reader)	# skip the first line IMPORTANT
	for row in reader:
		if row[rowNumber] not in d:
			d[str(row[rowNumber])] = 1
		else:
			d[str(row[rowNumber])] += 1

print(d)

import matplotlib.pyplot as plt
objects = tuple(key for key in d.keys())
y_pos = np.arange(len(objects))
number = d.values()

barlist = plt.bar(y_pos, number, align='center', color='c')
barlist[0].set_color('#60BD68')
barlist[1].set_color('#F15854')
barlist[2].set_color('#4D4D4D')
plt.xticks(y_pos, objects)
plt.xlabel('Commentable?')
plt.ylabel('Number')
plt.title('Number of commentable articles on Zeit.de')

plt.show()
