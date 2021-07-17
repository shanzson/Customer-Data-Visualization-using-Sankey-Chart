import pandas as pd

data = pd.read_csv('sharechat_data.csv')[
    ['userid', 'From', 'To']]

print(data.head(10))

# Checking if there are NAN values
print(data.isnull().any())

def remove_letter(val):
    if(val[0] == 'F' or val[0] == 'T'):
        return val[1:]

data['From'] = data['From'].apply(remove_letter)
data['To'] = data['To'].apply(remove_letter)

print(data.head(10))








