'''
Example script to generate a pie chart which shows the
frequency of the ressorts on Zeit.de
'''

import csv
import sys
import matplotlib.pyplot as plt
from pathlib import Path

# path where the plot gets saved
plot_name = 'ressort_frequency.png'
SAVE_PATH = Path(__file__).resolve().parent.joinpath('plots/').joinpath(plot_name)

# pass csv file via commandline
data = sys.argv[1]

# row where the ressorts are in the csv file
ressort_row = 4

# counters
total_articles = 0
zeit_magazin = 0
gesellschaft = 0
politik = 0
news = 0
kultur = 0
feuilleton = 0
wissen = 0
wirtschaft = 0
sport = 0
digital = 0

other_arr = []


with open(data, encoding='utf-8', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)
    next(reader)

    for row in reader:
        total_articles += 1

        if "zeit" in row[ressort_row].lower():
            zeit_magazin += 1
        elif "gesellschaft" in row[ressort_row].lower():
            gesellschaft += 1
        elif "politik" in row[ressort_row].lower():
            politik += 1
        elif "news" in row[ressort_row].lower():
            news += 1
        elif "kultur" in row[ressort_row].lower():
            kultur += 1
        elif "feuilleton" in row[ressort_row].lower():
            feuilleton += 1
        elif "wissen" in row[ressort_row].lower():
            wissen += 1
        elif "wirtschaft" in row[ressort_row].lower():
            wirtschaft += 1
        elif "sport" in row[ressort_row].lower():
            sport += 1
        elif "digital" in row[ressort_row].lower():
            digital += 1
        else:
            if row[ressort_row] not in other_arr:
                other_arr.append(row[ressort_row])

# print results
print("--- Basic ressorts ---")
print("total articles:", total_articles)
print("zeit-magazin:", zeit_magazin)
print("gesellschaft:", gesellschaft)
print("politik:", politik)
print("news:", news)
print("kultur:", kultur)
print("feuilleton:", feuilleton)
print("wissen:", wissen)
print("wirtschaft:", wirtschaft)
print("sport:", sport)
print("digital:", digital)
print("others:", total_articles - zeit_magazin - gesellschaft - politik - news - kultur - feuilleton - wissen - wirtschaft - sport - digital)
print("other:", other_arr)

# plot article frequency

def percentage(ressort):
    x = total_articles / 100
    return ressort * x

labels = 'zeit-magazin', 'gesellschaft', 'politik', 'news', 'kultur', 'feuilleton', 'wissen', 'sport', 'digital', 'other'
sizes = [percentage(zeit_magazin),
         percentage(gesellschaft),
         percentage(politik),
         percentage(news),
         percentage(kultur),
         percentage(feuilleton),
         percentage(wissen),
         percentage(sport),
         percentage(digital),
         percentage(total_articles - zeit_magazin - gesellschaft - politik - news - kultur - feuilleton - wissen - wirtschaft - sport - digital)]
# explode = (0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01)

plt.style.use('seaborn-ticks')
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Frequency of ressorts on Zeit.de')
plt.savefig(SAVE_PATH)
plt.show()
