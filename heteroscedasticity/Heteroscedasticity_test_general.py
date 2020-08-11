# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:38:37 2020

@author: kuzn137
"""
from sklearn import linear_model as lm
import pandas as pd

class Heteroscedasticity_tests():
      """ Generic class for Heteroscedasticity tests as
            Park and Glejser methods.
            Both methods use linear regression for residuals as outcome
    
        Attributes:
            data file, file_name is name string
            column col_x is for incoming features
            column col_y is for outcome
      """
      def __init__(self, file_name, col_x, col_y):
         self.df=pd.read_csv(file_name)
         self.X = self.df[col_x]
         self.Y = self.df[col_y]
         self.model = lm.LinearRegression()
    
      def find_residuals(self, x, y):
          '''
          function computes linear regression residuals
          args:
              regression incoming features: x
              regression outcome: y
          function outcome residual
          '''
          model = self.model
          x = self.X.values.reshape(-1,1)
          y = self.Y.values.reshape(-1,1)
          model.fit(x, y)
          y_pred=model.predict(y)
          return y_pred - y
        
        
         
    