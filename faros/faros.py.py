


import pandas as pd
import matplotlib

df = pd.read_csv("avocado.csv")

albany_df = df[df['region']=='Albany']

albany_df = albany_df.set_index("Date", inplace=True)

albany_df['AveragePrice'].plot()

#print(albany_df.head())

