# Heteroscedasticity-tests

# Description
 Class for Heteroscedasticity tests, Park and Glejser methods.  Both methods use linear regression for original incoming feature function and a function of residuals as outcome.
 Park test uses linear regression for log(x), x is incoming feature in original regression, and log(residuals^2).
 Glejser test choses between three linear regression for squared residuals outcome and x, sqrt(x) and 1/x as incoming features by best R2 score.
 If there is Heteroscedasticity is tested by p value for resulting regression (if p value < 0.05, we have Heteroscedasticity).
 Tests limitation is that it is assumed that resulting regression does not have Heteroscedasticity. If one method has high p value it is good to consider all methods.
 Class is under construction.
 
 # Author
 Inga Kuznetsova
 
 # Libraries
 scikit learn, stats models, numpy, pandas
 
 # Current files
 Heteroscedasticity_test_general.py is generic class
 
 park_test.py is Park test subclass
 
 Glejser_test.py is Glejser test subclass 
 
 data_1_1.csv is data file
 
# References
https://en.wikipedia.org/wiki/Heteroscedasticity

R. E. Park (1966). "Estimation with Heteroscedastic Error Terms". Econometrica. 34 (4): 888

Glejser, H. (1969). "A New Test for Heteroskedasticity". Journal of the American Statistical Association. 64 (235): 315–323
