# -*- coding: utf-8 -*-
"""
CS299
HW2
@author: Joanna Cao
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import random
from functools import reduce
import statistics
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import collections

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
    
def scaleToDigits(listOfNums):
    minVal = reduce(lambda a,b: min(a,b), listOfNums) #finds the min 
    maxVal = reduce(lambda a,b: max(a,b), listOfNums) #finds the max
    newList = []; #creates empty list
    for i in range(len(listOfNums)): #for each item in the list
        newValue = (round((listOfNums[i] - minVal)/(maxVal - minVal),2))*9 
        #complete the formula, THEN multiply by 9 to scale it to [0,9]
        newList.append(int(newValue)) #add to the empty list
    return newList
#QUESTION 2

#creates 3 datasets of 100 random numbers from 0 to 100
list1 = [np.random.randint(0,101) for i in range(100)] 
list2 = [np.random.randint(0,101) for i in range(100)]
list3 = [np.random.randint(0,101) for i in range(100)]

#incorporates the STATISTICS of these lists into a dataframe
df = DataFrame({'data 1' : summaryStatistics(list1),
                'data 2' : summaryStatistics(list2),
                'data 3' : summaryStatistics(list3)})
df = df.T #transpose the frame to make the desired plot
fig = df.plot(xticks=range(3), style=['r+','cx','gv','rx','g>','b<', 'y^'], title='Summary of Statistics')
#draws up the plot with 3 xticks, the specified styles, and the title of the plot
#default kind of plot is line
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,3,1,6,2,4,5]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order], bbox_to_anchor=(1,1), loc=2) 
#the above adds legend to the top right corner outside the plot
#also specifies the column order in the legend
fig.set_ylabel('Values') #sets the y label as Values
#QUESTION 3

#scales the lists list1,list2,list3 and then counters the number of 
#occurrences of each number in a dictionary. These dictionaries are
#then stored into a dataframe
df2 = DataFrame({'data 1' : collections.Counter(scaleToDigits(list1)),
                 'data 2' : collections.Counter(scaleToDigits(list2)),
                 'data 3' : collections.Counter(scaleToDigits(list3))})
#draws up a line plot with 10 xticks, specified styles, and title
fig2 = df2.plot(xticks=range(10),style=['r+-','gx-','b*-'], title='Frequency of Dataset')
plt.legend(bbox_to_anchor=(1,1), loc=2) #changes location of legend
fig2.set_xlabel('Values') #makes x label as Values
fig2.set_ylabel('Frequency') #makes y label as Frequency 






