#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
import seaborn as sns
import io

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
df


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 4)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()


# ### TASK 1: Visualize the relationship between Flight Number and Launch Site
# Use the function catplot to plot FlightNumber vs LaunchSite, set the parameter x parameter to FlightNumber,set the y to Launch Site and set the parameter hue to 'class

# In[60]:


sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 3)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("LaunchSite",fontsize=20)
plt.show()


# ### TASK 2: Visualize the relationship between Payload and Launch Site
# # Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value

# In[61]:


sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect = 3)
plt.xlabel("PayloadMass (kg) ",fontsize=20)
plt.ylabel("LaunchSite",fontsize=20)
plt.show()


# ## TASK 3: Visualize the relationship between success rate of each orbit type
# Let's create a bar chart for the sucess rate of each orbit

# In[4]:


df.groupby("Orbit")[("Class")].mean().plot(kind="bar")


# ### TASK  4: Visualize the relationship between FlightNumber and Orbit type
# # Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value

# In[62]:


sns.catplot(y="Orbit", x="FlightNumber", hue="Class", data=df, aspect = 3)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()


# ### TASK  5: Visualize the relationship between Payload and Orbit type
# # Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value

# In[63]:


sns.catplot(y="Orbit", x="PayloadMass", hue="Class", data=df, aspect = 3)
plt.xlabel("PayloadMass (kg)",fontsize=20)
plt.ylabel("Orbit",fontsize=20)
plt.show()


# ### TASK  6: Visualize the launch success yearly trend
# Plot a line chart with x axis to be Year and y axis to be average success rate, to get the average launch success trend.

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
df

year=[]
def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year
Extract_year()
df['Date'] = year
df.head(10)

df.groupby("Date")[("Class")].mean().plot(kind="line")
plt.xlabel("Date",fontsize=20)
plt.ylabel("Class",fontsize=20)
plt.title("Launch Success Trend")
plt.show()


# ## TASK 7 : Create dummy variables to categorical columns

# In[17]:


features = df[["FlightNumber", "PayloadMass", "Orbit", "LaunchSite", "Flights", "GridFins", "Reused", "Legs", "LandingPad", "Block", "ReusedCount", "Serial"]]
features

features_one_hot = pd.get_dummies(features, columns=["Orbit", "LaunchSite", "LandingPad", "Serial"], drop_first=True)
features_one_hot


# ### TASK  8: Cast all numeric columns to `float64`

# In[2]:


import pandas as pd

features_one_hot = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")

df2 = features_one_hot['PAYLOAD_MASS__KG_'].astype('float64')
df2


# In[ ]:




