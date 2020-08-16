# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:03:40 2020

@author: kuzn137
"""
import Glejser_test
import Park_test

#Park test
print(Park_test.Park_test("data_1_1.csv", 'x', 'y').park_test())
Park_test.Park_test("data_1_1.csv", 'x', 'y').plot_log_residuals()
#Glejser test      
print(Glejser_test.Glejser_test("data_1_1.csv", 'x', 'y').glejser_test())  
Glejser_test.Glejser_test("data_1_1.csv", 'x', 'y').plot_test(1)    
