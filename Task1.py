
# coding: utf-8

# In[52]:


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


# In[53]:


num_bins = 100
to_data = data['To']
legend = ['To']
plt.hist([to_data], bins = num_bins, color=['Orange'])
plt.xlabel("To data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[54]:


num_bins = 100
from_data = data['From']
legend = ['From']
plt.hist([from_data], bins = num_bins, color=['green'])
plt.xlabel("From data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[55]:


num_bins = 200
userid_data = data['userid']
legend = ['userid']
plt.hist([userid_data], bins = num_bins, color=['Red'])
plt.xlabel("userid")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[56]:


print('Sorting...')
data.sort_values(['userid', 'From', 'To'], ascending=[True, True, True], inplace=True)
# grouped = data.groupby('userid')
# grouped.head()


# In[57]:


plt.boxplot(data['To'])


# In[58]:


plt.boxplot(data['From'])


# In[59]:


data = data.sort_values('userid')

region_rank = []
for i in range(99, 210, 5):
    region_rank.append(i)

print(region_rank)

def mark_region(x):
    current_rank = 0
    for i in region_rank:
        if(x > i):
            current_rank+=1
        else: 
            return current_rank
    
    
# Apply the mark_region function 
data['source_to'] = data['To'].apply(mark_region)
data['target_from'] = data['From'].apply(mark_region)

# Confirming the absence of NAN values
print("Presence of NAN values : \n", data.isnull().any())
data.head(100)


# In[62]:


max_region = data['source_to'].max()
print(max_region)


# In[65]:


label = []
for i in range(1, max_region+1):
    label.append(str(i))
print(label)
    
node = dict(
    pad = 15,
    thickness = 20,
    line = dict(color = "black", width = 0.5),
    label = label,
    color = "blue"
)

# output = dict()
# output.update({'nodes_dict': dict()})
# i = 0
    
# output.update({'links_dict': dict()})

# def update_source_target(user):
#     try:
#         source_index
        
# grouped.apply(lambda user: update_source_target(user)) 

