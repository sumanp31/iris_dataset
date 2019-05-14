# iris_dataset
### Dataset details
Download the data set [here](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/) 

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

### Code Details
A description on files in this repository:
1. **data_vis.py** : Data visulaization. Part 1 visualises how the different attributes of the different categories vary. Part 2 is the scatter plot of length vs width with every category ploted in different colour.

2.** classification.py** : The following classification algorithms are used 
-- Logistic Regression 
-- Gaussian Naive Bayes 
-- Support Vector Machine 
-- Decision Tree 
-- Random Forest 
-- K-neighbour

The algorithms are compared using precision, recall and accuracy.

3.** clustering.py**: k- mean clustering.

##***Report***

### Dataset Visualisation
#### Checking each attribute for each of the category.
![](https://github.com/sumanp31/iris_dataset/blob/master/Figure_3.png)
![](https://github.com/sumanp31/iris_dataset/blob/master/Figure_4.png) 
![](https://github.com/sumanp31/iris_dataset/blob/master/Figure_5.png) 
![](https://github.com/sumanp31/iris_dataset/blob/master/Figure_2.png) 
As it can be seen from the above 4 images, the *iris-setosa* is very distinctive depending on petal lenght and width. However, the *iris-versicolor* and the *iris-virginica* are not distinguishable from each other.

#### Scatter plot for distribution of different category for different combination of attribute
![](https://github.com/sumanp31/iris_dataset/blob/master/Figure_1.png) 
From the above 4 images, It can be seen that *Iris-setosa* are completely different. However, the *iris-versicolor* and the *iris-virginica* are not distinguishable from each other. for most of the parameter combination except for sepal length vs petal length.

### Algorithm Output
The dataset was split into train and test dataset. 20% of dataset was randomly selected and used for testing. depending on the comparision between predicted category and original output, the following result was achieved.
#### Classification
1.**Linear Regression**
 ![](https://github.com/sumanp31/iris_dataset/blob/master/L_reg.png) 
2.**Naive Bayes**
![](https://github.com/sumanp31/iris_dataset/blob/master/N_Bayes.png) 
3.**SVM**
![](https://github.com/sumanp31/iris_dataset/blob/master/svm.png) 
4.**K neighbours**
![](https://github.com/sumanp31/iris_dataset/blob/k_neigh.png) 
5.**Decision Tree**
![](https://github.com/sumanp31/iris_dataset/blob/D_Tree.png) 
6.**Random Forest**
![](https://github.com/sumanp31/iris_dataset/blob/master/R_Forest.png) 