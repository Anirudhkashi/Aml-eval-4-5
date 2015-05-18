Group 8

1PI12CS025 ANIRUDH K
1PI12EC050 KISHORE R
1PI12IS010 AKSHAY DESHPANDE
1PI12IS083 RAVI AGRAWAL


Accuracy:
	We got an accuracy of (on test data): 78.0%
	The model converged for : 51 epochs

Documentation that describes your system:
	- We have used the neurolab python library.
	- Our model has 1 input layer(128 units), 1 output layer(26 units) and 1 hidden layer(16 units).
	- The middle hidden layer is the "tanh-sigmoid layer" and the last layer is the softmax layer.
	- We have used first 800 examples for training and next 200 examples for testing.

- We also tried for 32 hidden units which gave an accuracy of 67.5% for 10 epochs (The model did not converge).


Functions:

- getData(): The kind of main function which handles calling other functions and to extract dataset from files.

- discretize(): Mapps letters to one-hot assignment of 26 digits(0, 1)

- train(): Trains the input data using neurolab

- test(): Function to test the data

- maxed(): Function which finds the alphabet which has maximum probability.  
