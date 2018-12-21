from cInput import strInput
from statistics import mode
import re


class Guard:
    def __init__(self, id):
        self.id = id
        self.minutesSlept = []
        self.totalSlept = 0
        self.mostFrequentMinute = 0
    lastAsleep = 0

    def addMinute(self, minute):
        self.minutesSlept.append(minute)
        self.totalSlept += 1
    
    def getMostFrequentMinute(self):
        minutes = self.minutesSlept

        return mode(minutes)

#==================================================

strInput = strInput.split("\n")
del strInput[0]
strInput.sort()
guardDict = {}
#This is to allow me to reference the guard 'currently' on duty
currentGuard = Guard(0)

#getting the start of each guard's shift to break it up
for line in strInput:
    validID = re.search("(#[0-9]{1,4}?)\W", line)
    if (validID):
        id = validID.group(0)
        if id not in guardDict:
            guardDict[id] = Guard(id)
        
        currentGuard = guardDict.get(id)
        minutes = currentGuard.minutesSlept
        if id not in guardDict:
            guardDict[id] = currentGuard

    asleep = re.search("asleep", line)
    woke = re.search("wakes", line)
    rawTime = re.search("(:[0-9]{1,2}?)\W", line)
    if (asleep or woke): 
        time = int(rawTime.group(0)[1] + rawTime.group(0)[2])

    if (asleep):
        currentGuard.lastAsleep = time

    if (woke):
        start = currentGuard.lastAsleep
        end = time

        for i in range(start, end):
            currentGuard.addMinute(i)

mostSlept = Guard(0)

for guard in guardDict:
    cGuard = guardDict.get(guard)
    if (cGuard.totalSlept > mostSlept.totalSlept):
        mostSlept = cGuard
    

freqMinute = mostSlept.getMostFrequentMinute()
strId = mostSlept.id
strId = strId.strip()
strId = strId.replace('#','')
selectedGuardID = int(strId)

print(freqMinute * int(strId))

 

