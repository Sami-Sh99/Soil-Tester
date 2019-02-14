
###################
#Predicts the best fit plant type for a given pH
###################
import numpy as np # linear algebra
def predict(pHval,Moist):
	results = []
	finalResults=[]
	with open('AcidityData.txt') as inputfile:
		#the file contains data in the following format: plantName (Min_Ph-Max_Ph-Avg_moisture)
	    for line in inputfile:
	        results.append(line.strip().split(','))


	for i in range(len(results)):
		get=results[i][0].split(' ')
		plant=get[0]
		firstVal=float(get[1][1:4])
		lastVal=float(get[1][5:8])
		Moisture=float(get[1][9:13])
		#print(Moisture)
		finalResults.append([plant,firstVal,lastVal,Moisture])
	finalResults=sorted(finalResults,key=lambda l:l[0], reverse=False)
	names=[]


	for i in finalResults:
		names.append(i[0])

	plants=[]

	for plant in finalResults:
		if(pHval >=plant[1] and pHval<=plant[2]):
			#print(plant)
			plants.append(finalResults[finalResults.index(plant)])
	Chosenplants=[]
	for Mplant in plants:
		if(abs(Mplant[3]-Moist)<7):
			print(abs(Mplant[3]-Moist))
			Chosenplants.append(Mplant)


	[print(x) for x in Chosenplants]
	return(Chosenplants)
predict(5.6,79.23)