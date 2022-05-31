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
import math
from LogisticRegression import *

print('Usage: python3 logreg_train.py dataset_train.csv [-accuracy]')

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

def storeParameters(house, W, B, file):
    file.write(f"{house}:\n")
    file.write('Weights ')
    for i in range(len(W)):
        if i == len(W) - 1:
            file.write(f'{W[i][0]}')
        else:
            file.write(f'{W[i][0]},')
    file.write(f'\nBias {B}\n')

def main():
    # Load csv and fill our real values (1 or 0)
    try:
        X = pd.read_csv(fileName)
    except:
        print('Error: Invalid file or do not exists')
        exit(1)
    Y1 = np.array([1 if X['Hogwarts House'][i] == 'Ravenclaw' else 0 for i in range(X.shape[0])])
    Y2 = np.array([1 if X['Hogwarts House'][i] == 'Slytherin' else 0 for i in range(X.shape[0])])
    Y3 = np.array([1 if X['Hogwarts House'][i] == 'Gryffindor' else 0 for i in range(X.shape[0])])
    Y4 = np.array([1 if X['Hogwarts House'][i] == 'Hufflepuff' else 0 for i in range(X.shape[0])])
    X = X.select_dtypes('float')
    
    # Standardize our inputs avoiding scaling problem and optimum problem
    X = standardize(X)

    # Initialize Logistic Regression class
    LogReg = LogisticRegression()

    file = open("weights.save", "w")

    # Train and store weights and bias
    W, B, pred1 = LogReg.train(X, Y1)
    storeParameters('Ravenclaw', W, B, file)

    W, B, pred2 = LogReg.train(X, Y2)
    storeParameters('Slytherin', W, B, file)

    W, B, pred3 = LogReg.train(X, Y3)
    storeParameters('Gryffindor', W, B, file)

    W, B, pred4 = LogReg.train(X, Y4)
    storeParameters('Hufflepuff', W, B, file)

    file.close()

    if accuracy == True:
        classif1 = LogReg.classificate(pred1)
        classif2 = LogReg.classificate(pred2)
        classif3 = LogReg.classificate(pred3)
        classif4 = LogReg.classificate(pred4)
        print(f"For Ravenclaw  : {precision(Y1, classif1)}" + "%" + " of accuracy classification")
        print(f"For Slytherin  : {precision(Y2, classif2)}" + "%" + " of accuracy classification")
        print(f"For Gryffindor : {precision(Y3, classif3)}" + "%" + " of accuracy classification")
        print(f"For Hufflepuff : {precision(Y4, classif4)}" + "%" + " of accuracy classification")

main()