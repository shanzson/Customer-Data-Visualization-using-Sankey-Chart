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

# Plotting Histograms
num_bins = 100
from_data = data['To']
legend = ['To']
plt.hist([from_data], bins = num_bins, color=['Orange'])
plt.xlabel("To data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()

num_bins = 100
from_data = data['From']
legend = ['From']
plt.hist([from_data], bins = num_bins, color=['green'])
plt.xlabel("From data")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()

num_bins = 100
from_data = data['userid']
legend = ['userid']
plt.hist([from_data], bins = num_bins, color=['Red'])
plt.xlabel("userid")
plt.ylabel("Frequency")
plt.legend(legend)
plt.show()