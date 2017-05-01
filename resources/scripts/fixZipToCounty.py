
data = []
with open("../data/zipToCountyClean.csv", "w") as outputFile:
	with open("../data/zipToCountyRaw.txt", "r") as inputFile:		
		for line in inputFile:
			if "View Map" not in line:
				splitLine = line.split('\t')
				outputFile.write(splitLine[0]+","+splitLine[2]+"\n")
				data.append([splitLine[0], splitLine[2]])

countyList = []				
for d in data:
	if d[1] not in countyList:
		countyList.append(d[1])
		
print(countyList)
print(len(countyList))