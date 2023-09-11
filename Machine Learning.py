#!/usr/bin/env python
# coding: utf-8

# In[36]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import datasets
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


data1 = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
data1



# In[7]:


import pandas as pd
import numpy as np

Step1 = data1.replace('Nan, np.nan')

Step2 = Step1.fillna(0)
Step2



# In[8]:


import pandas as pd

data2 = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')
data2


# ## TASK 1
# Create a NumPy array from the column Class in data, by applying the method to_numpy() then assign it to the variable Y,make sure the output is a Pandas series (only one bracket df['name of column']).

# In[11]:


Y = data1['Class'].to_numpy()
Y


# ## TASK 2
# 
# Standardize the data in <code>X</code> then reassign it to the variable  <code>X</code> using the transform provided below.

# In[45]:


X = data1[['Class']].to_numpy()
X

Y = data1['Class'].to_numpy()
Y

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=4) 


X = preprocessing.StandardScaler().fit(X).transform(X)
X


# ## TASK 3
# 
# Use the function train_test_split to split the data X and Y into training and test data. Set the parameter test_size to 0.2 and random_state to 2. The training data and test data should be assigned to the following labels.

# In[38]:


X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=2)
Y_test.shape


# ## TASK 4
# Create a logistic regression object then create a GridSearchCV object logreg_cv with cv = 10. Fit the object to find the best parameters from the dictionary parameters.

# In[39]:


LR=LogisticRegression(C=0.01, penalty='l2', solver='lbfgs').fit(X_train,Y_train)
LR

parameters ={"C":[0.01,0.1,1],'penalty':['l2'], 'solver':['lbfgs']}

logreg_cv = GridSearchCV(LR, parameters, cv=10)
logreg_cv.fit(X, Y)

yhat = LR.predict(X_test)
yhat

print("tuned hpyerparameters :(best parameters) ",logreg_cv.best_params_)
print("accuracy :",logreg_cv.best_score_)




# ## TASK 5
# Calculate the accuracy on the test data using the method score:

# In[42]:


LR=LogisticRegression(C=0.01, penalty='l2', solver='lbfgs').fit(X_train,Y_train)
LR

LR.fit(X_train, Y_train)
LR.score(X_train, Y_train)


# ## TASK 6
# Create a support vector machine object then create a GridSearchCV object svm_cv with cv - 10. Fit the object to find the best parameters from the dictionary parameters.

# In[35]:


LR = svm.SVC(kernel='rbf')
LR

parameters ={"C":np.logspace(-3, 3, 5), 'kernel':('linear', 'rbf', 'poly', 'rbf', 'sigmoid'), 'gamma':np.logspace(-3, 3, 5)}

svm_cv = GridSearchCV(LR, parameters, cv=10)
svm_cv.fit(X, Y)

print("tuned hpyerparameters :(best parameters) ",svm_cv.best_params_)
print("accuracy :",svm_cv.best_score_)



# ## TASK 7
# Calculate the accuracy on the test data using the method score:

# In[41]:


LR = svm.SVC(kernel='poly')
LR

LR.fit(X_train, Y_train)
LR.score(X_train, Y_train)


# ## TASK 8
# Create a decision tree classifier object then create a GridSearchCV object tree_cv with cv = 10. Fit the object to find the best parameters from the dictionary parameters.

# In[47]:


tree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
tree

parameters = {'criterion': ['gini', 'entropy'],
     'splitter': ['best', 'random'],
     'max_depth': [2*n for n in range(1,10)],
     'max_features': ['auto', 'sqrt'],
     'min_samples_leaf': [1, 2, 4],
     'min_samples_split': [2, 5, 10]}

tree_cv = GridSearchCV(tree, parameters, cv=10)
tree_cv.fit(X, Y)

print("tuned hpyerparameters :(best parameters) ",tree_cv.best_params_)
print("accuracy :",tree_cv.best_score_)








# ## TASK 9
# Calculate the accuracy of tree_cv on the test data using the method score:

# In[48]:


tree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
tree

tree.fit(X_train, Y_train)
tree.score(X_train, Y_train)


# ## TASK 10
# Create a k nearest neighbors object then create a GridSearchCV object knn_cv with cv = 10. Fit the object to find the best parameters from the dictionary parameters.

# In[49]:


KNN = KNeighborsClassifier(n_neighbors=5)
KNN

parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'p': [1,2]}

knn_cv = GridSearchCV(KNN, parameters, cv=10)
knn_cv.fit(X, Y)

print("tuned hpyerparameters :(best parameters) ",knn_cv.best_params_)
print("accuracy :",knn_cv.best_score_)


# ## TASK 11
# Calculate the accuracy of knn_cv on the test data using the method score:

# In[50]:


KNN = KNeighborsClassifier(n_neighbors=5)
KNN

KNN.fit(X_train, Y_train)
KNN.score(X_train, Y_train)

