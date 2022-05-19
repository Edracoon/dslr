INDEX = 0
HOUSE = 1
FIRSTNAME = 2
LASTNAME = 3
BIRTHDAY = 4
BESTHAND = 5

ARITHMANCY = 0
ASTRONOMY = 1
HERBOLOGY = 2
DEFENSE = 3
DIVINATION = 4
MUGGLE = 5
ANCIENT = 6
HISTORY = 7
TRANSFIG = 8
POTIONS = 9
CARE = 10
CHARMS = 11
FLYING = 12
N_FEATS = 13  # Number numbered features

def parseCSV(fileName):
    lines = []
    try:
        file = open(fileName, 'r')
        lines = file.read().split('\n')
    except:
        print('Error: Invalid file or do not exists')
        return
    csvFile = []
    for line in lines:
        csvFile.append(line.split(','))
    return csvFile

def fillMissingData(features, means):
    for col in range(len(features)):
        for row in range(len(features[col])):
            if features[col][row] == 0.0:
                features[col][row] = means[col]

def fillDataContainers(csvFile):
    numericData = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    stringData = [[], [], [], [], [], []]
    # === Store data in float values === #
    for row in range(len(csvFile)):
        if row > 0:
            for col in range(len(csvFile[row])):
                if col >= 6 and csvFile[row][col] != '':
                    numericData[col - 6].append(float(csvFile[row][col]))
    # === Store data in string values === #
    for row in range(len(csvFile)):
        if row > 0:
            for col in range(len(csvFile[row]) - 13):
                stringData[col].append(csvFile[row][col])
    return numericData, stringData