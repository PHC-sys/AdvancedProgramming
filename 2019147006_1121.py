import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

from statsmodels.api import OLS, add_constant
import pandas_datareader.data as web

from linearmodels.asset_pricing import LinearFactorModel

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

#Predicting with FamaFrench Regression Model

sns.set_style('whitegrid')

ff_factor = 'F-F_Research_Data_5_Factors_2x3'
ff_factor_data = web.DataReader(ff_factor, 'famafrench', start='2010', end='2017-12')[0]
ff_factor_data.info()
ff_factor_data.describe()

ff_portfolio = '17_Industry_Portfolios'
ff_portfolio_data = web.DataReader(ff_portfolio, 'famafrench', start='2010', end='2017-12')[0]
ff_portfolio_data = ff_portfolio_data.sub(ff_factor_data.RF, axis=0)
ff_portfolio_data.info()
ff_portfolio_data.describe()


#Download the file in https://data.nasdaq.com/publishers/QDL
#Aftr that, transform the csv file to h5 file
#Make a prediction of Daily Return with regression

with pd.HDFStore('../data/assets.h5') as store:
    prices = store['/quandl/wiki/prices'].adj_close.unstack().loc['2010':'2017']
    equities = store['/us_equities/stocks'].drop_duplicates()

sectors = equities.filter(prices.columns, axis=0).sector.to_dict()
prices = prices.filter(sectors.keys()).dropna(how='all', axis=1)

returns = prices.resample('M').last().pct_change().mul(100).to_period('M')
returns = returns.dropna(how='all').dropna(axis=1)
returns.info()

ff_factor_data = ff_factor_data.loc[returns.index]
ff_portfolio_data = ff_portfolio_data.loc[returns.index]

ff_portfolio_data.describe()
ff_factor_data.describe()

excess_returns = returns.sub(ff_factor_data.RF, axis=0)
excess_returns.info()

excess_returns = excess_returns.clip(lower=np.percentile(excess_returns, 1),
                                     upper=np.percentile(excess_returns, 99))
print(excess_returns)

ff_factor_data = ff_factor_data.drop('RF', axis=1)

#Execute Cross-Validation

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True).fit(ff_portfolio_data,ff_factor_data)
cv = KFold(5, shuffle=True, random_state=0) # 80% for train data, 20% for test data

r2_scores = cross_val_score(model, ff_portfolio_data, ff_factor_data, scoring="r2", cv=cv)
r2_score = np.mean(r2_scores)

print(model)
print(f"Correlation by each Fold: {np.round(r2_scores,3)}")
print(f"Mean of Corrleation: {r2_score:.3f}")