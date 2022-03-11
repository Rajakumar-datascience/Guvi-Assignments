#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


df = pd.read_fwf('brain_body.txt')
df.head()


# In[8]:


df.shape


# In[20]:


print("No. of rows in the dataset:",df.shape[0])
print("No. of columns in the dataset:",df.shape[1])


# In[22]:


df.isnull().sum()


# In[23]:


df.info()


# In[35]:


df.describe()


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel("Brain")
plt.ylabel("Body")
plt.title("Brain vs Body")
plt.scatter(df["Brain"],df["Body"],color="red", marker="+")


# In[14]:


from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(df[["Brain"]],df["Body"])


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel("Brain")
plt.ylabel("Body")
plt.title("Brain vs Body")
plt.xticks()
plt.scatter(df["Brain"],df["Body"],color="red", marker="+")
plt.plot(df["Brain"],reg.predict(df[["Brain"]]), color='blue')


# In[16]:


reg.score(df[["Brain"]],df["Body"])


# In[ ]:




