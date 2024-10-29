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
sns.relplot(data=df, x="sy_dist", y="disc_year", hue="discoverymethod", legend=False)

# %%
