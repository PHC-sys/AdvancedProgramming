import pandas as pd

df = pd.read_csv('temperature_data_set.csv',skiprows=7 , index_col=0, usecols=['Date', 'AverageTemp'])
df = df.drop(index= [df.index[-1],df.index[0]])

index_list = df.index
new_index_list = list()

for index in index_list:
    index = index.replace('\t','')
    new_index_list.append(index)

df.index = new_index_list
rows = len(df)

temp_2017 = list()
temp_2018 = list()
temp_2019 = list()
temp_2020 = list()
temp_2021 = list()

for row in range(rows):
    date = df.iloc[row].name

    if '2017' in date:
        temp_2017.append(df.iloc[row])
    elif '2018' in date:
        temp_2018.append(df.iloc[row])
    elif '2019' in date:
        temp_2019.append(df.iloc[row])
    elif '2020' in date:
        temp_2020.append(df.iloc[row])
    else:
        temp_2021.append(df.iloc[row])

df_temp_2017 = pd.DataFrame(temp_2017)
df_temp_2018 = pd.DataFrame(temp_2018)
df_temp_2019 = pd.DataFrame(temp_2019)
df_temp_2020 = pd.DataFrame(temp_2020)
df_temp_2021 = pd.DataFrame(temp_2021)

import numpy as np

avg_temp_2017 = np.mean(temp_2017)
avg_temp_2018 = np.mean(temp_2018)
avg_temp_2019 = np.mean(temp_2019)
avg_temp_2020 = np.mean(temp_2020)
avg_temp_2021 = np.mean(temp_2021)

avg_temp_dic = {
    '2017':avg_temp_2017,
    '2018':avg_temp_2018,
    '2019':avg_temp_2019,
    '2020':avg_temp_2020,
    '2021':avg_temp_2021
}
avg_temp = np.array(list(avg_temp_dic.values())).mean()

print("Forecasting for 2022: ", avg_temp,"degrees Celcius")

import matplotlib.pyplot as plt

x_axis = np.arange(5)
#print(avg_temp_dic.values())

plt.bar(x_axis, list(avg_temp_dic.values()))
plt.xticks(x_axis, avg_temp_dic.keys())

for i, v in enumerate(x_axis):
    y = list(avg_temp_dic.values())
    plt.text(v, y[i], round(y[i],2), horizontalalignment='center', verticalalignment='bottom')

plt.show()
