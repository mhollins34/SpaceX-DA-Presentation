#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.head(50)

df['Landing_Outcome'].value_counts()


# In[5]:


import csv, sqlite3
import pandas as pd
con = sqlite3.connect("my_data1.db")
cur = con.cursor()
get_ipython().run_line_magic('sql', 'sqlite:///my_data1.db')



# ## TASK 1 
# Display the names of the unique launch sites in the space mission

# In[6]:


get_ipython().run_line_magic('sql', 'SELECT DISTINCT ("Launch_Site") from SPACEXTBL;')


# ## TASK 2
# Display 5 records where launch sites begin with the string 'CCA'
# 

# In[32]:


get_ipython().run_line_magic('sql', 'SELECT ("Launch_Site") from SPACEXTBL WHERE  "Launch_Site" LIKE \'%CCA%\' LIMIT 5;')


# ## TASK 3 
# Display the total payload mass carried by boosters launched by NASA (CRS)

# In[9]:


get_ipython().run_line_magic('sql', 'SELECT SUM ("PAYLOAD_MASS__KG_") from SPACEXTBL WHERE "Customer" LIKE \'%CRS%\';')


# ## TASK 4
# Display average payload mass carried by booster version F9 v1.1

# In[10]:


get_ipython().run_line_magic('sql', 'SELECT AVG ("PAYLOAD_MASS__KG_") from SPACEXTBL WHERE "Booster_Version" = \'F9 v1.1\';')


# ## TASK 6
# List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000

# In[31]:


get_ipython().run_line_magic('sql', 'SELECT ("Booster_Version") from SPACEXTBL WHERE "Landing_Outcome" = \'Success (drone ship)\' AND "PAYLOAD_MASS__KG_" >4000<6000;')


# ## TASK 7
# List the total number of successful and failure mission outcomes

# In[11]:


get_ipython().run_line_magic('sql', 'SELECT COUNT (Mission_Outcome) from SPACEXTBL;')


# ## TASK 8
# List the names of the booster_versions which have carried the maximum payload mass. Use a subquery

# In[20]:


get_ipython().run_line_magic('sql', 'SELECT ("Booster_Version") from SPACEXTBL WHERE ("PAYLOAD_MASS__KG_") = (SELECT MAX("PAYLOAD_MASS__KG_") from SPACEXTBL);')


# ## TASK 9
# List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.
# 
# Note: SQLLite does not support monthnames. So you need to use substr(Date, 4, 2) as month to get the months and substr(Date,7,4)='2015' for year.

# In[37]:


get_ipython().run_line_magic('sql', 'SELECT ("Date"),("Booster_Version"),("Launch_Site"),("Landing_Outcome") from SPACEXTBL WHERE "Landing_Outcome"= \'Failure (drone ship)\' and substr("Date", 4, 2) and substr("Date", 1, 4)=\'2015\';')


# ## TASK 10
# Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order.

# In[28]:


get_ipython().run_line_magic('sql', 'SELECT ("Date"),("Landing_Outcome") from SPACEXTBL WHERE "Date" BETWEEN \'2010-06-04\' AND \'2017-03-20\' and "Landing_Outcome" = \'Failure (drone ship)\' ORDER BY "Date" DESC;')


# In[ ]:




