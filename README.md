# Machine Learning: Titanic Survival
<img src="https://images8.alphacoders.com/405/405029.jpg">

## Overview

The Titanic tragedy was a maritime disaster that occurred on April 15, 1912, when the RMS Titanic, a luxurious British passenger liner, struck an iceberg in the North Atlantic Ocean and sank during its maiden voyage from England to the USA. The Titanic was considered unsinkable, but the collision caused significant damage, and the ship's watertight compartments were breached, leading to flooding and ultimately the ship's sinking. Of the 2,224 passengers and crew on board, more than 1,500 lost their lives, making it one of the deadliest peacetime maritime disasters in history. The tragedy led to the strengthening of maritime regulations.

The aim of this project is to demonstrate the predictability of passenger survival by using different machine learning algorithms such as the neural network, logistic regression, and random forest model. The output variables of the models are binary in nature to classify survival vs. death of a passenger. The dataset was downloaded from [Kaggle](https://www.kaggle.com/) and was pre-processed using Python, SQLite, and Scikit-Learn, and visualized through a [dashboard](https://public.tableau.com/app/profile/ji.yeol.yang/viz/titanic_16825642408080/Dashboard) created using Tableau.

## Data Preparation

Below is a snippet of the dataset downloaded from Kaggle:

![rawdata](https://github.com/ericyang91/Machine_Learning_Titanic_Survival/blob/main/images/rawdata.jpg)

- PassengerId = Passenger ID
- Survived: Survival (0 = No; 1 = Yes)
- Pclass: Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
- Name: Name
- sex: Sex
- Age: Age
- SibSp: Number of Siblings/Spouses Aboard
- parch: Number of Parents/Children Aboard
- Ticket: Ticket Number
- Fare: Passenger Fare in British pound
- Cabin: Cabin
- Embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
- boat: Boat identification number
- body: Body identification number for passengers who did not survive

The missing values in the age and fare columns were filled by calculating the average value of each column. Pclass, Embarked, and Sex columns were transformed into categorical data by performing one-hot coding. The original Pclass, Embarked, and Sex columns, as well as the Boat, Body, Name, Ticket, Cabin, and Index columns, were dropped because they were deemed unnecessary for the predictive analysis.

![cleandata](https://github.com/ericyang91/Machine_Learning_Titanic_Survival/blob/main/images/cleandata.jpg)

The data was then split into target data (column = Survived) and input features (all other columns). The input features were then scaled before being fit and trained by machine learning models.

## Neural Network

The neural network involved 2 hidden layers, each with 24 and 12 neurons. The output layer consisted of only one neuron to reflect the binary nature of the study. The activation model for the two hidden layers was set to ReLu, and that of the output layer was set to Sigmoid. With 100 epochs, I was able to achieve roughly 83% accuracy on the training data and 80% on the testing data. Below is the classification report.

![classification](https://github.com/ericyang91/Machine_Learning_Titanic_Survival/blob/main/images/classification.jpg)

Several attempts were made to optimize this model. The number of neurons, deep layers, the type of activation functions, and the number of epochs were adjusted, but the model did not improve in performance. The age feature was then transformed into multiple categorical variables for simpler model learning. However, none of these attempts led to improvement.

## Logistic Regression

The logistic regression model was the second of the three machine learning models used. After splitting, scaling, and fitting the model, the logistic regression model generated an accuracy score of 82%. The overall performance turned out to be better compared to the other two models.

![logisticregression](https://github.com/ericyang91/Machine_Learning_Titanic_Survival/blob/main/images/logisticregression.jpg)

## Random Forest

The last model was the random forest model. Again, the data was split, scaled, and trained. The accuracy score was around 80%.

![randomforest](https://github.com/ericyang91/Machine_Learning_Titanic_Survival/blob/main/images/randomforest.jpg)

## Interactive Dashboard

An [interactive dashboard](https://public.tableau.com/app/profile/ji.yeol.yang/viz/titanic_16825642408080/Dashboard) that visualizes the survival rate vs. input features were created by using Tableau.

![dash](https://github.com/ericyang91/Machine_Learning_Titanic_Survival/blob/main/images/dash.jpg)


## Review and Further Research

Although logistic regression generated the best performing model out of the three models implemented, the differences in performance were small. All three models performed well in accuracy and precision, but not in the recall metrics for survivors. The reason for this is that the provided dataset was imbalanced with significantly fewer survivors than those who died. Given that none of the optimization attempts worked for the neural network model, a more balanced and larger dataset would help improve the model performance. It would also be interesting to build a predictive dashboard using Streamlit through which a user can predict whether a passenger will survive or not by entering different combinations of input features.


## Languages and Libraries

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-1.x-orange.svg)](https://pandas.pydata.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.x-green.svg)](https://matplotlib.org/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-blueviolet.svg)](https://colab.research.google.com/)
[![Logistic Regression](https://img.shields.io/badge/Logistic%20Regression-red.svg)](https://en.wikipedia.org/wiki/Logistic_regression)
[![Neural Networks](https://img.shields.io/badge/Neural%20Networks-yellow.svg)](https://en.wikipedia.org/wiki/Artificial_neural_network)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![SQLite3](https://img.shields.io/badge/SQLite-3.x-blue.svg)](https://www.sqlite.org/index.html)
[![Random Forest](https://img.shields.io/badge/Random_Forest-Machine_Learning-green)](https://en.wikipedia.org/wiki/Random_forest)
[![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-Machine_Learning-blue)](https://scikit-learn.org/)
[![Tableau](https://img.shields.io/badge/Tableau-Data_Visualization-orange)](https://www.tableau.com/)

