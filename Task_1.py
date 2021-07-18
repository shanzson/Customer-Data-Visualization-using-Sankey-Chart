
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')[
    ['userid', 'From', 'To']]

print(data.head(10))

# Checking if there are NAN values
print("Presence of NAN values : \n", data.isnull().any())

# Function to remove letter from column data
def remove_letter(val):
    if(val[0] == 'F' or val[0] == 'T'):
        return val[1:]

data['From'] = data['From'].apply(remove_letter)
data['To'] = data['To'].apply(remove_letter)

print(data.head(10))

print(data.dtypes)

# Converting object datatype to int
data['From'] = data['From'].astype(str).astype(int)
data['To'] = data['To'].astype(str).astype(int)

print(data.dtypes)


# In[ ]:


num_bins = 100
to_data = data['To']
legend = ['To']
plt.hist([from_data], bins = num_bins, color=['Orange'])
plt.xlabel("To data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[ ]:


num_bins = 100
from_data = data['From']
legend = ['From']
plt.hist([from_data], bins = num_bins, color=['green'])
plt.xlabel("From data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[41]:


num_bins = 200
userid_data = data['userid']
legend = ['userid']
plt.hist([userid_data], bins = num_bins, color=['Red'])
plt.xlabel("userid")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[32]:


print('Sorting...')
data.sort_values(['userid', 'From', 'To'], ascending=[True, True, True], inplace=True)
grouped = data.groupby('userid')
data.to_csv(r'C:\Users\Shantanu\Desktop\Interview_Bit\Sharechat_code_backup\ShareChat\Intermediate_outputs\grouped_data.csv', index = False)
grouped.head()


# In[4]:


plt.boxplot(data['To'])


# In[5]:


plt.boxplot(data['From'])


# In[12]:


data = data.sort_values('userid').drop_duplicates('userid')
data.head()

print('Working...')
def add_source(x): 
    # return x['time_event'].rank(method='first').astype(int)
    print('Calling...')
    if(151 <= x['To'] <= 200):
        return 4

# Apply the add_source function 
# data['source_to'] = data.apply(add_source).reset_index(0, drop=True)

data.head()