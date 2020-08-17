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
         #outcome
Y = df['SAT'].values.reshape(-1,1)

print(Park_test.Park_test(X, Y).park_test())
Park_test.Park_test(X, Y).plot_log_residuals()
#Glejser test      
print(Glejser_test.Glejser_test(X, Y).glejser_test())  
Glejser_test.Glejser_test(X, Y).plot_test(1)    


X=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]).reshape(-1,1)
Y=np.array([1.1, 2.1, 3.1, 4.1, 5.1, 6.2, 7.0, 8.1, 8.9, 10.05, 10.96, 12.01, 13.1]).reshape(-1, 1)


print(Park_test.Park_test(X, Y).park_test())
Park_test.Park_test(X, Y).plot_log_residuals()
#Glejser test      
print(Glejser_test.Glejser_test(X, Y).glejser_test())  
Glejser_test.Glejser_test(X, Y).plot_test(1)    

