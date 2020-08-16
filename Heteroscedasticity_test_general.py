# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:38:37 2020

@author: kuzn137
"""

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
      def fit_results(self, x, y):
          '''
          fit linear model 
          args: x, y
          returns: model
          '''
          model=sm.regression.linear_model.OLS(x, y)
          return model.fit()
      
      def find_residuals(self, x, y):
          '''
          function computes linear regression residuals
          args:
              regression incoming features: x
              regression outcome: y
          returns: residuals
          '''
          
          return np.abs(self.fit_results(x, y).resid)
      
      def find_p_value(self, x, y):
          '''
          computes p value for regression between x and y
          args: x and y, income and outcome for linear regression
          returns: p value
          '''
        
          results = self.fit_results(x, y)
          return results.rsquared, results.pvalues[0]
      
      def plot_data(self, x, y, xlabel, ylabel, title=None):

        """Function to plot original data
        
        Args:
           x and y to plot, xlabel, ylabel, title
        Produces:
            plot
            
        """
        # make the plot
        plt.scatter(x, y)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
      
        plt.show()

        
        
        
         
    