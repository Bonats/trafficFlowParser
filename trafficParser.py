import json

trafficData = ''
streetChoice = ''
finalTime = ''

def parseFile(fileName, northOrSouth,address):

    #getting the date
    tempDate = fileName.split('-')
    year = tempDate[2][0:4]
    month = tempDate[2][4:6]
    day = tempDate[2][6:8]
    finalDate = month+'/'+day+'/'+year

    with open('./mmda-traffic-scrapped/out/'+fileName) as f:
        trafficData = json.load(f)

    for data in range(len(trafficData)):
        if northOrSouth is 'northbound' and address in trafficData[data].get('line'):
            status = trafficData[data].get('northbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
            timePosted = trafficData[data].get('northbound').get('time_updated').replace('am','')
            if 'pm' in timePosted:
                tempTime = timePosted.replace('pm','').split(':')
                getHour = int(tempTime[0]) + 12
                finalTime = finalDate + ' ' + str(getHour) + ':' + tempTime[1]
            else:
                finalTime = finalDate + ' ' + timePosted

            tempData = [finalTime,status,'1','100']
            return tempData

        # if direction is south
        elif northOrSouth is 'southbound':
            status = trafficData[data].get('southbound').get('status').replace('light','25').replace('mod','50').replace('heavy','75')
            timePosted = trafficData[data].get('southbound').get('time_updated').replace(' am','')
            if 'pm' in timePosted:
                tempTime = timePosted.replace(' pm','').split(':')
                getHour = int(tempTime[0]) + 12
                finalTime = finalDate + ' ' + str(getHour) + ':' + tempTime[1]
            else:
                finalTime = finalDate + ' ' + timePosted

            tempData = [finalTime,status,'1','100']
            return tempData
    
    

def getAddress(fileName,streetName):
    address = []

    with open('./mmda-traffic-scrapped/out/'+fileName) as f:
        trafficData = json.load(f)

    for x in range(len(trafficData)):
        sStreet = trafficData[x].get('line').split(' ')
        if streetName in sStreet[0]:
            address.append(trafficData[x].get('line'))

    return address