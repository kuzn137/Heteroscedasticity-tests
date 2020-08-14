# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:44:26 2020

@author: kuzn137
"""
import numpy as np
import statsmodels.api as sm

#import matplotlib.pyplot as plt
from Heteroscedasticity_test_general import Heteroscedasticity_tests
class Park_test(Heteroscedasticity_tests):
     '''
     Park_test class tests heteroscedasticity computing coefficient(s) of linear regression between feature in original regression under the test and squared residuals

     Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
     '''
     def __init__(self, file_name, col_x, col_y):
         Heteroscedasticity_tests.__init__(self, file_name, col_x, col_y)
        
     def park_regression(self):
         '''
         Function computes coefficient in park test regression
         arg:  none
         outcome: p value to test slope for regression between considered feature and residuals. If p < 0.05 we rather have Heteroscedasticity.
         '''
         x=self.X.values.reshape(-1,1)
         y=self.Y
         residuals = self.find_residuals(x, y)
         y_new = np.square(residuals)
         model=sm.regression.linear_model.OLS(x, y_new)
         results = model.fit()
         print(results.summary())
         return "pvalue {}, coefficient {}".format(results.pvalues[0])
 
#print(Park_test("data_1_1.csv", 'x', 'y').park_regression())
        
   