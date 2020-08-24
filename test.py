from initial_thoughts import HomemadeKmode

import pandas as pd

data = pd.read_csv('Data set/bankmarketing.csv')

data = data[data.columns[data.dtypes == object]]

# data = data.iloc[:20,:]

print(data.head())

kmode = HomemadeKmode(n_clusters=2, max_iter=100)

kmode.fit(data.values)
kmode.predict()