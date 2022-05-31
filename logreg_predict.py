# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   It takes as a parameter dataset_test.csv and a file containing the weights trained by previous program.
#   In order to evaluate the performance of your classifier this second program will have
#   to generate a prediction file houses.csv formatted exactly as follows:
#
#   Index,Hogwarts House
#   0,Gryffindor
#   1,Hufflepuff
#   2,Ravenclaw
#   3,Hufflepuff
#   4,Slytherin
#   5,Ravenclaw
#   6,Hufflepuff
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
import pandas as pd
import numpy as np
from LogisticRegression import *

INT_MIN     = -1 * (2 ** 16)
house_dictio = {
        0: 'Ravenclaw',
        1: 'Slytherin',
        2: 'Gryffindor',
        3: 'Hufflepuff'
        }

print('Usage: python3 logreg_predic.py dataset_test.csv')

def sigmoid(x):
    return (1.0 / (1.0 + np.exp(-x)))

def multiClassifier(X, weights, bias):
    n_samples, n_features = X.shape
    
    X = standardize(X)
    
    allPred = []
    for i in range(len(weights)):
        allPred.append(sigmoid(np.dot(X, weights[i]) + bias[i]))
    allPred[0] = allPred[0].reshape(allPred[0].shape[0])
    allPred[1] = allPred[1].reshape(allPred[1].shape[0])
    allPred[2] = allPred[2].reshape(allPred[2].shape[0])
    allPred[3] = allPred[3].reshape(allPred[3].shape[0])
    
    # Choose the best house for all samples
    bestHouses = []
    for index in range(n_samples):
        BestHouse = 0 # Start at Ravenclaw
        for house in range(len(allPred)):
            if allPred[house][index] > allPred[BestHouse][index]:
                BestHouse = house
        bestHouses.append(BestHouse)
            
    return bestHouses

def parseDataTest():
    if (len(sys.argv) < 2):
        print('Error: Need a dataset_test as argument')
        exit(1)
    else:
        fileName = sys.argv[1]
    try:
        X = pd.read_csv(fileName)
    except:
        print('Error: Invalid file or do not exists')
        exit(1)

    X = X.select_dtypes('float')
    X = X.drop('Hogwarts House', axis=1)
    return X

def parseWeigths():
    try:
        file = open('weights.save')
    except:
        print('Error: weights.save do not exist, you have to train in order to predict')
        exit(1)

    lines = file.read().split('\n')
    
    weights = []
    bias = []
    for line in lines:
        try:
            attrib, values = line.split(' ')
        except:
            continue
        if (attrib == 'Weights'):
            vals = values.split(',')
            weights.append(np.array([float(val) for val in vals]))
        if (attrib == 'Bias'):
            bias.append(float(values))
    
    # Reshape our weight so it supports np.dot as we want
    for i in range(len(weights)):
        weights[i] = weights[i].reshape(13, 1)
    return weights, bias


def main():

    X = parseDataTest()
    weights, bias = parseWeigths()
    
    n_samples, n_features = X.shape
    
    bestHouses = multiClassifier(X, weights, bias)
    file = open('houses.csv', 'w')
    file.write('Index,Hogwarts House\n')
    for index in range(len(bestHouses)):
        choosenHouse = house_dictio[bestHouses[index]]
        file.write(f'{index},{choosenHouse}\n')
    
    file.close()
    return 0
    
main()