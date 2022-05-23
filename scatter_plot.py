# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   scatter_plot.py displays a scatter plot answering the next question :
#
#   What are the two features that are similar ?
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
import matplotlib.pyplot as plt
from utils import *
from ft_math import *

csvFile = parseCSV('./datasets/dataset_train.csv')

def scatter_plot():
    HufflepuffX, GryffindorX, SlytherinX, RavenclawX = getGradesByHouse(csvFile, 'Astronomy', noZero=False)
    HufflepuffY, GryffindorY, SlytherinY, RavenclawY = getGradesByHouse(csvFile, 'Defense Against the Dark Arts', noZero=False)
    plt.scatter(HufflepuffX, HufflepuffY, s=10, color='red', alpha=1)
    plt.scatter(GryffindorX, GryffindorY, s=10, color='blue', alpha=0.2)
    plt.scatter(RavenclawX, RavenclawY, s=10, color='yellow', alpha=1)
    plt.scatter(SlytherinX, SlytherinY, s=10, color='green', alpha=0.2)
    plt.xlabel('Astronomy')
    plt.ylabel('Defense Against the Dark Arts')
    plt.show()

scatter_plot()