# Heteroscedasticity-tests, Park and Glejser methods

# Description
 Class for Heteroscedasticity tests, Park and Glejser methods.  Both methods use linear regression for original incoming feature or its function and a function of residuals as outcome. Park test uses linear regression for log(|x|), x is incoming feature in original regression, and log(residuals^2).
 Glejser test chooses between three linear regressions for absolute value of residuals outcome and x (test #1), sqrt(|x|) (test #2) and 1/x (test #3) as incoming features by best R2 score.
 Heteroscedasticity is tested by p value for resulting regression (if p value < 0.01 for Park and p value < 0.00001, we have heteroscedasticity). From tests with different datasets it was established what P values are good. Tests limitation is that it is assumed that resulting regression with residuals does not have Heteroscedasticity. If one method has high p value it is good to consider all methods.
 
 
 # Author
 Inga Kuznetsova
 
 # Libraries
 statsmodels, numpy
 
 # Current files
 Heteroscedasticity_test_general.py is generic class
 
 Park_test.py is Park test subclass
 
 Glejser_test.py is Glejser test subclass 
 
 data_1_1.csv and datasets_141319_332156_1.01. Simple linear regression.csv are data files
 
 tests.py tests classes on data from data_1_1.csv, which have heteroscedasticity
 
# References
https://en.wikipedia.org/wiki/Heteroscedasticity

R. E. Park (1966). "Estimation with Heteroscedastic Error Terms". Econometrica. 34 (4): 888

Glejser, H. (1969). "A New Test for Heteroskedasticity". Journal of the American Statistical Association. 64 (235): 315–323
