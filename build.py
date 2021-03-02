#! /usr/local/bin/python

from itertools import groupby
import csv
import glob

# Read food choices
food = []
for file in glob.glob("food/*.txt"):
    with open(file) as handle:
        choices = set([line.strip().lower() for line in handle.readlines()])
        food.extend(choices)

# Calculate stats
stats = [{'food': key, 'count': len(list(group))} for key, group in groupby(food)]

# Write CSV
with open("choices.csv", mode="w") as output:
    writer = csv.DictWriter(output, fieldnames=['food', 'count'])
    writer.writeheader()
    writer.writerows(stats)
    
print(stats)