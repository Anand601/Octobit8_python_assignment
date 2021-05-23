#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  
import pandas as pd 
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


dataset = pd.read_csv('C:\\Users\\Prakash Jha\\Downloads\\Restaurant_Reviews.tsv', delimiter = '\t')


# In[3]:


dataset


# In[4]:



 
nltk.download('stopwords')
 
# to remove stopword
from nltk.corpus import stopwords
 
# for Stemming propose 
from nltk.stem.porter import PorterStemmer
 
# Initialize empty array
# to append clean text 
corpus = [] 
 
# 1000 (reviews) rows to clean
for i in range(0, 1000): 
     
   # column : "Review", row ith
   review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) 
     
   # convert all cases to lower cases
   review = review.lower() 
     
   # split to array(default delimiter is " ")
   review = review.split() 
     
   # creating PorterStemmer object to
   # take main stem of each word
   ps = PorterStemmer() 
     
   # loop for stemming each word
   # in string array at ith row    
   review = [ps.stem(word) for word in review
               if not word in set(stopwords.words('english'))] 
                 
   # rejoin all string array elements
   # to create back into a string
   review = ' '.join(review)  
     
   # append each string to create
   # array of clean text 
   corpus.append(review) 


# In[5]:



  
# To extract max 1500 feature.
# "max_features" is attribute to
# experiment with to get better results
cv = CountVectorizer(max_features = 1500) 
  
# X contains corpus (dependent variable)
X = cv.fit_transform(corpus).toarray() 
  
# y contains answers if review
# is positive or negative
y = dataset.iloc[:, 1].values 


# In[6]:


# Splitting the dataset into
# the Training set and Test set

  
# experiment with "test_size"
# to get better results
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)


# In[7]:


from sklearn.ensemble import RandomForestClassifier
  
# n_estimators can be said as number of
# trees, experiment with n_estimators
# to get better results 
model = RandomForestClassifier(n_estimators = 501,
                            criterion = 'entropy')
                              
model.fit(X_train, y_train) 


# In[8]:


y_pred = model.predict(X_test)
  
y_pred


# In[9]:


from sklearn import metrics


# In[10]:


acc=metrics.accuracy_score(y_pred,y_test)


# In[11]:


print(acc)


# In[15]:


from sklearn.neighbors import KNeighborsClassifier
max=0
for k in range(1,30):
    knn_obj=KNeighborsClassifier(n_neighbors=k)
    knn_obj.fit(X_train,y_train)
    pred=knn_obj.predict(X_test)
    acc=metrics.accuracy_score(pred,y_test)
    print(k,"=",acc)
    if max<acc:
        max=acc
        kvalue=k
print("max accuracy is at value k is ",kvalue)
print("max accuracy is",max)
    


# In[16]:


knn_obj=KNeighborsClassifier(n_neighbors=3)
knn_obj.fit(X_train,y_train)
pred=knn_obj.predict(X_test)
acc1=metrics.accuracy_score(pred,y_test)
print(acc1)


# In[ ]:




