# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import scipy as sp
# %%
table = pd.read_csv ("exoplanetes.csv", comment="#")
# %%
df = table[['pl_name', 'hostname', 'discoverymethod', 'disc_year', 'disc_facility', 'sy_dist', 'pl_orbsmax', 'pl_orbper']]
# %%
sample = df
sample.head ()
# %%
df1 = sample.groupby (by='disc_year').count ().loc[:, 'pl_name'].rename({'pl_name':'number'})
sns.lineplot (data=df1).set(title='Number of exoplanet discoverder by year')
# %%
df2 = sample.loc [:, ['disc_year', 'disc_facility', 'sy_dist']]
df2.head ()
ax = sns.scatterplot (data=df2, x='disc_year', y='sy_dist', hue='disc_facility', s=10)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
# %%
df3 = sample.groupby (by='disc_facility').count ().loc[:, 'pl_name']
ax = sns.barplot (data=df3)
ax.tick_params(axis='x', labelrotation=40)
ax.set_title ("Number of stars discovered by facility")
# %%
df4 = sample.loc[:, ['pl_orbsmax', 'pl_orbper']].dropna ().sort_values (by='pl_orbsmax').iloc[:-6]
df4['logorb'] = np.log(df4['pl_orbsmax'])
df4['logperiod'] = np.log(df4['pl_orbper'])
ax = sns.regplot (data=df4, x='logorb', y='logperiod', line_kws=dict(color="r"))
ax.set (title="Periode de révolution en fonction du demi grand-axe de la trajectoire\n avec regression linéaire (3ème loi de Kepler)", xlabel="Log (demi grand-axe)", ylabel="log (periode de révolution)")


# %%
table.plot(x='sy_pnum', y='st_mass', style='.', xlabel='nombre planètes', ylabel='masse étoile', legend=False)
table.plot(x='sy_pnum', y='st_dens', style='.', xlabel='nombre planètes', ylabel='densité étoile', legend=False)
table.plot(x='sy_pnum', y='st_rad', style='.', xlabel='nombre planètes', ylabel='rayon étoile', legend=False);

# %% [markdown]
# Les étoiles ayant le plus de planètes dans leur système sont les plus petites, peu denses. 
# Toutefois, on remarque que les étoiles des systèmes à 7 planètes semblent plus denses que celles des systèmes à 5, 6 ou 8 planètes.


table.plot(x='sy_snum', y='st_mass', style='.', xlabel='nombre étoiles', ylabel='masse étoile', legend=False)
table.plot(x='sy_snum', y='st_dens', style='.', xlabel='nombre étoiles', ylabel='densité étoile', legend=False)
table.plot(x='sy_snum', y='st_rad', style='.', xlabel='nombre étoiles', ylabel='rayon étoile', legend=False);

# %% [markdown]
# On observe le même phénomène avec le nombre d’étoiles des systèmes. Il y a cependant une étoile d’un système à 3 étoiles qui est particulièrement dense.

# %%

Earth_like={}
Earth_like['pl_rade']=(0.5,2)
Earth_like['pl_masse']=(0.5,2)
Earth_like['pl_orbeccen']=(0,0.2)

Earth_like['st_teff']=(4500,7000)
Earth_like['st_mass']=(0.1,10)

# %%

def dict_to_mask(df,dict):
    mask=df['disc_year'] > 0
    keys=['pl_name','sy_dist']
    for key in dict:
        keys.append(key)
        if type(dict[key]) == tuple:
            mask_key = (df[key] >= dict[key][0]) & (df[key] <= dict[key][1])
       
        else:
            mask_key = df[key] == dict[key]
        
        mask = mask & mask_key

    return df[mask][keys]

# %%

df=dict_to_mask(table,Earth_like)
print('Earth-like planets:')
print(df)

