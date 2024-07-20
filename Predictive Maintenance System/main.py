import pandas as pd
import seaborn as sns
import numpy as np
data = pd.read_csv("ai4i2020.csv")
data.head()
data.tail()
data.columns
data.shape
data.describe()
data.isnull().sum()
sns.relplot(x='Air temperature [K]',y='Process temperature [K]',data=data)
sns.relplot(x='Air temperature [K]',y='Rotational speed [rpm]',data=data)
sns.relplot(x='Air temperature [K]',y='Torque [Nm]',hue='Tool wear [min]',data=data)