# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:50:51 2020

@author: kuzn137
"""
from Heteroscedasticity_test_general import Heteroscedasticity_tests
class Glejser_test(Heteroscedasticity_tests):
     '''
     Glejser_test class tests heteroscedasticity computing p value for linear regression between function of feature in original regression under the test and 
     absolute value of residuals

     Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
     '''
     def __init__(self, file_name, col_x, col_y):
         Heteroscedasticity_tests.__init__(self, file_name, col_x, col_y)
            
     def choose_test(self):
        '''
         Function chooses regression for Glejser test with the best R2 score
         
         args:  none
         return: maximum R2 score, and number of Glejser regression with this score
        '''
        scores=[]
        for j in range(len(self.features)):
            scores.append(self.find_p_value(self.features[j], self.y_new))
        #array with R2 scores
        R2s=[i[0] for i in scores]
        #array with p values
        pvalues =[i[1] for i in scores]
        #maximum R2 score
        mR2=max(R2s)
        #test wirh mR2
        n=R2s.index(mR2)+1
        del scores
        return mR2,  n, pvalues[n-1]
    
     def glejser_test(self):
         '''
         Function computes p value for Glejser test regression
         args:  none
         returns: p value to test slope for regression between considered feature and squared residuals. If p < 0.05 we rather have Heteroscedasticity.
         '''
         R2, n, pvalue= self.choose_test()
         self.plot_original()
         print("Test number {} works best with R2={}".format(n, R2))
         if pvalue > 0.05:
            return "Glejser test: P value {} is larger than 0.05, you may not have Heteroscedasticity, check the Glejser test".format(pvalue)
         else:
            return "Glejser test: P value {} is smaller than 0.05, you have Heteroscedasticity".format(pvalue)
 
    
 