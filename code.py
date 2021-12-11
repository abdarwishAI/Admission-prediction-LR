import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso, RidgeCV, LassoCV, ElasticNet, ElasticNetCV, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df= pd.read_csv('Admission_Prediction.csv')
df.isnull().sum()
df.columns = [c.replace(' ', '_') for c in df.columns]
df1= df.drop(columns='Serial_No.')
x= df1.drop(columns='Chance_of_Admit_')
y=df1['Chance_of_Admit_']
print (y)

#Try LinearRegression
from sklearn.linear_model import LinearRegression
x_train, x_test , y_train, y_test = train_test_split(x, y, test_size =0.3)
lr = LinearRegression()
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
error = np.sqrt(mean_squared_error(y_test,y_pred))
print('error = %f' %error )
mse= mean_squared_error(y_test,y_pred)
print ('mean squared error = %f' %mse)

model = pickle.dump(lr, open('ML_Admission_final.pkl', 'wb'))
