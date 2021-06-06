#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#Dataset1
rawdata=r'S:\NUNAM\data.xlsx'

#Dataset2
rawdata1=r'S:\NUNAM\data_1.xlsx'


# In[2]:


df=pd.read_excel(rawdata,sheet_name=None)


# In[3]:


df


# In[5]:


df_new=pd.concat(df,sort=False)


# In[6]:


df_new.keys()


# In[7]:


df.keys()


# In[8]:


df1=pd.read_excel(rawdata1,sheet_name=None)
#Returns an ordered dictionary


# In[11]:


df1


# In[9]:


df_new1=pd.concat(df1,sort=False)


# In[10]:


df_new1.keys()


# In[11]:


df1.keys()


# # Detail_67_

# In[12]:


Detail_67=df['Detail_67_1_1']
Detail_67.describe()


# In[13]:


import seaborn as sns
cm = sns.light_palette("green", as_cmap=True)

s = Detail_67.style.background_gradient(cmap=cm)
s


# In[14]:


Detail_67.describe()


# In[24]:


Detail_67=Detail_67.append(df['Detail_67_1_1'])


# In[25]:


Detail_67=Detail_67.append(df['Detail_67_1_1_1'])


# In[26]:


Detail_67=Detail_67.append(df['Detail_67_1_1_2'])


# In[27]:


Detail_67=Detail_67.append(df['Detail_67_1_1_3'])


# In[28]:


Detail_67=Detail_67.append(df['Detail_67_1_1_4'])


# In[29]:


Detail_67=Detail_67.append(df['Detail_67_1_1_5'])


# In[30]:


Detail_67=Detail_67.append(df['Detail_67_1_1_6'])


# In[31]:


Detail_67.describe()


# In[32]:


Detail_67.to_csv('detail.csv')


# # DetailVol_67_

# In[33]:


df.keys()


# In[34]:


detail_vol=df['DetailVol_67_1_1']


# In[48]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_1'])


# In[49]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_2'])


# In[50]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_3'])


# In[51]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_4'])


# In[52]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_5'])


# In[53]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_6'])


# In[54]:


detail_vol.describe()


# In[55]:


detail_vol.to_csv('detailVol.csv')


# In[56]:


df1.keys()


# In[57]:


detail_temp=df['DetailTemp_67_1_1']


# In[58]:


detail_temp.describe()


# In[59]:


detail_temp=detail_temp.append(df['DetailTemp_67_1_1_1'])


# In[60]:


detail_temp=detail_temp.append(df['DetailTemp_67_1_1_2'])


# In[62]:


detail_temp=detail_temp.append(df1['DetailTemp_67_1_1_3'])


# In[63]:


detail_temp=detail_temp.append(df1['DetailTemp_67_1_1_4'])


# In[64]:


detail_temp=detail_temp.append(df1['DetailTemp_67_1_1_5'])


# In[65]:


detail_temp=detail_temp.append(df1['DetailTemp_67_1_1_6'])


# In[66]:


detail_temp.describe()


# In[67]:


detail_temp.to_csv('DetailTemp.csv')


# In[ ]:




