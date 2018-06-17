import os
import json
import trafficParser
import saveCsvFile

mmdaTrafficFiles = []
streetName = ['QUEZON AVE','ORTIGAS','ESPAA','C5','EDSA','SLEX','COMMONWEALTH','ROXAS BLVD','MARCOS HIGHWAY']
northOrSouth = ''

# getting files from the directory of .json
for files in os.listdir('./mmda-traffic-scrapped/out'):
    if files.endswith(".json"):
        mmdaTrafficFiles.append(files)

# getting direction whether north or south
while True:
    northOrSouth = input('n = northbound / s = southbound: ')
    if 'n' in northOrSouth:
        northOrSouth = 'northbound'
        break
    elif 's' in northOrSouth:
        northOrSouth = 'southbound'
        break
    else:
        print('Invalid Input')

for sName in range(len(streetName)):
    print(sName+1,'-'+streetName[sName])

# getting specific street
while True:
    try:
        streetChoice = int(input('Enter Road[1-9]: '))
        if(streetChoice > 9):
            print('Invalid Input')
        elif(streetChoice < 1):
            print('Invalid Input')
        else:
            break
    except:
        print('Invalid Input!')

tempAdd = []
# getting address
for count in range(len(mmdaTrafficFiles)):
    with open('./mmda-traffic-scrapped/out/'+mmdaTrafficFiles[count],"r") as f:
        if f.mode == "r":
            contents = f.read()
            if contents:
                tempStreet = streetName[streetChoice-1].replace(" AVE","").replace(" BLVD","").replace(" HIGHWAY","")
                tempAdd.append(trafficParser.getAddress(mmdaTrafficFiles[count],tempStreet))

# merging list of address
myListAddress = []
for x in range(len(tempAdd)):
    myListAddress = myListAddress + tempAdd[x]

# getting unique addresses
finalListAddress = list(set(myListAddress))

for x in range(len(finalListAddress)):
    print(x+1, '-',finalListAddress[x])

while True:
    try:
        roadChoice = int(input('Enter Street: '))
        if(roadChoice > len(finalListAddress)):
            print('Invalid Input')
            print(roadChoice)
        elif(roadChoice < 1):
            print('Invalid Input')
        else:
            break
    except:
        print('Invalid Input!')

csvHeader = ['5 Minutes','Lane 1 Flow (Veh/5 Minutes)','Lane Points','% Observed']
tempData = []
tempData.append(csvHeader)

# to be process for parsing
for count in range(len(mmdaTrafficFiles)):
    with open('./mmda-traffic-scrapped/out/'+mmdaTrafficFiles[count],"r") as f:
        if f.mode == 'r':
            contents = f.read()
            if contents:
                tempData.append(trafficParser.parseFile(mmdaTrafficFiles[count],northOrSouth,finalListAddress[roadChoice-1]))
            else:
                print('json object is empty')

saveCsvFile.saveFile(tempData,northOrSouth,finalListAddress[roadChoice-1].replace(' ','_').replace('.','').lower())
