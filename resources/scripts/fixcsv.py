
import csv

dataFile = open("../data/EMS_Data_2015_cleaned_by_date.csv")
newData = open("../data/2015EMS.csv", "w")
try:
	reader = csv.reader(dataFile)
	
	for row in reader:
		newData.write(row[0] + "," + row[1] + "\n")
finally:
	dataFile.close()
	newData.close()