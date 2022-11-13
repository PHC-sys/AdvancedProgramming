import pandas as pd

class president:
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 1
        self.rankName = 'President'
        self.totalWage = totalWage

        basic_wage = (20000/73000) * totalWage
        bonus_wage = (15000/73000) * totalWage
        sup1 = (13000/73000) * totalWage
        sup2 = (10000/73000) * totalWage
        sup3 = (8000/73000) * totalWage
        sup4 = (5000/73000) * totalWage
        sup5 = (2000/73000) * totalWage

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = sup3
        self.sup4 = sup4
        self.sup5 = sup5

    def modifyWage(self):
        if self.rank != 1:
            self.totalWage = self.totalWage*(0.95**(self.rank-1))
            return self.totalWage

    def eachWage(self):
        return [self.rankName, self.totalWage, self.basicWage, self.bonusWage, self.sup1, self.sup2, self.sup3, self.sup4, self.sup5]

class vicePresident(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 2
        self.rankName = 'Vice President'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = (20000 / 73000) * totalWage
        bonus_wage = (15000 / 73000) * totalWage
        sup1 = (13000 / 73000) * totalWage
        sup2 = (10000 / 73000) * totalWage
        sup3 = (8000 / 73000) * totalWage
        sup4 = (5000 / 73000) * totalWage
        sup5 = (2000 / 73000) * totalWage

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = sup3
        self.sup4 = sup4
        self.sup5 = 'N/A'

class dean(president):
    def __init__(self, name, tw):
        self.name = name
        self.rank = 3
        self.rankName = 'Dean'
        self.totalWage = tw
        tw = super().modifyWage()

        bw = (20000 / 73000) * tw
        bow = (15000 / 73000) * tw
        sup1 = (13000 / 73000) * tw
        sup2 = (10000 / 73000) * tw
        sup3 = (8000 / 73000) * tw
        sup4 = (5000 / 73000) * tw
        sup5 = (2000 / 73000) * tw

        self.basicWage = bw
        self.bonusWage = bow
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = sup3
        self.sup4 = 'N/A'
        self.sup5 = 'N/A'

class chairMan(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 4
        self.rankName = 'Chairman'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = (20000 / 73000) * totalWage
        bonus_wage = (15000 / 73000) * totalWage
        sup1 = (13000 / 73000) * totalWage
        sup2 = (10000 / 73000) * totalWage
        sup3 = (8000 / 73000) * totalWage
        sup4 = (5000 / 73000) * totalWage
        sup5 = (2000 / 73000) * totalWage

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = 'N/A'
        self.sup4 = 'N/A'
        self.sup5 = 'N/A'

class professor(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 5
        self.rankName = 'Professor'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = (20000 / 73000) * totalWage
        bonus_wage = (15000 / 73000) * totalWage
        sup1 = (13000 / 73000) * totalWage
        sup2 = (10000 / 73000) * totalWage
        sup3 = (8000 / 73000) * totalWage
        sup4 = (5000 / 73000) * totalWage
        sup5 = (2000 / 73000) * totalWage

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = 'N/A'
        self.sup3 = 'N/A'
        self.sup4 = 'N/A'
        self.sup5 = 'N/A'

class assistant(president):
    def __init__(self,name, totalWage):
        self.name = name
        self.rank = 6
        self.rankName = 'Assistant'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = totalWage*0.4
        bonus_wage = totalWage*0.6

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = 'N/A'
        self.sup2 = 'N/A'
        self.sup3 = 'N/A'
        self.sup4 = 'N/A'
        self.sup5 = 'N/A'

totalWage = 73000

president = president('President', totalWage)
vicePresident1 = vicePresident('Vice President', totalWage)
vicePresident2 = vicePresident('Vice President', totalWage)
dean1 = dean('Dean', totalWage)
dean2 = dean('Dean', totalWage)
dean3 = dean('Dean', totalWage)
chairMan1 = chairMan('Chairman', totalWage)
chairMan2 = chairMan('Chairman', totalWage)
chairMan3 = chairMan('Chairman', totalWage)
chairMan4 = chairMan('Chairman', totalWage)
'''
professor1 = professor('Professor1', totalWage)
professor2 = professor('Professor2', totalWage)
assistant1 = assistant('Assistant1', totalWage)
assistant2 = assistant('Assistant2', totalWage)
'''
checkList = [president, vicePresident1, vicePresident2, dean1, dean2, dean3, chairMan1, chairMan2, chairMan3, chairMan4]

data = {}

for i in range(len(checkList)):
    each_list = checkList[i].eachWage()
    data[checkList[i].name] = each_list

df = pd.DataFrame(data, index=['Rank', 'Total Wage', 'Basic Wage', 'Bonus Wage', 'Sup1', 'Sup2', 'Sup3', 'Sup4', 'Sup5']).T
pd.set_option('display.max_columns', None)

print(df['Total Wage'].iloc[0:10])

df.to_csv('C:/Users/john/PycharmProjects/pythonProject/2019147006_0921.csv')
