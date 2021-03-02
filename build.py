#! /usr/local/bin/python

import collections
import csv
import glob

# Read food choices
food = []
stats = collections.Counter()

for file in glob.glob("food/*.txt"):
    with open(file) as handle:
        choices = set([line.strip().lower() for line in handle.readlines()])
        stats.update(choices)

# Calculate stats
output_rows = [{'food': food, 'count': count} for food, count in stats.items()]
print(output_rows)

# Write CSV
with open("choices.csv", mode="w") as output:
    writer = csv.DictWriter(output, fieldnames=['food', 'count'])
    writer.writeheader()
    writer.writerows(output_rows)
