import pandas as pd

df = pd.read_csv('resultsQS2022ranking.csv',encoding='cp949', index_col=0, usecols=[0,1,2], nrows = 500)

institution = df.columns[0]
country = df.columns[1]
df[institution] = df[institution].str.replace(" ", "")
df[country] = df[country].str.replace(" ", "")

#Total Sum of Rank
total = sum(df.index)
print('Total Sum of Rank: ', total, '\n')

#Smallest Rank(Top)
top_index = df.index[0]
print('Smallest Rank School: ',df.loc[top_index, institution], '\n')

#Largest Rank(Bottom)
#There is joint ranking
bot_index = df.index[-1]
print('Largest Rank Schools: ',df.loc[bot_index, institution], '\n')

#Finding School Name
mySchoolName = 'YonseiUniversity'
mySchoolColumn = df.loc[df[institution] == mySchoolName]
mySchoolRank = mySchoolColumn.index[0]
jointRankingNumber = len(df.loc[mySchoolRank, institution])
mySchoolRank += jointRankingNumber - 1

schoolNameList = df[institution].iloc[0:mySchoolRank]
print(schoolNameList, '\n')
print(type(schoolNameList))
print('My School Name is: ', schoolNameList.iloc[mySchoolRank-1:mySchoolRank].values)
