import pandas as pd
import numpy as np
import seaborn as sns

table = pd.read_csv ("exoplanetes.csv", comment="#")
for elt in table.columns:
    print (elt)

df = table[['pl_name', 'hostname', 'discoverymethod', 'disc_year', 'disc_facility', 'sy_dist']]

sample = df
sample.head ()

df1 = sample.groupby (by='disc_year').count ().loc[:, 'pl_name'].rename({'pl_name':'number'})
sns.lineplot (data=df1).set(title='Number of exoplanet discoverder by year')

df2 = sample.loc [:, ['disc_year', 'disc_facility', 'sy_dist']]
df2.head ()
ax = sns.scatterplot (data=df2, x='disc_year', y='sy_dist', hue='disc_facility')
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))

df3 = sample.groupby (by='disc_facility').count ().loc[:, 'pl_name']
sns.set(rc={"figure.figsize":(40, 20)})
ax = sns.barplot (data=df3)
ax.tick_params(axis='x', labelrotation=40)
ax.set_title ("Number of stars discovered by facility")
sns.set(rc={"figure.figsize":(12.0, 7.0)})


