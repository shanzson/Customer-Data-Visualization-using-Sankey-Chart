
# coding: utf-8

# In[1]:


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


# In[2]:


num_bins = 100
to_data = data['To']
legend = ['To']
plt.hist([to_data], bins = num_bins, color=['Orange'])
plt.xlabel("To data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[3]:


num_bins = 100
from_data = data['From']
legend = ['From']
plt.hist([from_data], bins = num_bins, color=['green'])
plt.xlabel("From data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[4]:


num_bins = 200
userid_data = data['userid']
legend = ['userid']
plt.hist([userid_data], bins = num_bins, color=['Red'])
plt.xlabel("userid")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()


# In[5]:


print('Sorting...')
data.sort_values(['userid', 'From', 'To'], ascending=[True, True, True], inplace=True)
# grouped = data.groupby('userid')
# grouped.head()


# In[6]:


plt.boxplot(data['To'])


# In[7]:


plt.boxplot(data['From'])


# In[12]:


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


# In[9]:


max_region = data['source_to'].max()
print(max_region)


# In[27]:


label = []
for i in range(1, max_region + 1):
    label.append(str(i))
print(label)



# Creating source, target and value lists
source = []
target = []
value = []

source = data['source_to'].values.tolist()
print('Source:\n')
print(source)

target = data['target_from'].values.tolist()
print('\n Targets:\n')
print(target)

print("length of source list is: ", len(source))
print("length of target list is: ", len(target))

for i in range(len(source)):
    value.append(1)

#################### Sankey Diagram Trial 1##################

output = dict()

output.update({'links_dict': dict()})

def update_source_target(src, t):
    try:
        print(src, t)
        # If this source is already in links_dict...
        if src in output['links_dict']:
            if t in output['links_dict'][src]:
                # Increment count of users with this source/target pair by 1,
                output['links_dict'][src][t]['unique_users'] += 1
            # but if the target is not already associated to this source...
            else:
                 # ...we create a new key for this target, for this source, and initiate it with 1 user and the time from source to target
                output['links_dict'][src].update({t:
                    dict(
                        {'unique_users': 1
                        })
                })
        # ...but if this source isn't already available in the links_dict, we create its key and the key of this source's target, and we initiate it with 1 user and the time from source to target
        else:
            output['links_dict'].update({src: dict({t: dict(
                {'unique_users': 1})})})

    except Exception as e:
        pass

data2 = data.apply(lambda x: update_source_target(x['source_to'], x['target_from']), axis = 1)

print('Lambda Function Working... \n\n')
for key, value in output['links_dict'].items():
    print(key, value)


# In[137]:


import plotly.graph_objects as go

node = dict(
    pad = 15,
    thickness = 20,
    line = dict(color = "black", width = 0.5),
    label = label,
    color = "blue"
)

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = label,
      color = "blue"
    ),
    link = dict(
    source = source, 
    target = target,
    value = value
))])

fig.update_layout(autosize=True, title_text="Medium app", font=dict(size=15))
fig.show()
    


# In[139]:


import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()

