# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:50:51 2020

@author: kuzn137
"""
from sklearn.metrics import r2_score, mean_squared_error
from Heteroscedasticity_test_general import Heteroscedasticity_tests
class Glejser_test(Heteroscedasticity_tests):
     '''
     Glejser_test class tests heteroscedasticity computing p value for linear regression between function of feature in origional regression under the test and absolute value of residuals

     Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
     '''
     def __init__(self, file_name, col_x, col_y):
         Heteroscedasticity_tests.__init__(self, file_name, col_x, col_y)
         self.scores=[]
         self.regression = [self.glejser_1(), self.glejser_2(), self.glejser_3()]
        
         
     def regression_scores(self, x, y):
         '''
         Function computes R2 and MSE in linear regression
         
         args: regession income x and outcome y
         returns: R2 and rme squared errors for regression with given x and y
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
         Function computes R2 and MSE in Glejser test regression
         
         arg:  none
         outcome coeffitient in regression between income feature in original regression and absolute value of residuals
         '''
         y=self.Y
         y_new=self.find_residuals(self.X, y)
         return  self.regression_scores(self.features[0], y_new)
     
     def glejser_2(self):
        '''
         Function computes R2 and MSE scores in Glejser test regression
         
         arg:  none
         outcome: scores in regression between square root from incoming feature in original regression and absolute value residuals
        '''
        y=self.Y
        y_new = self.find_residuals(self.X, y)
        return  self.regression_scores(self.features[1], y_new)
    
     def glejser_3(self):
        '''
         Function computes R2 and MSE scores in Glejser test regression
         
         arg:  none
         returns: R2 and MSE scores  in regression between inverse income feature in original regression and absolute value residuals
        '''
    
        y=self.Y
        y_new = self.find_residuals(self.X, y)
        return  self.regression_scores(self.features[2], y_new)
    
     def choose_test(self):
        '''
         Function choose regression for Glejser test with best R2 score
         
         arg:  none
         returns: R2 score, and number of Glejser regression
        '''
        for i in self.regression:
            self.scores.append(i)
            arr=[i[0] for i in self.scores]
            mR2=max(arr)
        return mR2,  arr.index(mR2)+1
    
     def glejser_test(self):
         '''
         Function computes p value for Glejser test regression
         args:  none
         returns: p value to test slope for regression between considered feature and squared residuals. If p < 0.05 we rather have Heteroscedasticity.
         '''
         R2, n = self.choose_test()
         y_new = self.find_residuals(self.X, self.Y)
         pvalue = self.find_p_value(self.features[n-1], y_new)
         return  pvalue
        
#print(Glejser_test("data_1_1.csv", 'x', 'y').glejser_test())       
 