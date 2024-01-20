#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn import linear_model


# In[6]:


df = pd.read_excel(r'C:\Users\AHLP\Documents\ML\homeprices.xlsx')
print(df)


# In[11]:


pd.DataFrame(df)


# # Data Preprocessing: Fill NA values with median value of a column

# In[19]:


df.bedrooms.median()


# In[18]:


import math
median_bedrooms = math.floor(df.bedrooms.median())
median_bedrooms


# In[17]:


df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
df


# In[30]:


reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)


# In[23]:


reg.coef_


# In[26]:


reg.intercept_


# In[33]:


reg.predict([[2500,4,5]])


# In[ ]:




