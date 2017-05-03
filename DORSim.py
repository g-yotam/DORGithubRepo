import pandas as pd
import os
import numpy as np
import random

#todo historic call center data, current call center data


wage = input("Enter the Wage:") #$13.27
historicCalls = input("Enter the amount of historic calls:")
currentCalls = input("Enter the amount of current calls:")
print "\n"
# month = input("Enter the month (format as number from 1 to 12): ")

oldweightedAM = []
oldcitizen = (5832 + 5823 + 5930)
oldcommercial = (1298 + 787 + 903)
#no data available on the county so taken from abandoned calls
oldcounty = 639
oldtotalNumberOfCalls = oldcitizen + oldcommercial + oldcounty

oldcitizenWeight = int(float(oldcitizen) / historicCalls * 100)
oldcommercialWeight = int(float(oldcommercial) / historicCalls * 100)
oldcountyWeight = int(float(oldcounty) / historicCalls * 100)

newWeightedAM = []
newCountyWeight = oldcountyWeight
newCitizen = (6568 + 6078 +  5884)
newCommercial = (1061 + 696 + 540)
newTotalNumberOfCalls = oldcounty+ newCitizen + newCommercial
newCitizenWeight = int(float(newCitizen) / newTotalNumberOfCalls * 100)
newCommercialWeight = int(float(newCitizen) / newTotalNumberOfCalls * 100)
newCountyWeight = int(float(oldcounty) / newTotalNumberOfCalls * 100)

#puts in the proper values for array
index = 0
for i in range(0,oldcitizenWeight):
    oldweightedAM.append(0)
for j in range(0,oldcommercialWeight):
    oldweightedAM.append(1)
for k in range(0,oldcountyWeight):
    oldweightedAM.append(2)

for l in range(0,newCitizenWeight):
    newWeightedAM.append(0)
for m in range(0,newCommercial):
    newWeightedAM.append(1)
for n in range(0,newCountyWeight):
    newWeightedAM.append(2)

#determines how long a call is with probability of getting a type of call

avgWaitMVDCitizen = 23.5
avgWaitMVDCommVeh = 8
avgWaitCounty = 8.5

timePerCall = [avgWaitMVDCitizen, avgWaitMVDCommVeh, avgWaitCounty]

#file = "Monthly.xlsx"
#print os.path.abspath(file) #finds file path. must put in pycharms folder

#reads and cleans file
#x1 = pd.ExcelFile("/Users/ETheReal/PycharmProjects/DORSim/Monthly.xlsx")
#df = x1.parse()

# callsRemaining = 15000
tShift = 8.5 * 60  #8am - 4:30pm
# timeRemaining = tShift
# callsAbandoned = 0
totalTime = 0
for c in range(0, historicCalls):
    wamIndex = random.randrange(0, len(oldweightedAM))
    timeIndex = oldweightedAM[wamIndex]
    totalTime += timePerCall[timeIndex]

dollarPerMin = float(wage) / 60
totalExpenses = dollarPerMin * totalTime

newTotalTime = 0
for d in range(0, currentCalls):
    wamIndex = random.randrange(0, len(newWeightedAM))
    timeIndex = newWeightedAM[wamIndex]
    newTotalTime += timePerCall[timeIndex]

newTotalExpenses = dollarPerMin * newTotalTime

# while(timeRemaining > 0 and callsRemaining > 0): #simulates a workday
#     index = random.randrange(3)
#     #print index
#     timeRemaining -= timePerCall[index]
#     if index == 1:
#         callsRemaining -= 639
#         callsAbandoned += 639
#     callsRemaining -= numWorkers
# print "Total expenses: " + str(wage * numWorkers * (tShift - timeRemaining)/60)
# print "Calls Remaining: " + str(callsRemaining)
# print "Calls solved: " + str(totalCalls - callsRemaining)
# print "Calls Abandoned: " + str(callsAbandoned)

print "Total expenses for Historic Calls:" + ("%.2f" % round(totalExpenses,2))
print "old Amount per call:" + ("%.2f" % round(totalExpenses/historicCalls,2) + "\n")


print "Total expenses for Historic Calls:" + ("%.2f" % round(newTotalExpenses,2))
print "new Amount per call:" + ("%.2f" % round(totalExpenses/currentCalls,2) + "\n")
saved = totalExpenses - newTotalExpenses

print "Total amount saved:" + str(saved)
print "Total amount saved per call:" + ("%.2f" % round(saved/((currentCalls + historicCalls)/2),2))