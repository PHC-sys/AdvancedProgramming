import pandas as pd
#The file is same as 2019147006_0921
class president:
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 1
        self.rankName = 'President'
        self.totalWage = totalWage

        basic_wage = totalWage*0.5
        bonus_wage = totalWage*0.25
        sup1 = totalWage*0.07
        sup2 = totalWage*0.06
        sup3 = totalWage*0.06
        sup4 = totalWage*0.06

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = sup3
        self.sup4 = sup4

    def modifyWage(self):
        if self.rank != 1:
            self.totalWage = self.totalWage*(0.9**(self.rank-1))
            return self.totalWage

    def eachWage(self):
        return [self.rankName, self.totalWage, self.basicWage, self.bonusWage, self.sup1, self.sup2, self.sup3, self.sup4]

class vicePresident(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 2
        self.rankName = 'Vice President'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = totalWage*0.5
        bonus_wage = totalWage*0.25
        sup1 = totalWage*0.09
        sup2 = totalWage*0.08
        sup3 = totalWage*0.08

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = sup3
        self.sup4 = 'N/A'

class dean(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 3
        self.rankName = 'Dean'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = totalWage*0.5
        bonus_wage = totalWage*0.25
        sup1 = totalWage*0.125
        sup2 = totalWage*0.125

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = sup2
        self.sup3 = 'N/A'
        self.sup4 = 'N/A'

class chairMan(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 4
        self.rankName = 'Chairman'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = totalWage*0.5
        bonus_wage = totalWage*0.25
        sup1 = totalWage*0.25

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = sup1
        self.sup2 = 'N/A'
        self.sup3 = 'N/A'
        self.sup4 = 'N/A'

class professor(president):
    def __init__(self, name, totalWage):
        self.name = name
        self.rank = 5
        self.rankName = 'Professor'
        self.totalWage = totalWage
        totalWage = super().modifyWage()

        basic_wage = totalWage*0.5
        bonus_wage = totalWage*0.5

        self.basicWage = basic_wage
        self.bonusWage = bonus_wage
        self.sup1 = 'N/A'
        self.sup2 = 'N/A'
        self.sup3 = 'N/A'
        self.sup4 = 'N/A'

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

totalWage = 20000

pre = 'President'
d = 'Dean'
cm = 'Chairman'
pf = 'Professor'
a = 'Assistant'

president = president(pre, totalWage)
vicePresident = vicePresident('Vice '+ pre, totalWage)
dean1 = dean(d + '1', totalWage)
dean2 = dean(d + '2', totalWage)
chairMan1 = chairMan(cm +'1', totalWage)
chairMan2 = chairMan(cm +'2', totalWage)
professor1 = professor(pf + '1', totalWage)
professor2 = professor(pf + '2', totalWage)
assistant1 = assistant(a + '1', totalWage)
assistant2 = assistant(a + '2', totalWage)

checkList = [president, vicePresident, dean1, dean2, chairMan1, chairMan2, professor1, professor2, assistant1, assistant2]

data = {}

for i in range(len(checkList)):
    each_list = checkList[i].eachWage()
    data[checkList[i].name] = each_list

df = pd.DataFrame(data, index=['Rank', 'Total Wage', 'Basic Wage', 'Bonus Wage', 'Sup1', 'Sup2', 'Sup3', 'Sup4']).T
pd.set_option('display.max_columns', None)

print(df)

df.to_csv('C:/Users/john/PycharmProjects/pythonProject/2019147006_0921.csv')
