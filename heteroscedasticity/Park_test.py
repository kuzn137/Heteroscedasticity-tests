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
     Park_test class tests heteroscedasticity computing p value for linear regression between feature in original regression under the test and squared residuals

     Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
     '''
     def __init__(self, file_name, col_x, col_y):
         Heteroscedasticity_tests.__init__(self, file_name, col_x, col_y)
        
     def park_regression(self):
         '''
         Function computes p value for park test regression
         args:  none
         returns: p value to test slope for regression between considered feature and squared residuals. If p < 0.05 we rather have Heteroscedasticity.
         '''
      
         x = np.log(np.abs(self.X))
         pvalue = self.find_p_value(x, np.square(self.y_new))
         return "pvalue {}".format(pvalue)
 
#print(Park_test("data_1_1.csv", 'x', 'y').park_regression())
        
   