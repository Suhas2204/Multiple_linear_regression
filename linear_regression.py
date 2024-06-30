import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

# %matplotlib inline

import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
response = requests.get(url)

# with open("FuelConsumption.csv", "wb") as file:
# This opens a new file named "FuelConsumption.csv" in write-binary mode ("wb").
# This means we are creating a file that we can write to and it will store binary data.
with open("FuelConsumption.csv", "wb") as file:
    file.write(response.content)

# df = pd.read_csv("FuelConsumption.csv"): This reads the CSV file into a pandas DataFrame named df.
df = pd.read_csv("FuelConsumption.csv")

# take a look at the dataset
df.head()

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(9)

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='magenta')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='magenta')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


from sklearn import linear_model
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)


y_hat= regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Mean Squared Error (MSE) : %.2f"       # '%.2f' indicates that the floating point number should be placed there with 2 decimal places.
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))