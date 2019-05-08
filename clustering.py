import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


sns.set()

from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

df = pd.read_csv("iris.csv")
X = df.iloc[:, 0:4]
y = df.iloc[:, 4]


est= KMeans(n_clusters=3)

est.fit(X)
labels = est.labels_

A = X
A['name'] = labels
for i in range(len(labels)):
  if A.loc[i , 'name'] == 0:
    A.loc[i , 'name'] = str("Iris-versicolor")
  elif A.loc[i , 'name'] == 1:
    A.loc[i , 'name'] = str("Iris-setosa")
  else :
    A.loc[i , 'name'] = str("Iris-virginica")

fig = plt.figure(1, figsize=(4, 3))
plt.subplot(2,2,1)
plt.title('Predicted')
sns.scatterplot(x="s_length", y="s_width",hue="name", style="name", data=A)

sns.set()
plt.subplot(2,2,2)
plt.title('Ground truth')
sns.scatterplot(x="s_length", y="s_width",hue="name", style="name", data=df)

plt.subplot(2,2,3)
sns.scatterplot(x="p_length", y="p_width",hue="name", style="name", data=A)

sns.set()
plt.subplot(2,2,4)
sns.scatterplot(x="p_length", y="p_width",hue="name", style="name", data=df)


plt.show()

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print(confusion_matrix(y, df.iloc[:, 4]))
print(classification_report(y, df.iloc[:, 4]))
print(accuracy_score(y, df.iloc[:, 4]))

