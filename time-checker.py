#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:14:43 2017

@author: polzak
"""

import time
import matplotlib.pyplot as plt


def rateChecker():
    diff_list = []
    ttime = 0
    rated = 0
    start = input("Start?")
    if start:
        print("Start!")
    stime = time.time()
    print(round(stime, 2))    
    while True:
        go = input("Oh yeah?")
        if go == 'q':
            break
        print("Got it!")
        tm = time.time()
        diff = round(tm - stime, 2)
        print()
        print(convertSec(diff) + " taken.")
        rated += 1
        print(rated, "Rated!")
        ttime += diff
        diff_list.append(diff)
        print("Total " + convertSec(ttime))
        print("Avg.", convertSec(int(ttime/rated)), "seconds per rating")
        stime = time.time()   
        print(diff_list)
    showChart(diff_list)    
        
        

def convertSec(s):
    sec = int(s%60)
    mins = int(s/60)
    sec = str(sec)
    mins = str(mins)
    return mins + ":" + sec + " seconds"


def showChart(L):
    plt.plot(L, marker='o')
    plt.show()


rateChecker()
 
    


    
#r_1023_1 = [85.48, 53.44, 202.59, 60.48, 107.23, 104.51, 108.94, 80.29, 92.09, 36.45, 68.28, 37.57, 55.86, 142.9, 62.86, 90.95, 74.33, 176.02, 117.14, 55.75, 93.59, 63.2, 145.21, 129.59, 192.94, 156.82, 114.56, 179.94, 188.31, 147.67, 201.54, 191.04, 145.83, 117.88, 127.53, 270.71, 178.23]
#plt.plot(r_1023)
#plt.show()
    
#r_1023_2 = [91.44, 270.41, 196.56, 146.17, 124.73, 531.02, 208.41, 205.09, 210.28, 145.3, 307.91, 238.4, 188.41, 172.83, 148.62, 552.55, 142.92, 121.95, 148.91, 332.54, 199.04]

    
    
#    time() -- return current time in seconds since the Epoch as a float
#    clock() -- return CPU time since process start as a float
#    sleep() -- delay for a number of seconds given as a float
#    gmtime() -- convert seconds since Epoch to UTC tuple
#    localtime() -- convert seconds since Epoch to local time tuple
#    asctime() -- convert time tuple to string
#    ctime() -- convert time in seconds to string
#    mktime() -- convert local time tuple to seconds since Epoch
#    strftime() -- convert time tuple to string according to format specification
#    strptime() -- parse string to time tuple according to format specification
#    tzset() -- change the local timezone