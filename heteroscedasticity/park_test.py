# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:44:26 2020

@author: kuzn137
"""
import numpy as np
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
         outcome coeffitient in regression between income feature in origional regression and squared residuals
         '''
        x=self.X
        y=self.Y
        residuals = self.find_residuals(x, y)
        x = self.X.values.reshape(-1,1)
        y = np.square(residuals)
        model=self.model
        model.fit(x, y)
        return  model.coef_[0][0]
 
print(Park_test("data_1_1.csv", 'x', 'y').park_regression())
        
   
