# iris_dataset
Download the data set here : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

Attributes:
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica

A description on files in this repository:
1. data_vis.py : Data visulaization. Part 1 visualises how the different attributes of the different categories vary. Part 2 is the scatter plot of length vs width with every category ploted in different colour.

2. classification.py : The following classification algorithms are used 
-- Logistic Regression
-- Gaussian Naive Bayes
-- Support Vector Machine
-- Decision Tree
-- Random Forest
-- K-neighbour 

   The algorithms are compared using precision, recall and accuracy.

3. clustering.py: k- mean clustering.
