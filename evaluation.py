#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:06:46 2017

@author: 
    Md Enamul Haque 
"""
import numpy as np
import sys
    

def getIplusMax(relevance):
    #unique_elements, counts_elements = np.unique(relevance, return_counts=True)
    #iplusmax = counts_elements[0] * counts_elements[1]
    iplusmax = relevance.count('REL') * relevance.count('NREL')
    
    return iplusmax
    
def getIplus(relevance):

    iplus = 0
    for i in range(len(relevance)):
        if relevance[i] == 'REL':
            c = relevance[i+1:].count('NREL')
            iplus = iplus + c

    return iplus
    
def getIminus(relevance):
    
    iminus = 0
    for i in range(len(relevance)):
        if relevance[i] == 'NREL':
            c = relevance[i+1:].count('REL')
            iminus = iminus + c
        
    return iminus
    
    
def get_Rnorm(relevance):
    
    iplusmax = getIplusMax(relevance)
    iplus = getIplus(relevance)
    iminus = getIminus(relevance)
    print("I+: ", iplus)
    print("I-: ", iminus)
    print("I+ max: ", iplusmax)
    rnorm = 0.5 * (1 + ((iplus-iminus)/iplusmax))
    
    return rnorm
    
    
if __name__ == "__main__":
    global D
    
    doclist = [2,4,8,9,10]
    rel_list = ['REL','REL','NREL','REL','NREL']

    D = np.array([
                  [0,2,0,2],
                  [2,3,1,0],
                  [0,1,1,0],
                  [1,2,0,0],
                  [1,3,2,1]
                  ])
    SP = 1
    GP = 0
    GPLS = 1
    Roch = 0
    
    
    if (SP+GP+GPLS+Roch) != 1:
        print('\033[1;38mLogical error!!\033[1;m')
        print("Please select single method and try again!\n\n")
        sys.exit()
    
    
    if SP == 1:
        # standard perceptron
        method = 'Standard perceptron'
        q = np.array([9,5,-11,-4])
        #q = np.array([ -3,   8, -11,  -7])
    
    if GP == 1:
        # generalized perceptron
        method = 'Generalized perceptron'
        q = np.array([4,1,-5,-4])
    
    if GPLS == 1:
        # generalized perceptron - learning by sample
        method = 'Generalized perceptron - learning by sample'
        q = np.array([1,-1,-1,2])
        
    if Roch == 1:
        # Rocchio's method
        method = 'Rocchio\'s method'
        q = np.array([0.21, 0.19, -0.23, 0.0])
    
    RSV = np.matmul(D, q.transpose())
    # sort RSV in descending order and get the indices
    order = np.flipud(np.argsort(RSV))
    
    print("Result for "+str(method))
    print("------------------------------------")
    print("Optimal Query: ", q)
    print("RSV:", RSV)
    print("Document ranking:")
    FIN_DLIST = []
    for k in range(len(doclist)):
        FIN_DLIST.append("d"+str(doclist[order[k]]))
    print(FIN_DLIST)
    
    print("Relevance ranking:")
    FIN_LIST = []
    for k in range(len(doclist)):
        FIN_LIST.append(rel_list[order[k]])
    print(FIN_LIST)
    
    Rnorm = round(get_Rnorm(FIN_LIST), 2)
    
    print("Rnorm: ", Rnorm)
