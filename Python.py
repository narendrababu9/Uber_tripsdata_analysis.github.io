#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
data=pd.read_csv("uberdata.csv")


# In[37]:


data


# In[38]:


data[['START_DATE*','PURPOSE*']]


# In[39]:


data.loc[[2,4,6],['PURPOSE*','MILES*']]


# In[40]:


data.iloc[:7,:4]


# In[12]:


data[data['START*'] =='Unknown Location']


# In[41]:


data[data['MILES*'] > 200]


# In[42]:


len(data['MILES*'])


# In[43]:


data.isnull().sum()


# In[44]:


data.info()


# In[45]:


data.dropna(inplace=True)


# In[46]:


data.isnull().sum()


# In[47]:


data


# In[18]:





# In[48]:


x = data['CATEGORY*'].value_counts().plot(kind='bar')


# In[49]:


data


# In[50]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[51]:


plt.hist(data['MILES*'], bins=50)
plt.xlabel('Trip Distance (miles)')
plt.ylabel('Frequency')
plt.title('Distribution of Trip Distance')
plt.show()


# In[52]:


# plot the distribution of the trip distance by purpose
sns.histplot(data=data, x='MILES*', hue='PURPOSE*', multiple='stack')
plt.xlim(0, 80)


# In[19]:


sns.pairplot(data[['MILES*', 'START_DATE*', 'END_DATE*', 'PURPOSE*']], hue='PURPOSE*')
plt.xlim(0, 80)


# In[53]:


data.corr


# In[55]:


sns.heatmap(data.corr(), annot = True,fmt="0.1f")


# In[ ]:





# In[57]:


data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format='%m/%d/%Y %H:%M')


# In[58]:


data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format='%m/%d/%Y %H:%M')


# In[59]:


data['weekday'] = data['START_DATE*'].dt.weekday


# In[60]:


trips_by_category = data.groupby('CATEGORY*').size()
print(trips_by_category)


# In[61]:


trips_by_weekday = data.groupby('weekday').size()
print(trips_by_weekday)


# In[62]:


miles_by_purpose = data.groupby('PURPOSE*')['MILES*'].sum()
print(miles_by_purpose)


# In[63]:


trips_by_category.plot(kind='bar')
plt.xlabel('CATEGORY*')
plt.ylabel('Number of trips')
plt.title('Uber trips by category')
plt.show()


# In[64]:


trips_by_weekday.plot(kind='bar')
plt.xlabel('Weekday')
plt.ylabel('Number of trips')
plt.title('Uber trips by weekday')
plt.show()


# In[65]:


miles_by_purpose.plot(kind='bar')
plt.xlabel('PURPOSE*')
plt.ylabel('MILES*')
plt.title('Uber miles by purpose')
plt.show()


# In[71]:


purpose_counts = data.groupby('PURPOSE*')['MILES*'].sum()


# In[72]:


plt.figure(figsize=(8, 6))
plt.pie(purpose_counts.values, labels=purpose_counts.index, autopct='%1.1f%%')
plt.title('Uber miles by purpose')
plt.show()


# In[75]:


weekday_category_counts = data.groupby(['weekday', 'CATEGORY*'])['MILES*'].sum().unstack()


# In[76]:


weekday_category_counts.plot(kind='bar', stacked=True, figsize=(8, 6))
plt.title('Uber miles by weekday and category')
plt.xlabel('Weekday')
plt.ylabel('Miles')
plt.show()


# In[79]:


purpose = 'Meeting'
data = data[data['PURPOSE*'] == purpose]

# Create a scatter plot of miles by start date
plt.figure(figsize=(8, 6))
plt.scatter(data['START_DATE*'], data['MILES*'])
plt.title(f'Uber miles for {purpose} by start date')
plt.xlabel('Start date')
plt.ylabel('Miles')
plt.show()


# In[83]:


plt.figure(figsize=(8, 6))
plt.hist(data['MILES*'], bins=20)
plt.title('Distribution of Uber miles')
plt.xlabel('Miles')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




