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
from utils import *
from ft_math import *

print('Usage: describe.py ./path/file.csv\n')

fileName = ''
if (len(sys.argv) < 2):
    print('Error: Need a dataset as argument')
    exit(1)
else:
    fileName = sys.argv[1]

csvFile = parseCSV(fileName)

def getMinMax(features): # Return a list of the min and the max of each column
    minmax = []
    for i in range(len(features)):
        minmax.append([min(features[i]), max(features[i])])
    return minmax

def getMeans(features): # Return a list of the mean of each column
    means = []
    for col in features:
        means.append( ft_mean(col) )
    return means

def getCoursesNames(csvFile): # Return a list of all courses names
    names = []
    for i in range(len(csvFile[0])):
        if i > 5:
            names.append((csvFile[0][i]).split(' ')[0])
    return names

def getCounts(numericData):
    counts = []
    for col in range(len(numericData)):
        counts.append(len(numericData[col]))
    return counts

def getPercentile(features): # Return a list of a the 25, 50, 75th percentile for each columns
    percentiles = []
    for col in range(len(features)):
        percentiles.append([ft_percentile(features[col], 25), ft_percentile(features[col], 50), ft_percentile(features[col], 75)])
    return percentiles

def getStandardDeviation(features, means): # Return a list of the standard deviation for each columns
    standardDeviations = []
    for col in range(len(features)):
        standardDeviations.append( ft_standard_deviation(features[col]) )
    return standardDeviations

def printDescribe():
    # ====== Features ====== #
    line = ''.rjust(17)
    for row in coursesNames:
        line += (row + "|").rjust(16)
    print(line)
    line = '                '
    for i in range(len(coursesNames)):
        line += '+---------------'
    print(line)
    # ====== Counts ====== #
    line = ''
    for count in counts:
        line += (str(round(count, 4)) + "|").rjust(16)
    print('Counts |'.rjust(16), line)
    # ====== Means ====== #
    line = ''
    for mean in means:
        line += (str(round(mean, 4)) + "|").rjust(16)
    print('Means |'.rjust(16), line)    
    # ======= STD ======= #
    line = ''
    for std in standardDeviations:
        line += (str(round(std, 4)) + "|").rjust(16)
    print('Std |'.rjust(16), line)
    # ======= Min ======= #
    min = ''
    max = ''
    for col in minimax:
        min += (str(round(col[0], 4)) + "|").rjust(16)
        max += (str(round(col[1], 4)) + "|").rjust(16)
    print('Min |'.rjust(16), min)
    # ====== Percentiles ====== #
    for i in range(3):
        line = ''
        for row in range(len(percentiles)):
            line += (str(round(percentiles[row][i], 4)) + "|").rjust(16)
        print(f'{(i+1) * 25}% |'.rjust(16), line)
    # ====== Max ====== #
    print('Max |'.rjust(16), max)


coursesNames = getCoursesNames(csvFile)
numericData, stringData = fillDataContainers(csvFile) # Filling our data tabs

counts = getCounts(numericData)
means = getMeans(numericData) # Calculate means after filling missing data
minimax = getMinMax(numericData)
standardDeviations = getStandardDeviation(numericData, means)
percentiles = getPercentile(numericData)

printDescribe()
