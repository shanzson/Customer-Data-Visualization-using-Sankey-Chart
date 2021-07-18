# coding: utf-8

# In[126]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')[
    ['userid', 'From', 'To']]

print(data.head(10))

# Checking if there are NAN values
print("Presence of NAN values : \n", data.isnull().any())


# Function to remove letter from column data
def remove_letter(val):
    if (val[0] == 'F' or val[0] == 'T'):
        return val[1:]


data['From'] = data['From'].apply(remove_letter)
data['To'] = data['To'].apply(remove_letter)

print(data.head(10))

print(data.dtypes)

# Converting object datatype to int
data['From'] = data['From'].astype(str).astype(int)
data['To'] = data['To'].astype(str).astype(int)

print(data.dtypes)

# In[127]:


num_bins = 100
to_data = data['To']
legend = ['To']
plt.hist([to_data], bins=num_bins, color=['Orange'])
plt.xlabel("To data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()

# In[128]:


num_bins = 100
from_data = data['From']
legend = ['From']
plt.hist([from_data], bins=num_bins, color=['green'])
plt.xlabel("From data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()

# In[129]:


num_bins = 200
userid_data = data['userid']
legend = ['userid']
plt.hist([userid_data], bins=num_bins, color=['Red'])
plt.xlabel("userid")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()

# In[130]:


print('Sorting...')
data.sort_values(['userid', 'From', 'To'], ascending=[True, True, True], inplace=True)
# grouped = data.groupby('userid')
# grouped.head()


# In[131]:


plt.boxplot(data['To'])

# In[132]:


plt.boxplot(data['From'])

# In[133]:


data = data.sort_values('userid')

region_rank = []
for i in range(99, 210, 5):
    region_rank.append(i)

print(region_rank)


def mark_region(x):
    current_rank = 0
    for i in region_rank:
        if (x > i):
            current_rank += 1
        else:
            return current_rank


# Apply the mark_region function
data['source_to'] = data['To'].apply(mark_region)
data['target_from'] = data['From'].apply(mark_region)

# Confirming the absence of NAN values
print("Presence of NAN values : \n", data.isnull().any())
data.head(100)

# In[134]:


max_region = data['source_to'].max()
print(max_region)

# In[135]:


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

# for i in range(0, len(source)):
#     try:
#         if source[i] not in output:
#             output[]

#     except Exception as e:
#         pass

# for key, value in output['comb_dict'].items():
#     print('key: ', key, ' value: ', value, '\n')

# def update_source_target(user):
#     try:
#         if source in output['links_dict']:
#             if target_index in output['links_dict'][source_index]:

# grouped.apply(lambda user: update_source_target(user))


# In[137]:


import plotly.graph_objects as go

node = dict(
    pad=15,
    thickness=20,
    line=dict(color="black", width=0.5),
    label=label,
    color="blue"
)

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=label,
        color="blue"
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    ))])

fig.update_layout(autosize=True, title_text="Medium app", font=dict(size=15))
fig.show()

