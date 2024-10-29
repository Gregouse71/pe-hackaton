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
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("exoplanetes.csv", comment="#")

# %%
df.set_index('sy_dist').groupby(by='discoverymethod')['disc_year'].plot(style='.')
#test = df.groupby(by='discoverymethod')
#test.plot(x='sy_dist', y='disc_year', kind='scatter')

# %%
df.describe()

# %%
ax = sns.relplot(data=df, x="sy_dist", y="disc_year", hue="discoverymethod")
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))

# %%
df.set_index("st_age")[['sy_bmag', 'sy_vmag', 'sy_jmag', 'sy_hmag', 'sy_kmag', 'sy_umag']].plot(style=".", ms=1)

# %%
(df.dtypes == object).sum()


# %%
df.isna().any(axis=1).unique() # toutes les planètes ont au moins un NaN

# %%
# tentative de regrouper les étoiles par catégories en fonction de leur température.
# échec, c'es très continu et pas du tout dispersé
df[df["st_teff"]< 10000].sort_values("st_teff").set_index("st_teff", drop=False)["st_teff"].plot(style=".", ms=1)

# %%
# pas plus concluant pour la température
df.sort_values("sy_vmag").set_index("sy_vmag", drop=False)["sy_vmag"].plot(style=".", ms=1)

# %%
df.sort_values("pl_dens").set_index("pl_dens", drop=False)["pl_dens"].dropna().iloc[:-2].plot(style=".", ms=1)

# %%
# Il manque des colonnes, notamment st_teff_reflink qui est documentée

# %%
df.sort_values("pl_dens").set_index("pl_dens", drop=False).index.to_series().isna().count()

# %%
