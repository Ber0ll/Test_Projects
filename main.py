# Stage-1 Data download (done)
# Stage-2 Cleaning data (done)
# Stage-3 Crypto fear and greed index graph (done)
# Stage-4 Data set saving mechanism (done)
# Stage-6 GUI

import json
import requests
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd


# Function definition

# Download data form API
def download_data():
    data_set = requests.get("https://api.alternative.me/fng/?limit=30&format=json&date_format=world")

    if data_set.status_code == 200:
        print("Data downloaded successfully")
    else:
        print("Server error")
    data = data_set.json()
    return data


# cleaning data set from useless information
def cleaning_data(data_set):
    value = data_set['data']  # obtaining the main set of data

    # creating new dictionary with most important information
    data_dic = {}
    # iterating backwards, so the newest records are on the end of the dictionary (so I can add newer one easily)
    for i in range(len(value) - 1, -1, -1):
        data_dic[data_set['data'][i]['timestamp']] = data_set['data'][i]['value']
    return data_dic


# saving data
def checking_function(data_to_check):
    try:
        with open("data_set.json", "r") as arch_data:
            old_data = json.load(arch_data)
        arch_data.close()
        print("File Founded")
    except:
        with open("data_set.json", "w") as arch_data:
            json.dump(data_to_check, arch_data)
        arch_data.close()
        print("New File Created")
        return

    added_new_content = False

    for i in data_to_check:
        if i in old_data:
            continue
        else:
            old_data[i] = data_to_check[i]
            added_new_content = True
    if added_new_content:
        with open("data_set.json", "w") as arch_data:
            json.dump(old_data, arch_data)
        arch_data.close()
        print("New data have been saved!")
    else:
        print("New records not found!")


def sorting_function():
    # opening file
    with open("data_set.json", "r") as arch_data:
        unsorted_data = json.load(arch_data)
        arch_data.close()
        # sorting
        sorted_data = dict(sorted(unsorted_data.items(), key=lambda x: datetime.strptime(x[0], "%d-%m-%Y")))

    with open("data_set.json", "w") as arch_data:
        json.dump(sorted_data, arch_data)
    arch_data.close()
    print("Sorted data saved")
    return sorted_data


def plotting_function(data_to_plot):
    a = [""]
    b = [""]
    for x, y in data_to_plot.items():
        a.append(str(x))
        b.append(int(y))

    a.pop(0)
    b.pop(0)

    plt.plot(a, b)
    plt.title("Fear and Greed index in last month", loc='left')
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    plt.show()


def pandas_table_test(data_to_show):
    print(pd.DataFrame.from_dict(data_to_show, orient='index'))


# Program sequence

# 1.Download Data
downloaded_data = download_data()

# 2.Cleaning_Data
data_base = cleaning_data(downloaded_data)
print(type(data_base))

# 3.Saving Data
checking_function(data_base)

# 4. Sorting Data
sorted_data = sorting_function()

# 5. Plotting function
pandas_table_test(sorted_data)

plotting_function(sorted_data)


