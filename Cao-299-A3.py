# -*- coding: utf-8 -*-
"""
CS 299
HW3
@author: Joanna Cao

"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from xml.dom import minidom #used to create the xml_dict
from collections import OrderedDict #used to create the ticker list

def ticker_find(xml_dict, ticker): 
    return xml_dict[ticker]['name'] #returns the name found at the ticker key in xml_dict
 
def calc_avg_open(csv_data, ticker):
    sum = 0;  #initializes sum to 0
    df = csv_data[csv_data['Symbol'] == ticker] #creates a dataframe df consisting only of data with the ticker in the arg
    openingPriceList = list(df['Open']) #creates a list of data in the column "Open" in df
    for i in openingPriceList:
        sum += i #increments each value in this list to sum
    return sum / (len(openingPriceList)) #divides sum by the number of "Open" values to get avg open value

def vwap(stock_dict, ticker):
    df = stock_dict[stock_dict['Symbol'] == ticker] #creates dataframe consisting only of information correlating with the ticker 
    
    high = list(df['High']) #creates a list 'high' consisting of the values in df's column 'High'
    low = list(df['Low']) #creates a list 'low' consisting of values from df's column 'Low'
    close = list(df['Close']) #creates a list 'close' consisting of values from df's column 'Close'
    volume = list(df['Volume']) #creates a list 'volumn' consisting of values from df's column 'Volumn'
    
    totalVolume = 0; #initializes totalVolume to 0
    sum = 0; #initializes sum to 0
    volumeIndex = 0; #initializes volumeIndex of 0 (iterates through volume)
    
    while volumeIndex < len(volume):
        totalVolume += volume[volumeIndex] #increments values of volume to the totalVolume
        volumeIndex += 1
        
    elem = 0
    while elem < len(df.index): #finds volume weighted average price
       dailyAvgPrice = (high[elem] + low[elem] + close[elem]) / 3 #finds daily average price using this formula
       sum += dailyAvgPrice * volume[elem] #increments sum with a calculation of the daily average price * the volume for that day
       elem += 1
       
    return (sum / totalVolume) #once the totalSum is divided by the total volume you have volume weighted average price

csv_data = pd.read_csv('SP500_ind.csv'); #reads the csv file into csv_data (dataframe)
xf = minidom.parse('SP500_symbols.xml'); #parses the xml file 

xml_dict = dict() #creates an empty dict called xml_dict
SP500_symbols = xf.getElementsByTagName('symbol') #can now use SP500_symbols to refer to a specific tag name in the xml

i = 0
while i < len(SP500_symbols): #iterates until there are no more symbols 
    subDict = dict() #creates an empty dict called subDict
    subDict['type'] = SP500_symbols[i].attributes['type'].value #a key 'type' is created and given the value of the 'type' attribute in that current symbol tag
    subDict['industry'] = SP500_symbols[i].attributes['industry'].value #a key 'industry' is created and given the value of the 'industry' attribute
    subDict['sector'] = SP500_symbols[i].attributes['sector'].value #a key 'sector' is created and given the value of the 'sector' attribute 
    subDict['name'] = SP500_symbols[i].attributes['name'].value #a key 'name' is created and given the value of the 'name' attribute
    ti = SP500_symbols[i].attributes['ticker'].value #variable ti is assigned the value of the ticker for that current symbol
    xml_dict[ti] = subDict.copy() #whatever value in ti is now used as a key in xml_dict, given a copy of subDict as its value
    i += 1
    #xml_dict now has tickers as keys which access a dictionary containing the rest of their information
    
symbol_list = csv_data['Symbol'] #creates a list 'symbol_list' consisting of all the values in the csv_data column 'Symbols'
ticker = list(set(symbol_list)) #creates a new list 'ticker', deleting all of the duplicate symbols

tickerIndex = 0; #used to iterate through the ticker list 
while tickerIndex < len(ticker): #assigns t to the value at the ticker[tickerIndex]
    t = ticker[tickerIndex]
    if t in xml_dict: #checks if the ticker in csv_data also shows up in xml
        print(ticker_find(xml_dict, t), calc_avg_open(csv_data, t), vwap(csv_data, t)) #print the name at that ticker
    else: 
        print("No data in SP500", calc_avg_open(csv_data, t), vwap(csv_data, t)) #prints the calculated open average and the volume weighted average price
    print("\n")
    tickerIndex += 1      
            
    
                
    