# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:38:37 2020

@author: kuzn137
"""
from sklearn import linear_model as lm
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
class Heteroscedasticity_tests():
      """ Generic class for Heteroscedasticity tests as
            Park and Glejser methods.
            Both methods use linear regression for functions of tested income feature and residuals as outcome
    
        Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
      """
      def __init__(self, file_name, col_x, col_y):
         self.df=pd.read_csv(file_name)
         #incoming feature
         self.X = self.df[col_x].values.reshape(-1,1)
         #outcome
         self.Y = self.df[col_y].values.reshape(-1,1)
         #residuals
         self.y_new=self.find_residuals(self.X, self.Y)
        
         del self.df
      def find_residuals(self, x, y):
          '''
          function computes linear regression residuals
          args:
              regression incoming features: x
              regression outcome: y
          function returns residuals
          '''
          model = lm.LinearRegression()
          y = self.Y
          model.fit(x, y)
          y_pred=model.predict(y)
          return abs(y_pred - y)
      
      def find_p_value(self, x, y):
          '''
          computes p value for regression between x and y
          args: x and y, income and outcome for linear regression
          returns: p value
          '''
          #other library for regression to find p value 
          model=sm.regression.linear_model.OLS(x, y)
          results = model.fit()
          return results.rsquared, results.pvalues[0]
      
      def plot_data(self, x, y):

        """Function to plot original data
        
        Args:
           none
        Produces:
            plot
            
        """
        # make the plot
        plt.scatter(x, y)
        plt.title('Original data')
        plt.ylabel('Y')
        plt.xlabel('X')
      
        plt.show()

        
        
        
         
    