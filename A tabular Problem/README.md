# A Tabular Problem - Blue book for bull dozers #

## Introduction ##
Predict the auction sale price for a piece of heavy equipment to create a "blue book" for bulldozers.

## Approach ##
I've trained my model on various features along with various models such as KNeighbors Regressor, Linear Regression, XGB Regressor, Random Forest Regressior.  I have obtained cross-validation accuracies simultaneously which can be found in the later section.  
The feature sets used are as follows:
1. feature1 = YearMade, datasource
2. feature1 = YearMade, datasource, state and fiBaseModel
3. feature3 = YearMade, datasource, state ,fiBaseModel, fiProductClassDesc and fiModelDesc

## Results ##

Feature1 = YearMade, datasource

Feature1 = YearMade, datasource, state and fiBaseModel

Feature3 = YearMade, datasource, state ,fiBaseModel, fiProductClassDesc and fiModelDesc
