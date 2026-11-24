import pandas as pd
df=pd.read_csv('insurance.csv')
print(df.isnull().sum())
print(df.describe())
df=df[df["children"]>4]