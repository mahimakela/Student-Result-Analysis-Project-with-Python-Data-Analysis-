#!/usr/bin/env python
# coding: utf-8

# # BEST PYTHON PROJECT:
#     STUDENT RESULT ANALYSIS PROJECT WITH PYTHON AND DATA ANALYSIS

# In[53]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




df=pd.read_csv("student_scores.csv.csv")
df


# In[54]:


print(df.head())


# In[55]:


print(df.describe())


# In[56]:


df.describe()


# In[57]:


df.info()


# In[58]:


df.isnull().sum()


# # drop unnamed column

# In[59]:


df=df.drop("Unnamed: 0",axis=1)
print(df.head())


# # Gender distribution

# In[66]:


plt.figure(figsize=(5, 5))
ax = sns.countplot(data=df, x='Gender')
ax.bar_label(ax.containers[0])

plt.title("Gender Distribution", fontsize=14, weight='bold', pad=20)
plt.xlabel('Gender')
plt.ylabel('Count')

plt.show()


# Based on the analysis of the count plot,
# it is evident that the dataset contains a higher number of females compared to males.
# 
# 

# In[61]:


gb= df.groupby("ParentEduc").agg({"MathScore":"mean" , "ReadingScore":"mean" ,"WritingScore":"mean"  })
print(gb)


# In[65]:


plt.figure(figsize=(6, 5)) 
ax = sns.heatmap(data=gb, annot=True)
plt.title("Relationship Between Parents' Education and Student Scores")   
plt.show()


# From the chart above, we can conclude that the education level of the parents is positively associated with higher scores.

# In[63]:


gb1= df.groupby("ParentMaritalStatus").agg({"MathScore":"mean" , "ReadingScore":"mean" ,"WritingScore":"mean"  })
print(gb1)


# In[68]:


plt.figure(figsize=(5, 5))  
sns.heatmap(data=gb1, annot=True)
plt.title("Relationship Between Parents' Marital Status and Student Score", fontsize=14, weight='bold', pad=15)
plt.show()


# From the chart above, we can conclude that the marital status of the parents has a negligible impact on the students' scores.

# In[69]:


gb2= df.groupby("IsFirstChild").agg({"MathScore":"mean" , "ReadingScore":"mean" ,"WritingScore":"mean"  })
print(gb2)


# In[73]:


plt.figure(figsize=(8, 6)) 
ax = sns.barplot(data=gb2)
ax.bar_label(ax.containers[0])


# # Distribution of ethnic group

# In[76]:


groupA=df.loc[(df["EthnicGroup"] == "group A")].count()
print(groupA)


# In[77]:


groupB=df.loc[(df["EthnicGroup"] == "group B")].count()
print(groupB)


# In[78]:


groupC=df.loc[(df["EthnicGroup"] == "group C")].count()
print(groupC)


# In[79]:


groupD=df.loc[(df["EthnicGroup"] == "group D")].count()
print(groupD)


# In[80]:


groupE=df.loc[(df["EthnicGroup"] == "group E")].count()
print(groupE)


# In[89]:


counts = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]


labels = ["Group A", "Group B", "Group C", "Group D", "Group E"]

plt.figure(figsize=(8, 8)) 
plt.pie(counts, labels=labels, autopct="%1.2f%%", startangle=140)

plt.title("Distribution of Ethnic Groups")

plt.show()


# In[98]:


ax= sns.countplot(data=df,x="EthnicGroup")
ax.bar_label(ax.containers[0])


# Thank you for taking the time to review my Python-based student analysis project. Your feedback on the data analysis methodologies and code implementation is highly valued.

# In[ ]:




