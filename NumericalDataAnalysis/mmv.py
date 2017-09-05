import csv
from decimal import Decimal


with open("magic04.txt", "r") as magic_file:

    readCSV = csv.reader(magic_file, delimiter=',')

    # hold each rows mean value.
    means = []

    for row in readCSV:
        mean = 0
        for item in row[:-1]:
            mean += Decimal(item)

        mean = mean / (len(row) - 1)

        means.append(mean)

    for item in means:
        print(item)
