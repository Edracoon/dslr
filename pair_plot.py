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
plt.subplots_adjust(wspace=0.30, hspace=0.30)

def pair_plot():
    for y in range(13):
        for x in range(13):
            axis[y][x].tick_params(labelbottom=False)
            axis[y][x].tick_params(labelleft=False)
            if y != x:
                HufflepuffX, GryffindorX, SlytherinX, RavenclawX = getGradesByHouse(csvFile, courses[x], noZero=False)
                HufflepuffY, GryffindorY, SlytherinY, RavenclawY = getGradesByHouse(csvFile, courses[y], noZero=False)
                axis[y][x].scatter(HufflepuffX, HufflepuffY, s=1, color='red', alpha=0.3)
                axis[y][x].scatter(GryffindorX, GryffindorY, s=1, color='blue', alpha=0.3)
                axis[y][x].scatter(SlytherinX, SlytherinY, s=1, color='green', alpha=0.3)
                axis[y][x].scatter(RavenclawX, RavenclawY, s=1, color='yellow', alpha=0.3)
            else:
                Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, courses[y])
                axis[y][x].hist(Hufflepuff, color='red', alpha=0.5)
                axis[y][x].hist(Gryffindor, color='blue', alpha=0.5)
                axis[y][x].hist(Slytherin, color='green', alpha=0.5)
                axis[y][x].hist(Ravenclaw, color='yellow', alpha=0.5)
            if y == 12:
                axis[y][x].set_xlabel(courses[x].replace(' ', '\n'), fontsize=8)
                axis[y][x].tick_params(labelbottom=True)
            if x == 0:
                axis[y][x].set_ylabel(courses[y].replace(' ', '\n'), fontsize=8)
                axis[y][x].tick_params(labelleft=True)      
    plt.show()


pair_plot()