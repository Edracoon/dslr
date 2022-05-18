# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# V1
#   This program will take a dataset as a parameter. All it has to do is to display information
#   for all numerical features like in the example:
#
#   python3 describe.py dataset_train.csv
#
#           Feature 1   Feature 2     Feature 3   Feature 4
#   Count   149.000000  149.000000    149.000000  149.000000
#   Mean      5.848322    3.051007      3.774497    1.205369
#   Std       5.906338    3.081445      4.162021    1.424286
#   Min       4.300000    2.000000      1.000000    0.100000
#   25%       5.100000    2.800000      1.600000    0.300000
#   50%       5.800000    3.000000      4.400000    1.300000
#   75%       6.400000    3.300000      5.100000    1.800000
#   Max       7.900000    4.400000      6.900000    2.500000
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import string
import sys
from xml.dom import INDEX_SIZE_ERR

# Index,Hogwarts House,First Name,Last Name,Birthday,Best Hand,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,
# Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying
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


def parseCSV():
    fileName = ''
    if (len(sys.argv) < 2):
        print('Error: Need a dataset as argument')
        exit(1)
    else:
        fileName = sys.argv[1]
    lines = []
    try:
        file = open(fileName, 'r')
        lines = file.read().split('\n')
    except:
        print('Error: Invalid file or do not exists')
    csvFile = []
    for line in lines:
        csvFile.append(line.split(','))
    return csvFile

def fillMissingData(features, means):
    for col in range(len(features)):
        for row in range(len(features[col])):
            if features[col][row] == 0.0:
                features[col][row] = means[col]

def fillDataContainers():
    numericData = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    stringData = [[], [], [], [], [], []]
    # === Store data in float values === #
    for row in range(len(csvFile)):
        if row > 0:
            for col in range(len(csvFile[row])):
                if col >= 6 and csvFile[row][col] != '':
                    numericData[col - 6].append(float(csvFile[row][col]))
                elif csvFile[row][col] == '':
                    numericData[col - 6].append(0)
    # === Store data in string values === #
    for row in range(len(csvFile)):
        if row > 0:
            for col in range(len(csvFile[row]) - 13):
                stringData[col].append(csvFile[row][col])
    return numericData, stringData


def getMinMax(features):
    minmax = []
    for i in range(len(features)):
        min_value = min(features[i])
        max_value = max(features[i])
        minmax.append([min_value, max_value])
    return minmax

def getNormalizeData(features, minimax):
    normalizedData = []
    for col in range(len(features)):
        normalizedCol = []
        for row in range(len(features[col])):
            norm = (features[col][row] - minimax[col][0]) / (minimax[col][1] - minimax[col][0])
            normalizedCol.append(norm)
        normalizedData.append(normalizedCol);
    return normalizedData

def getMeans(features):
    means = []
    for col in range(len(features)):
        total = 0
        for row in range(len(features[col])):
            total += float(features[col][row])
        means.append(total / len(features[col]))
    return means
        
csvFile = parseCSV()

numericData, stringData = fillDataContainers() # Filling our data tabs
means = getMeans(numericData) # Calculate means before filling missing data
fillMissingData(numericData, means)

minimax = getMinMax(numericData)
numericNormalized = getNormalizeData(numericData, minimax)
NormMeans = getMeans(numericNormalized) # Calculate means before filling missing data

print('means:')
print(means)
print('minimax:')
print(minimax)

def printDescribe():
    # === features === #
    print('\t Arithmancy\tAstronomy\tHerbology\tDADA\t\tDivination\tMuggle\t\tAncient\t\tHistory\t\tTransfig\tPotions\t\tCare\t\tCharms\t\tFlying')
    # === means === #
    line = ''
    for mean in means:
        line += str(round(mean, 6)) + ' \t'
    print('means\t', line)
    line = ''
    for mean in NormMeans:
        line += str(round(mean, 6)) + ' \t'
    print('norm\t', line)
    # === min max === #
    print()

# Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,
# Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying
printDescribe()
