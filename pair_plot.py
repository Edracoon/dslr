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
    for x in range(13):
        for y in range(13):
            axis[x][y].tick_params(labelbottom=False)
            axis[x][y].tick_params(labelleft=False)
            if x != y:
                HufflepuffX, GryffindorX, SlytherinX, RavenclawX = getGradesByHouse(csvFile, courses[x])
                HufflepuffY, GryffindorY, SlytherinY, RavenclawY = getGradesByHouse(csvFile, courses[y])
                fillMissingData(HufflepuffX + GryffindorX + SlytherinX + RavenclawX, ft_mean(HufflepuffX + GryffindorX + SlytherinX + RavenclawX))
                fillMissingData(HufflepuffY + GryffindorY + SlytherinY + RavenclawY, ft_mean(HufflepuffY + GryffindorY + SlytherinY + RavenclawY))
                axis[x][y].scatter(HufflepuffY, HufflepuffX, s=0.7, color='red', alpha=0.8)
                axis[x][y].scatter(GryffindorY, GryffindorX, s=0.7, color='blue', alpha=0.6)
                axis[x][y].scatter(SlytherinY, SlytherinX, s=0.7, color='green', alpha=0.2)
                axis[x][y].scatter(RavenclawY, RavenclawX, s=0.7, color='yellow', alpha=0.1)
            else:
                Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, courses[x])
                axis[x][y].hist(Hufflepuff, color='red', alpha=0.3)
                axis[x][y].hist(Gryffindor, color='blue', alpha=0.3)
                axis[x][y].hist(Slytherin, color='green', alpha=0.3)
                axis[x][y].hist(Ravenclaw, color='yellow', alpha=0.3)
            if x == 12:
                axis[x][y].set_xlabel(courses[y].replace(' ', '\n'), fontsize=10)
                axis[x][y].tick_params(labelbottom=True)
            if y == 0:
                axis[x][y].set_ylabel(courses[x].replace(' ', '\n'), fontsize=10)
                axis[x][y].tick_params(labelleft=True)      
    plt.show()


pair_plot()