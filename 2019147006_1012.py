import pandas as pd
import csv

read_file_name = "email_address_list" # the filename of 1005 assignment
rewrite_file_name = "email_w_name_list"
name = ["", "Alanis", "Brown", "Chaney", "Daniel", "Fosth", "Hussey", "Potzler", "Aponte", "Lim", "Blanchard"]

df = pd.read_csv(read_file_name, index_col=0)
df['Name'] = pd.Series(name)

df.to_csv(rewrite_file_name)

df2 = pd.read_csv(rewrite_file_name, index_col=0)
name_list = df2['Name']

for name in name_list:
    print(f"Happy Birthday {name}! Have a nice day!")

f = open(rewrite_file_name, 'r', encoding = 'utf-8--sig')
rdr = csv.reader(f)

data = list()

for row in rdr:
    data.append(row)

print(data)
