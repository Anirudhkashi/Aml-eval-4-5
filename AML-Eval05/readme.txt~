Group 8

1PI12CS025 Anirudh K
1PI12EC050 Kishore R
1PI12IS010 Akshay R Deshpande
1PI12IS083 Ravi Agarwal


Accuracy:
          We got the maximum accuracy around (35-45)%.
          The model converges in about 50 epochs.


Documentation that describes the system:
          - We have used neurolab python library and the HMM implementation provided by you.
          - Our neural network model has 1 input layer(128+1 units), 1 output layer(26 units) and 1 hidden layer(16 units).
          - The middle hidden layer is the "tanh-sigmoid layer" and the last layer is the softmax layer.
          - Our HMM model has 2 states. The input to each HMM is the bitmap representation of the image. We are using 2 HMM s to differentiate b/w vowels and consonants.
          - The dataset we used consists of 2 subsets, one of vowel examples and other for consonants both of size 2000.


Functions:

- getData(): The kind of main function which handles calling other functions and to extract dataset from files.

- discretize(): Mapps letters to one-hot assignment of 26 digits(0, 1)

- train(): Trains the input data using neurolab

- test(): Function to test the data

- maxed(): Function which finds the alphabet which has maximum probability. 

- addBit(): Function which trains and tests the HMMs and appends the class bit which is got as the result to the input of neural network.

- genModel(): Function that trains the HMM given the input vectors.

- argMax(): Function that returns the class of the input test vector using the forward algorithm.

- yVals(): Function that returns the class vector given a list of test examples. 

           
