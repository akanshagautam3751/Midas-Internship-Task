# A Tabular Problem - Blue book for bull dozers #

## Introduction 
Predict the auction sale price for a piece of heavy equipment to create a "blue book" for bulldozers.

## Approach 
I've trained my model on various features along with various models such as KNeighbors Regressor, Linear Regression, XGB Regressor, Random Forest Regressior.  I have obtained cross-validation accuracies simultaneously which can be found in the later section.  
The feature sets used are as follows:
1. feature1 = YearMade, datasource
2. feature1 = YearMade, datasource, state and fiBaseModel
3. feature3 = YearMade, datasource, state ,fiBaseModel, fiProductClassDesc and fiModelDesc

## Results 

Feature1 = YearMade, datasource

![Result Image 1](https://github.com/akanshagautam3751/Midas-Internship-Task/blob/master/A%20tabular%20Problem/Images_TabularProblem/1_bull.JPG)

Feature2 = YearMade, datasource, state and fiBaseModel

![Result Image 2](https://github.com/akanshagautam3751/Midas-Internship-Task/blob/master/A%20tabular%20Problem/Images_TabularProblem/2_bull.JPG)

Feature3 = YearMade, datasource, state ,fiBaseModel, fiProductClassDesc and fiModelDesc

![Result Image 3](https://github.com/akanshagautam3751/Midas-Internship-Task/blob/master/A%20tabular%20Problem/Images_TabularProblem/3_bull.JPG)
