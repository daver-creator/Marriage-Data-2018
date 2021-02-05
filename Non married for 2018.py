# Author: 801114005
# September 25, 2020
# This file contains the solution to Lab 1 of DTSC 1301, where we
# manipulate and read data from the Current Population Survey 
# from a CSV file.
import csv
filename = "cps_maritalstatus_2018.csv"
fileobject = open(filename)
all_data = csv.reader(fileobject)
cps_datalist = list(all_data)
headers = cps_datalist.pop(0)
USA = cps_datalist[0:24]
northeast = cps_datalist[24:48]
midwest = cps_datalist[48:72]
south = cps_datalist[72:96]
west = cps_datalist[96:120]

never_married_adults = []
total_adults = []

never_married_count=0
total_adults_count=0
for row in USA[1 : 8]:
    never_married_count += int(row[9])
    total_adults_count += int(row[3])
never_married_adults.append(never_married_count)
total_adults.append(total_adults_count)

never_married_count=0
total_adults_count=0
for row in northeast[1 : 8]:
    never_married_count += int(row[9])
    total_adults_count += int(row[3])
never_married_adults.append(never_married_count)
total_adults.append(total_adults_count)


never_married_count=0
total_adults_count=0
for row in midwest[1 : 8]:
    never_married_count += int(row[9])
    total_adults_count += int(row[3])
never_married_adults.append(never_married_count)
total_adults.append(total_adults_count)

never_married_count=0
total_adults_count=0
for row in south[1 : 8]:
    never_married_count += int(row[9])
    total_adults_count += int(row[3])
never_married_adults.append(never_married_count)
total_adults.append(total_adults_count)

never_married_count=0
total_adults_count=0
for row in west[1 : 8]:
    never_married_count += int(row[9])
    total_adults_count += int(row[3])
never_married_adults.append(never_married_count)
total_adults.append(total_adults_count)

labels = ["USA", "northeast", "midwest", "south", "west"]


for i in range(5):
  print("%s region: %.2f" % (labels[i], float((never_married_adults[i]/total_adults[i])*100))+"%")
