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
df = table[['pl_name', 'hostname', 'discoverymethod', 'disc_year', 'disc_facility', 'sy_dist', 'pl_orbsmax', 'pl_orbper', "st_age", 'sy_bmag', 'sy_vmag', 'sy_jmag', 'sy_hmag', 'sy_kmag', 'sy_umag', 'pl_dens', 'st_teff']]
# %%
sample = df
sample.head()
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
# tracé avec pandas de la découverte des étoiles selon la distance
df.set_index('sy_dist').groupby(by='discoverymethod')['disc_year'].plot(style='.')
# et avec seaborn
sns.relplot(data=df, x="sy_dist", y="disc_year", hue="discoverymethod", legend=False)

# %%
# est-ce que la luminosité des étoiles diminue avec l'âge ?
df.set_index("st_age")[['sy_bmag', 'sy_vmag', 'sy_jmag', 'sy_hmag', 'sy_kmag', 'sy_umag']].plot(style=".", ms=1)
# Pas trop

# %%
table.isna().any(axis=1).unique() # toutes les planètes ont au moins un NaN

# %%
# tentative de regrouper les étoiles par catégories en fonction de leur température.
# échec, c'est très continu et pas du tout regroupé
df[df["st_teff"]< 10000].sort_values("st_teff").set_index("st_teff", drop=False)["st_teff"].plot(style=".", ms=1)

# %%
# pas plus concluant pour la température
df.sort_values("sy_vmag").set_index("sy_vmag", drop=False)["sy_vmag"].plot(style=".", ms=1)

# %%
# Pas beaucoup mieux pour la densité, mais beaucoup de NaN et quelques rares planètes très denses
df.sort_values("pl_dens").set_index("pl_dens", drop=False)["pl_dens"].dropna().plot(style=".", ms=1)

# %% [markdown]
# Il manque des colonnes, notamment st_teff_reflink qui est documentée mais pas présente

# %%
