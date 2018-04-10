# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
CS299
HW1
@author: Joanna Cao
"""
#import math
import statistics
import numpy as np
from functools import reduce #imported reduce for use in summaryStatistics function

"""Given two list of numbers that are already sorted, 
return a single merged list in sorted order.
"""
def merge(sortedListA, sortedListB):
   
    sortedList = sortedListA + sortedListB #concatenated the argument lists
    sortedList.sort(); #sorted the original list

    return sortedList #returns the final sorted list

"""Givne a list of numbers in random order, return the summary statistics 
that includes the max, min, mean, population standard deviation, median,
75 percentile, and 25 percentile.
"""    
def summaryStatistics(listOfNums):
    
    maxVal = reduce(lambda a,b: max(a,b), listOfNums) #calculates the max
    minVal = reduce(lambda a,b: min(a,b), listOfNums) #calculates the min
    meanVal = statistics.mean(listOfNums) #calculates the mean using statistics.mean function
    stdev = statistics.stdev(listOfNums) #calculates standard deviation using statistics.stdev
    median = statistics.median(listOfNums) #calculates median
    npArray = np.array(listOfNums) #converts argument list into a numpy array
    perc75 = np.percentile(npArray, 75) #calculates 75th percentile of numpy array
    perc25 = np.percentile(npArray, 25) #calculates 25th percentile of numpy array
    
    # You can decide to return the following statistics either in a sequence 
    # type (i.e., list, tuple), or a key-value pair (i.e., dictionary)
    return {'max': maxVal, #returns all of the values
            'min': minVal, 
            'mean': meanVal, 
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}
    

"""Given a list of real numbers in any range, scale them to be 
between 0 and 1 (inclusive). For each number x in the list, the new number 
is computed with the formula round((x - min)/(max - min)) where max is the 
maximum value of the original list and min is the minimum value of the list. 
"""	
def scaleToDigits(listOfNums):
    minVal = reduce(lambda a,b: min(a,b), listOfNums)
    maxVal = reduce(lambda a,b: max(a,b), listOfNums)
    newList = []; 
    for i in range(len(listOfNums)): 
        newValue = round((listOfNums[i] - minVal)/(maxVal - minVal),3)
        newList.append(newValue)
    return newList

