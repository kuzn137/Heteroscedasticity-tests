# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:50:51 2020

@author: kuzn137
"""
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
from Heteroscedasticity_test_general import Heteroscedasticity_tests
class Glejser_test(Heteroscedasticity_tests):
     '''
     Glejser_test class tests heteroscedasticity computing coefficient(s) of linear regression between feature in origional regression under the test and squared residuals

     Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
     '''
     def __init__(self, file_name, col_x, col_y):
         Heteroscedasticity_tests.__init__(self, file_name, col_x, col_y)
        
     def regression_scores(self, x, y):
         '''
         Function computes coefficient in park test regression
         
         arg:  none
         outcome R2 and rme squared errors for regression with given x and y
         '''
        #x = x.values.reshape(-1,1)
         model=self.model
         model.fit(x, y)
         y_pred = model.predict(x)
         r2=r2_score(y, y_pred)
         mse = mean_squared_error(y, y_pred)
         return r2, mse
    
     def glejser_1(self):
         '''
         Function computes coefficient in park test regression
         
         arg:  none
         outcome coeffitient in regression between income feature in original regression and absolute value of residuals
         '''
         x=self.X.values.reshape(-1,1)
         y=self.Y
         y_new=self.find_residuals(x, y)
         return  self.regression_scores(x, y_new)
    
    
     def glejser_2(self):
        '''
         Function computes coefficient in park test regression
         
         arg:  none
         outcome: scores in regression between inverse income feature in original regression and absolute value residuals
        '''
        x=self.X.values.reshape(-1,1)
        y=self.Y
        y_new = self.find_residuals(x, y)
        x_new=np.reciprocal(x)
        return  self.regression_scores(x_new, y_new)
        
#print(Glejser_test("data_1_1.csv", 'x', 'y').glejser_1())       
 