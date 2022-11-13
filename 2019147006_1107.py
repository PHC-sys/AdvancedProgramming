import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

#Using LSTM method to train and test Samsung stock price
samsung_stock_price = yf.download('005930.KS',start = '2018-01-01')

#print(samsung_stock_price.tail())

plt.figure(figsize = (18,9))
plt.title('Samsung Stock Price')
df = samsung_stock_price.copy()
plt.plot(df.index,(df['Low']+df['High'])/2.0)
plt.xticks(df.iloc[::50,:].index,rotation=45)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)
#plt.show()

stockPriceClose=samsung_stock_price[['Close']]
split_date = pd.Timestamp('01-01-2022')

#Separate into train_data set and test_data set
train_data=pd.DataFrame(stockPriceClose.loc[:split_date,['Close']])
test_data=pd.DataFrame(stockPriceClose.loc[split_date:,['Close']])

#Check the separated data
ax = train_data.plot()
test_data.plot(ax=ax)
plt.legend(['train', 'test'])
#plt.show()

from sklearn.preprocessing import MinMaxScaler

#Scale the dataset for LSTM
scaler = MinMaxScaler()
train_data_sc=scaler.fit_transform(train_data)
test_data_sc= scaler.transform(test_data)

train_sc_df = pd.DataFrame(train_data_sc, columns=['Scaled'], index=train_data.index)
test_sc_df = pd.DataFrame(test_data_sc, columns=['Scaled'], index=test_data.index)

#Use 30days dataset for forecasting
for i in range(1, 31):
    train_sc_df ['Scaled_{}'.format(i)]=train_sc_df ['Scaled'].shift(i)
    test_sc_df ['Scaled_{}'.format(i)]=test_sc_df ['Scaled'].shift(i)

x_train=train_sc_df.dropna().drop('Scaled', axis=1)
y_train=train_sc_df.dropna()[['Scaled']]

x_test=test_sc_df.dropna().drop('Scaled', axis=1)
y_test=test_sc_df.dropna()[['Scaled']]

#Change the dataframe into ndarray format - for machine learning algorithm
x_train=x_train.values
x_test=x_test.values

y_train=y_train.values
y_test=y_test.values

#Make it appropriate for LSTM Model
x_train_t = x_train.reshape(x_train.shape[0], 30,1)
x_test_t = x_test.reshape(x_test.shape[0], 30, 1)

from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

K.clear_session()
# Sequeatial Model
model = Sequential()
# First LSTM Layer
model.add(LSTM(30,return_sequences=True, input_shape=(30, 1)))
# Second LSTM Layer
model.add(LSTM(42,return_sequences=False))
# The Forecasting data
model.add(Dense(1, activation='linear'))
# Loss Function - The erro between Forecasting and Actual data, using MSE
# Optimizer - Generally adam
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()

#Monitor the Loss, if the performance does not get better, cease the epoch
#Print 'vervose=1'
early_stop = EarlyStopping(monitor='loss', patience=5, verbose=1)

#epochs is the number of training, batch_size is the input data size in one iteration
model.fit(x_train_t, y_train, epochs=50,
          batch_size=20, verbose=1, callbacks=[early_stop])

y_pred = model.predict(x_test_t)

#Compare the forecast & the actual data of test data set
t_df=test_sc_df.dropna()
y_test_df=pd.DataFrame(y_test, columns=['close'], index=t_df.index)
y_pred_df=pd.DataFrame(y_pred, columns=['close'], index=t_df.index)

ax1=y_test_df.plot()
y_pred_df.plot(ax=ax1)
plt.legend(['test','pred'])
plt.show()
