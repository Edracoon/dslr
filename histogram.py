# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   histogram.py displays a histogram answering the next question :
#
#   Which Hogwarts course has a homogeneous score distribution between all four houses ?
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import matplotlib.pyplot as plt
from utils import *

csvFile = parseCSV('./datasets/dataset_train.csv')
# print(csvFile[:][:])
Hufflepuff, Gryffindor, Slytherin, Ravenclaw = getGradesByHouse(csvFile, 'Arithmancy')
plt.hist(Hufflepuff, color='red')
plt.hist(Gryffindor, color='blue')
plt.hist(Slytherin, color='green')
plt.hist(Ravenclaw, color='yellow')
plt.show()