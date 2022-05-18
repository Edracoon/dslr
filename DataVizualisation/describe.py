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
import sys

# Index,Hogwarts House,First Name,Last Name,Birthday,Best Hand,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,
# Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying
INDEX = 0
HOUSE = 1
FIRSTNAME = 2
LASTNAME = 3
BIRTHDAY = 4
BESTHAND = 5
ARITHMANCY = 6
ASTRONOMY = 7
HERBOLOGY = 8
DEFENSE = 9
DIVINATION = 10
MUGGLE = 11
ANCIENT = 12
HISTORY = 13
TRANSFIG = 14
POTIONS = 15
CARE = 16
CHARMS = 17
FLYING = 18
N_FEATS = 19  # Number of features


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
    everyone = []
    for line in lines:
        everyone.append(line.split(','))
    return everyone


def mean(feature):
    total = 0
    for i in range(len(feature)):
        if feature[i] != '':
            total += float(feature[i])
    return total / len(feature)


everyone = parseCSV()
features = [[], [], [], [], [], [], [],
            [], [], [], [], [], [],
            [], [], [], [], [], []]

for row in range(len(everyone)):
    if row > 0:
        for col in range(len(everyone[row])):
            features[col].append(everyone[row][col])

print(mean(features[DIVINATION]))
