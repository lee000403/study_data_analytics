import pandas as pd
import numpy as np
import re

df_TFD = pd.read_csv('datasets/TitanicFromDisaster_train.csv')

print(df_TFD)

df_TFD["Initial"] = 0
for i in df_TFD:
    df_TFD["Initial"] = df_TFD["Name"].str.extract('([A-Za-z]+)\.')
df_TFD["Initial"].unique()
print(df_TFD["Initial"].unique())

df_TFD = df_TFD['Name'].unique()
df_TFD = pd.DataFrame(df_TFD)


pattern = r'^([^,]+)'
df_Name_extract = df_TFD[0].str.extract(pattern)
print(df_Name_extract)
print(df_TFD.isnull().sum())

