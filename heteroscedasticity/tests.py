# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:03:40 2020

@author: kuzn137
"""
import pandas as pd
import numpy as np
import Glejser_test
import Park_test
df=pd.read_csv("data_1_1.csv")
         #incoming feature
X = df['x'].values.reshape(-1,1)
         #outcome
Y = df['y'].values.reshape(-1,1)
#Park test
print(Park_test.Park_test(X, Y).park_test())
Park_test.Park_test(X, Y).plot_log_residuals()
#Glejser test      
print(Glejser_test.Glejser_test(X, Y).glejser_test())  
Glejser_test.Glejser_test(X, Y).plot_test(1)    

df=pd.read_csv("datasets_141319_332156_1.01. Simple linear regression.csv")
X = df['GPA'].values.reshape(-1,1)
Y = df['SAT'].values.reshape(-1,1)

print(Park_test.Park_test(X, Y).park_test())
Park_test.Park_test(X, Y).plot_log_residuals()
#Glejser test      
print(Glejser_test.Glejser_test(X, Y).glejser_test())  
Glejser_test.Glejser_test(X, Y).plot_test(1)    


X=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]).reshape(-1,1)
Y=np.array([1.1, 2.1, 3.2, 4.3, 5.2, 6.2, 7.3, 8.1, 8.9, 10.05, 10.96, 12.1, 13.1, 14.4]).reshape(-1, 1)


print(Park_test.Park_test(X, Y).park_test())
Park_test.Park_test(X, Y).plot_log_residuals()
#Glejser test   
print(Glejser_test.Glejser_test(X, Y).glejser_test())  
Glejser_test.Glejser_test(X, Y).plot_test(1)    

