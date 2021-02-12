#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import plotly.express as px


# In[2]:


url = 'http://api.open-notify.org/iss-now.json'


# In[51]:


df = pd.read_json(url)


# In[61]:


df


# In[71]:


df['longitude'] = df.loc['longitude','iss_position']
df['latitude'] = df.loc['latitude','iss_position']
df.reset_index(inplace=True)


# In[72]:


df


# In[73]:


df = df.drop(['index','message'],axis=1)


# In[74]:


df


# In[76]:


fig = px.scatter_geo(df,lat='latitude',
                    lon = 'longitude')
fig.show()


# In[ ]:




