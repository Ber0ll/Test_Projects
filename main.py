# Stage-1 Data download and save i JSON file
# Stage-2 Crypto fear and greed index graph
# Stage-3 Polkadot and ETH pair value comparrision
# Stage-4 GUI

import json
import requests
import matplotlib import pyplot as plt
# Function definition

# Download data form API
def download_data():
    data_set = requests.get("https://api.alternative.me/fng/?limit=30&format=json&date_format=world")
    print(data_set.status_code)
    data = data_set.json()
    return data

#cleaning data set from usless information
def sorting_data(data_set):
    value_list =[]
    print(type(data_set))
    value = data_set['data'] #obtaining the main set of data

    #creating new dictionary with most important informations
    data_dic = {}
    for i in range(0,len(value)):
        data_dic[data_set['data'][i]['timestamp']] = data_set['data'][i]['value']
    return data_dic

# Program sequence
data_base = sorting_data(download_data())
print(data_base)

with open("Sorted_data.json", "w") as f:
    json.dump(data_base, f)


