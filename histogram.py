# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   histogram.py displays a histogram answering the next question :
#
#   Which Hogwarts course has a homogeneous score distribution between all four houses ?
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
import matplotlib.pyplot as plt
from utils import *
from ft_math import *

seeAll = False
seeDiff = False
if (len(sys.argv) > 1 and sys.argv[1] == '-see-all'):
    seeAll = True
if (len(sys.argv) > 1 and sys.argv[1] == '-see-diff'):
    seeDiff = True

print('Usage: histogram.py [-see-all,-see-diff]\n')

csvFile = parseCSV('./datasets/dataset_train.csv')

def allHistograms():
    figure, axis = plt.subplots(4, 4)
    i = 0
    for y in range(4):
        for x in range(4):
            if i >= len(courses):
                break
            Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, courses[i], noZero=True)
            axis[y, x].set_title(courses[i])
            axis[y, x].hist(Hufflepuff, color='red', alpha=0.3)
            axis[y, x].hist(Gryffindor, color='blue', alpha=0.3)
            axis[y, x].hist(Slytherin, color='green', alpha=0.3)
            axis[y, x].hist(Ravenclaw, color='yellow', alpha=0.3)
            i += 1
    plt.show()

def HomogeneousDiff(course):
    Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, course, noZero=True)
    tab = [Hufflepuff, Gryffindor, Slytherin, Ravenclaw]
    means = []
    for house in tab:
        minmax = ft_minmax(house)
        data = ft_normalize(house, minmax)
        means.append(ft_mean(data))
    glob_mean = ft_mean(means)
    diff = 0
    for i in range(len(means)):
        diff += abs(means[i] - glob_mean)
    return round(diff, 4)

if (seeDiff):
    print('Houses Names |'.rjust(31), 'Homogeneous Diff'.ljust(31))
    print('------------------------------|---------------------')
    for course in courses:
       print((course + ' |').rjust(31), HomogeneousDiff(course))

if (seeAll):
    allHistograms()
else:
    Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, 'Care of Magical Creatures', noZero=True)
    plt.hist(Hufflepuff, color='red', alpha=0.3)
    plt.hist(Gryffindor, color='blue', alpha=0.3)
    plt.hist(Slytherin, color='green', alpha=0.3)
    plt.hist(Ravenclaw, color='yellow', alpha=0.3)
    plt.title('Care of Magical Creatures')
    plt.xlabel('Grades')
    plt.ylabel('Nb Students')
    plt.show()