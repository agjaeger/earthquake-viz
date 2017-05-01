import csv

dataFile = open("../data/2015EMS.csv", "r")
newData = open("../data/2015EMSOrg.csv", "w")

dataDict = {}

reader = csv.reader(dataFile)

for row in reader:
	if row[1] not in dataDict.keys():
		dataDict[row[1]] = 0
	dataDict[row[1]] += 1

for k, v in dataDict.items():
	if len(k) == 5:
		newData.write(k + "," + str(v) + "\n")