#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 07:46:03 2019

@author: masixin
"""


#Sizing Up a New Data Set
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pylab
import scipy.stats as stats
from scipy import stats
from pandas import DataFrame
from pandas.plotting import parallel_coordinates
data = pd.read_csv('/Users/masixin/Documents/msfe/ie598/hw3/HY_Universe_corporate bond.csv',header=0)
data.head()
print("Num of rows: " + str(data.shape[0]))
print("Num of columns: " + str(data.shape[1]))
data.dtypes
print(data.describe(percentiles=[0.25, 0.5,0.75]))
# Counts for categorical data
Coupon_Type = data['Coupon Type']
Coupon_Type
unique = set(Coupon_Type)
sys.stdout.write("Unique Label Values \n")
print(unique) 
count = {}
freq = []
for i in Coupon_Type:
    if i in count:
        count[i] = count[i]+1
    else:
        count[i] = 1   
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(count)
total_mean_size = data['total_mean_size']
stats.probplot(total_mean_size, dist="norm", plot=plt)
plt.show()
print(data.head())
print(data.tail())
print(data.describe())
data1 = data[['LIQ SCORE','total_median_size','weekly_mean_volume','total_mean_size','weekly_median_volume']][:50]
parallel_coordinates(data1, 'LIQ SCORE')
plt.legend(loc = 'upper right', bbox_to_anchor = (0.6,-0.1),  ncol = 2, fancybox = True, shadow = True)
plt.show()
plt.scatter(data['n_trades'], data['LIQ SCORE'])
plt.xlabel('n_trades')
plt.ylabel('LIQ SCORE')
plt.show()
correlations = pd.DataFrame(data.corr())
print(correlations)
sys.stdout.write("Correlation between n_trades and n_days_trade \n")
np.corrcoef(data['n_trades'], data['n_days_trade'])[0, 1]
corMat = pd.DataFrame(data.corr())
sns.heatmap(corMat)
sns.set()
sns.boxplot(data['Coupon'][:30], data['n_days_trade'][:20], data=data)
plt.show()
print("My name is SIXIN MA")
print("My NetID is: {sixinma2}")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")