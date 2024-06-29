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

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()