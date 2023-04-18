# Project-4-Survival Prediction on the Titanic Ship

<img src="https://images8.alphacoders.com/405/405029.jpg">

Using Machine learning algorithm on the famous Titanic Disaster Dataset for Predicting the survival of the passenger

Data Information:

    Survival: 0 = Did not survive, 1 = Survived
    Pclass: Ticket class where 1 = First class, 2 = Second class, 3 = Third class.
    Sex: Male or female
    Age: Age of Passengers
    SibSp: Number of siblings or spouses aboard the titanic
    Parch: Number of parents or children aboard the titanic
    Ticket: Passenger ticket number
    Fare: Passenger fare
    Cabin: Cabin number
    Embarked: Point of embarkation where C = Cherbourg, Q = Queenstown, S = Southampton
 

Dependencies:

    Python3
    Numpy
    Pandas
    Sqlite
    Matplotlib
    Machine Learning Algorithm
    Classification Algorithms
    
This Notebook contains:

    Data Handling
    Importing Data with Pandas
    Cleaning Data
    Exploring Data through Visualizations with Matplotlib

Data Analysis:

    Logistic Regression
    Random Forest
    Neural network
    


Preprocessing and Cleaning Data
    - We have import the data into panada and sqlite to clean the data.
    - The data have been reviewed and filled in null.
    - after filled in all the null numbers, dropped unnecessary col
  
![Data Cleaning](https://user-images.githubusercontent.com/115420417/232640688-92aaf987-be7d-4a2d-b8e6-3e1c5abda3dc.png)



Neural Network

- By using the Neural Network, our first attempt, loss = 0.44, accuracy = 0.81
![original](https://user-images.githubusercontent.com/115420417/232641026-13a0f9e1-0711-4214-9b99-f19ba43329c6.jpg)


- The second attempt, loss: 0.46, accuracy = 0.82

![optimization](https://user-images.githubusercontent.com/115420417/232641033-f6e2d815-e7a2-4996-a33b-24fce5696911.jpg)

The neural network is the first of several models we used to predict the survival outcome of the Titanic tragedy. After cleaning up and scaling the data set, we used 13 input features to predict the outcome of passenger survival. We used two hidden layers that consisted of 26 and 13 neurons, with 1 neuron in the outcome layer for binary classification purpose. The ReLu function was used as our activation function for the two hidden layers, as the function is computationally more efficient than Tanh. The function also helps to address the vanishing gradient problem, which can lead to slower training and lower accuracy.
We used the sigmoid function for our outcome layer due to its binary nature. With epoch set to 200, the model's accuracy was 0.81 with loss at 0.48.


Supervised Learning

- Logistic Regression

![1681779282(1)](https://user-images.githubusercontent.com/115420417/232641491-395df0ed-b312-4f3b-a536-48aa5fa48285.png)

- As the classified and binned data, we had needed to utilize classification based supervised learning models.
- After training, the model achieved an overall accuracy of 80%.
- With the available data, the model had the most difficulty with recall in detecting survivors.


- Random Forest

![1681779429(1)](https://user-images.githubusercontent.com/115420417/232641722-03e6bc78-bb2a-4ab2-97ff-4b1170114a2c.png)

- The initial randomly selected parameters yielded 79.3% accuracy.
- To fine tune the model, the grid_search command was used to train the model and determine the most accurate model.  
- The first optimization yielded an accuracy of 79.6% with depth=20, samples/leaf=5, estimators=25
- The second optimization yielded an accuracy of 79.7% with depth=20, samples/leaf=4, estimators=50


Visualizations 

- Passenger Class Distribution

![Passenger Class](https://user-images.githubusercontent.com/115420417/232641934-44f76aa6-b218-444e-9cc7-e583bd442f7f.png)


- Survived VS Not Survived

![Survival and Not Survival](https://user-images.githubusercontent.com/115420417/232642175-62425376-1fcf-4287-a0ba-9a4793ca4b80.png)


- Sex Distribution

![Sex](https://user-images.githubusercontent.com/115420417/232642211-55471374-5bcb-4024-be87-3add22f8adb3.png)


- Age Distribution

![Age Distribution](https://user-images.githubusercontent.com/115420417/232642239-d29a6bd4-70df-4264-b0bd-519c9079c599.png)

