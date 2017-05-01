from __future__ import print_function

import csv
import json
import datetime
import numpy as np

from random import randint
from operator import itemgetter

eqFile = open("../data/earthquakeData.csv")
emsFile = open("../data/2015EMS.csv")
zipToCountyFile = open("../data/zipToCountyClean.csv")

eqReader = csv.reader(eqFile)
emsReader = csv.reader(emsFile)
zipToCountyReader = csv.reader(zipToCountyFile)

eqs = []
emsData = []
zipToCounty = {}

for row in zipToCountyReader:
	zipToCounty[row[0]] = row[1]

for row in emsReader:
	if len(row[1]) == 5:
		emsData.append(row)

for row in eqReader:
	if row[0][3] == "5":
		eqs.append(row)

selectedEqs = sorted(eqs, key=itemgetter(4), reverse=True)[:5]

orgEq = []
orgEms = []

for eq in selectedEqs:
	eqData = {}
	
	eqDate = datetime.datetime.strptime(eq[0], "%Y-%m-%dT%H:%M:%S.%fZ")
	eqNextDayDate = eqDate + datetime.timedelta(days=1)
	
	eqData["date"] = eqDate.strftime("%d-%b-%Y")
	eqData["lat"] = eq[1]
	eqData["long"] = eq[2]
	eqData["mag"] = eq[4]
	
	print(eqData)
	
	orgEq.append(eqData)
	
	emsTotal = {}
	
	for ems in emsData:
		emsDate = datetime.datetime.strptime(ems[0], "%d-%b-%y")
		
		if emsDate.date() == eqDate.date() or emsDate.date() == eqNextDayDate.date():
			if ems[1] in zipToCounty.keys():	
				county = zipToCounty[ems[1]].upper()

				if county not in emsTotal.keys():
					emsTotal[county] = 0
				emsTotal[county] += 1

	emsMin = 10000
	emsMax = -1
	
	for k, v in emsTotal.items():
		if v < emsMin:
			emsMin = v 
		if v > emsMax:
			emsMax = v
	
	for k, v in emsTotal.items():
		binIndex = np.digitize(v, [1, 5, 15, 20, 25, 50, 75, 100, 500])
		emsTotal[k] = {"fillKey": str(binIndex), "total": v}
		
	orgEms.append(emsTotal)

#print(orgEms)
with open('../data/earthquakeTest.json', 'w') as outfile:
	outfile.write("countyColors = '")
	json.dump(orgEms, outfile)
	outfile.write("'\n")
	
	outfile.write("earthquakes = '")
	json.dump(orgEq, outfile)
	outfile.write("'\n")