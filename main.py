# Stage-1 Data download
# Stage-2 Cleaning data
# Stage-3 Crypto fear and greed index graph
# Stage-4 Data set saving mechanism
# Stage-5 Polkadot and ETH pair value comparrision
# Stage-6 GUI

import json
import requests
from matplotlib import pyplot as plt


# Function definition

# Download data form API
def download_data():
    data_set = requests.get("https://api.alternative.me/fng/?limit=30&format=json&date_format=world")
    print(data_set.status_code)
    data = data_set.json()
    return data


# cleaning data set from usless information
def sorting_data(data_set):
    value_list = []
    print(type(data_set))
    value = data_set['data']  # obtaining the main set of data

    # creating new dictionary with most important informations
    data_dic = {}
    for i in range(0, len(value)):
        data_dic[data_set['data'][i]['timestamp']] = data_set['data'][i]['value']
    return data_dic


# Program sequence
data_base = sorting_data(download_data())
print(data_base)

with open("Sorted_data.json", "w") as f:
    json.dump(data_base, f)


a = [""]
b = [""]
for x, y in data_base.items():
    a.append(str(x))
    b.append(int(y))

a.pop(0)
b.pop(0)
a.reverse()
b.reverse()

print(a)
print(b)

plt.plot(a,b)
plt.title("Fear and Greed index in las mounth",loc= 'left')
plt.xticks(rotation = 90, fontsize=8)
plt.show()