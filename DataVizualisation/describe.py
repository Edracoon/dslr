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

if (len(sys.argv) < 2):
    print('Error: Need a dataset as argument')
    exit(1)

lines = []
try:
    file = open('../datasets/dataset_train', 'r')
    lines = file.read()
except:
    print('Error: Invalid file or do not exists')

print(lines)