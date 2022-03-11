#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


# In[11]:


ground_cricket_data = {"Chirps/Second": [20.0, 16.0, 19.8, 18.4, 17.1, 15.5, 14.7,
                                         15.7, 15.4, 16.3, 15.0, 17.2, 16.0, 17.0,
                                         14.4],
                       "Ground Temperature": [88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7,
                                              71.6, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5,
                                              76.3]}
df = pd.DataFrame(ground_cricket_data)


# In[12]:


df = pd.DataFrame(ground_cricket_data)
df


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel("Ground Temperature")
plt.ylabel("Chirps/Second")
plt.title("Ground Temperature vs Chirps/Second")
plt.scatter(df["Ground Temperature"],df["Chirps/Second"],color="red", marker="+")


# In[14]:


reg=linear_model.LinearRegression()
reg.fit(df[["Ground Temperature"]],df["Chirps/Second"])


# In[44]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel("Ground Temperature")
plt.ylabel("Chirps/Second")
plt.title("Ground Temperature vs Chirps/Second")
plt.grid()
plt.xticks()
plt.scatter(df["Ground Temperature"],df["Chirps/Second"],color="red", marker="+")
plt.plot(df["Ground Temperature"],reg.predict(df[["Ground Temperature"]]), color='blue')


# In[56]:


reg.coef_


# In[57]:


reg.intercept_


# In[58]:


#If the ground temperature reached 95, then crickets would be chirping at 19.7 per seconds.
reg.predict([[95]])


# In[35]:


reg.predict([[95]])
print(x)


# In[37]:


reg.score(df[["Ground Temperature"]],df["Chirps/Second"])


# In[ ]:




