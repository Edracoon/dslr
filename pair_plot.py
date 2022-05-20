# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   pait_plot.py displays a pair plot or scatter plot matrix (according to the library).
#
#   From this visualization, what features are you going to use for your logistic regression ?
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
import matplotlib.pyplot as plt
from utils import *
from ft_math import *

csvFile = parseCSV('./datasets/dataset_train.csv')
figure, axis = plt.subplots(13, 13)

for y in range(13):
    i = 0
    for x in range(13):
        if i >= len(courses):
            break
        Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, courses[i])
        Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, courses[i])
        tab = [Hufflepuff, Gryffindor, Slytherin, Ravenclaw]
        axis[y][x].scatter(tab, color='red', alpha=0.3)
        i += 1
        
