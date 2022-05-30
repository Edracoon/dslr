# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   It takes as a parameter dataset_train.csv. You must use the
#   technique of gradient descent to minimize the error. The program generates a file
#   containing the weights that will be used for the prediction.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
import pandas as pd
import numpy as np
from LogisticRegression import LogisticRegression

fileName = ''
if (len(sys.argv) < 2):
    print('Error: Need a dataset as argument')
    exit(1)
else:
    fileName = sys.argv[1]

accuracy = False
if (len(sys.argv) > 2 and sys.argv[2] == '-accuracy'):
    accuracy = True

def precision(reals, preds):
    mean = 0
    for i in range(len(reals)):
        mean += abs(reals[i] - preds[i])
    percent = 100 - (mean / len(reals))
    return (round(percent, 4))

# Load csv and fill our real values (1 or 0)
X = pd.read_csv(fileName)
Y1 = np.array([1 if X['Hogwarts House'][i] == 'Ravenclaw' else 0 for i in range(X.shape[0])])
Y2 = np.array([1 if X['Hogwarts House'][i] == 'Slytherin' else 0 for i in range(X.shape[0])])
Y3 = np.array([1 if X['Hogwarts House'][i] == 'Gryffindor' else 0 for i in range(X.shape[0])])
Y4 = np.array([1 if X['Hogwarts House'][i] == 'Hufflepuff' else 0 for i in range(X.shape[0])])
X = X.select_dtypes('float')


file = open("weights.save", "w")

# Initialize Logistic Regression class
LogReg = LogisticRegression()
W, B, pred1 = LogReg.train(X, Y1)
file.write(f"{W} {B}")
class1 = LogReg.classificate(pred1)
W, B, pred2 = LogReg.train(X, Y2)
file.write(f"{W} {B}")
W, B, pred3 = LogReg.train(X, Y3)
file.write(f"{W} {B}")
W, B, pred4 = LogReg.train(X, Y4)
file.write(f"{W} {B}")

file.close()

print(f"For Ravenclaw  : {precision(Y1, class1)}" + "%" + " of accuracy classification")
print(f"For Slytherin  : {precision(Y2, pred2)}" + "%" + " of accuracy classification")
print(f"For Gryffindor : {precision(Y3, pred3)}" + "%" + " of accuracy classification")
print(f"For Hufflepuff : {precision(Y4, pred4)}" + "%" + " of accuracy classification")

