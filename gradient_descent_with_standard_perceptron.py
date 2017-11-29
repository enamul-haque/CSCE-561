#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:06:46 2017

@author: 
    Md Enamul Haque

Desc:  
    The order is: d1, d3, d5, d6, d7 in the D matrix.
    d6 and d7 are negated due to the non-relevancy.
    Mapping in the Yset: 0-->d1, 1-->d3, 2-->d5, 3-->d6, 4-->d7
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

import numpy as np

def get_yset(DQ):
    yset = list()
    for i in range(len(DQ)):
        if DQ[i] <= 0:
            yset.append(i)
        
    return yset
    
def update_q(q, yset):
    l = len(yset)
    Dvec = np.array(D.shape[1] * [0])
    if l>0:
        for i in yset:
            Dvec = Dvec + D[i]
    q = q + Dvec

    return q
    
if __name__ == "__main__":
    print(__doc__)
    
    iteration_count = 500
    empty = "\u03a6"
    global D
    
    D = np.array([
                  [0,2,0,2],
                  [1,3,0,0],
                  [1,3,1,0],
                  [0,-2,-1,-1],
                  [0,-3,-1,-2]
                  ])

#    D = np.array([
#              [0,2,0,2],
#              [1,3,1,0],
#              [0,-3,-1,-2], 
#              [1,3,0,0],
#              [0,-2,-1,-1]
#              ])
        

#    D = np.array([
#              [0,-1,-1,0],
#              [0,0,-1,1],
#              [1,0,0,-2],
#              [1,1,0,-1],
#              [1,0,-1,-2],
#              [1,1,-1,-1]
#              ])

    #q = np.array(D.shape[1] * [0])
    q = np.array([-10, -10, -10, -10])
    for iteration in range(iteration_count):
        
        print("At iteration: \t"+str(iteration))
        print("Query: \t\t", q)
        
        DQ = np.matmul(D, q.transpose())
        print("D alpha Q: \t", DQ)
        
        # stopping criteria
        if (sum(DQ>0) == D.shape[0]):
            print("*************************************")
            print("Converged at iteration: \t", iteration)
            print("Optimum query: \t", q)
            print("D alpha Q: \t", DQ)
            print("Yset: \t\t", empty)
            print("*************************************")
            break
        
        # get set of non-relevant docs
        setY = get_yset(DQ)
        # update query
        q = update_q(q, setY)

        print("Yset: \t\t", setY)
        print("-----------------------------------------")