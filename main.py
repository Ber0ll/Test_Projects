# Stage-1 Data download (done)
# Stage-2 Cleaning data (done)
# Stage-3 Crypto fear and greed index graph (done)
# Stage-4 Data set saving mechanism
# Stage-5 Polkadot and ETH pair value comparrision
# Stage-6 GUI

import json
import requests
from matplotlib import pyplot as plt


# Function definition

# Download data form API
def download_data():
    data_set = requests.get("https://api.alternative.me/fng/?limit=20&format=json&date_format=world")
    print(data_set.status_code)
    data = data_set.json()
    return data


# cleaning data set from useless information
def sorting_data(data_set):
    print(type(data_set))
    value = data_set['data']  # obtaining the main set of data

    # creating new dictionary with most important information
    data_dic = {}
    # iterating backwards, so the newest records are on the end of the dictionary (so I can add newer one easily)
    for i in range(len(value)-1,-1,-1):
        data_dic[data_set['data'][i]['timestamp']] = data_set['data'][i]['value']
    return data_dic

#saving data
def checking_function(data_to_check):
    try:
        with open("data_set.json","r") as arch_data:
           old_data = json.load(arch_data)
        arch_data.close()
        print("File Founded")
    except:
        with open("data_set.json","w") as arch_data:
            json.dump(data_to_check,arch_data)
        arch_data.close()
        print("New File Created")
        return

    print(old_data)

    j = 0
    for i in data_to_check:
        if i in old_data:
            continue
        else:
            old_data[i] = data_to_check[i]
            j+=1
    if j > 0:
        with open("data_set.json","w") as arch_data:
            json.dump(old_data,arch_data)
        arch_data.close()
        print("New data have been saved!")
    else:
        print("New records not found!")

# Program sequence

    #1.Download Data
downloaded_data = download_data()

    #2.Sorting_Data
data_base = sorting_data(downloaded_data)
print(type(data_base))

    #3.Saving Data
checking_function(data_base)



a = [""]
b = [""]
for x, y in data_base.items():
    a.append(str(x))
    b.append(int(y))

a.pop(0)
b.pop(0)

plt.plot(a,b)
plt.title("Fear and Greed index in las mounth",loc= 'left')
plt.xticks(rotation = 90, fontsize=8)
plt.show()